#!/usr/bin/env python3
"""Procedurally render compass avatars without external deps.

Usage:
  python3 avatars/generate_compass_avatar.py --output avatars/codex-avatar.png
  python3 avatars/generate_compass_avatar.py --output avatars/codex-avatar-mono.png --mode mono

"""
import argparse
import math
import struct
import zlib
import binascii
from typing import Tuple

RGBA = Tuple[int, int, int, int]


def hex_to_rgb(value: str) -> Tuple[int, int, int]:
    value = value.lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError(f"Color '{value}' must be 6 hex digits")
    r = int(value[0:2], 16)
    g = int(value[2:4], 16)
    b = int(value[4:6], 16)
    return r, g, b


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def mix(c1: Tuple[int, int, int], c2: Tuple[int, int, int], t: float) -> Tuple[int, int, int]:
    return (
        int(lerp(c1[0], c2[0], t)),
        int(lerp(c1[1], c2[1], t)),
        int(lerp(c1[2], c2[2], t)),
    )


def write_png(path: str, width: int, height: int, data: bytearray) -> None:
    raw = bytearray()
    stride = width * 4
    for y in range(height):
        raw.append(0)  # filter type 0
        row = data[y * stride : (y + 1) * stride]
        raw.extend(row)

    def chunk(tag: bytes, payload: bytes) -> bytes:
        return (
            struct.pack(">I", len(payload))
            + tag
            + payload
            + struct.pack(">I", binascii.crc32(tag + payload) & 0xFFFFFFFF)
        )

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(
            chunk(
                b"IHDR",
                struct.pack(">I I B B B B B", width, height, 8, 6, 0, 0, 0),
            )
        )
        f.write(chunk(b"IDAT", zlib.compress(bytes(raw), 9)))
        f.write(chunk(b"IEND", b""))


def set_pixel(buf: bytearray, width: int, x: int, y: int, color: RGBA) -> None:
    if 0 <= x < width and 0 <= y < width:
        idx = (y * width + x) * 4
        buf[idx : idx + 4] = bytes(color)


def blend_pixel(buf: bytearray, width: int, x: float, y: float, color: RGBA) -> None:
    xi, yi = int(x), int(y)
    if not (0 <= xi < width and 0 <= yi < width):
        return
    idx = (yi * width + xi) * 4
    br, bg, bb, ba = buf[idx : idx + 4]
    sr, sg, sb, sa = color
    if sa == 255:
        buf[idx : idx + 4] = bytes(color)
        return
    alpha_src = sa / 255
    alpha_dst = ba / 255
    out_a = alpha_src + alpha_dst * (1 - alpha_src)
    if out_a == 0:
        out_rgb = (0, 0, 0)
    else:
        out_rgb = (
            int((sr * alpha_src + br * alpha_dst * (1 - alpha_src)) / out_a),
            int((sg * alpha_src + bg * alpha_dst * (1 - alpha_src)) / out_a),
            int((sb * alpha_src + bb * alpha_dst * (1 - alpha_src)) / out_a),
        )
    buf[idx] = out_rgb[0]
    buf[idx + 1] = out_rgb[1]
    buf[idx + 2] = out_rgb[2]
    buf[idx + 3] = int(out_a * 255)


def draw_disc(buf, size, cx, cy, radius, color):
    r2 = radius * radius
    for y in range(int(cy - radius - 1), int(cy + radius + 2)):
        for x in range(int(cx - radius - 1), int(cx + radius + 2)):
            if 0 <= x < size and 0 <= y < size:
                dx = x + 0.5 - cx
                dy = y + 0.5 - cy
                if dx * dx + dy * dy <= r2:
                    blend_pixel(buf, size, x, y, color)


def draw_line(buf, size, x0, y0, x1, y1, width, color):
    steps = int(max(abs(x1 - x0), abs(y1 - y0)) * 2) + 1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        draw_disc(buf, size, x, y, width / 2, color)


def draw_circle(buf, size, cx, cy, radius, width, color):
    segments = 720
    for deg in range(segments):
        ang1 = 2 * math.pi * deg / segments
        ang2 = 2 * math.pi * (deg + 1) / segments
        x1 = cx + radius * math.cos(ang1)
        y1 = cy + radius * math.sin(ang1)
        x2 = cx + radius * math.cos(ang2)
        y2 = cy + radius * math.sin(ang2)
        draw_line(buf, size, x1, y1, x2, y2, width, color)


def fill_polygon(buf, size, points, color):
    minx = int(min(p[0] for p in points)) - 1
    maxx = int(max(p[0] for p in points)) + 1
    miny = int(min(p[1] for p in points)) - 1
    maxy = int(max(p[1] for p in points)) + 1
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if not (0 <= x < size and 0 <= y < size):
                continue
            px = x + 0.5
            py = y + 0.5
            inside = True
            for i in range(len(points)):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % len(points)]
                if ((x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)) < 0:
                    inside = False
                    break
            if inside:
                blend_pixel(buf, size, x, y, color)


def render_avatar(size: int, mode: str, args) -> bytearray:
    buf = bytearray(size * size * 4)
    center = size / 2
    # background gradient
    top = args.bg_top
    bottom = args.bg_bottom
    for y in range(size):
        for x in range(size):
            dx = x - center
            dy = y - size * 0.35
            dist = (dx * dx + dy * dy) ** 0.5
            t = min(dist / (size * 0.8), 1)
            col = mix(top, bottom, t)
            set_pixel(buf, size, x, y, (*col, 255))

    grid_color = (*args.grid, int(args.grid_alpha * 255))
    spacing = args.grid_spacing
    for y in range(spacing, size, spacing):
        draw_line(buf, size, 0, y, size, y, 2, grid_color)
    for x in range(spacing, size, spacing):
        draw_line(buf, size, x, 0, x, size, 2, grid_color)

    draw_circle(buf, size, center, center, size * 0.37, 5, (*args.outer_ring, 115))
    draw_circle(buf, size, center, center, size * 0.29, 3, (*args.inner_ring, 230))

    angle = -math.radians(args.needle_angle)
    needle_len = size * 0.34
    head = (
        center + needle_len * math.sin(angle),
        center - needle_len * math.cos(angle),
    )
    tail = (
        center - needle_len * math.sin(angle),
        center + needle_len * math.cos(angle),
    )
    draw_line(buf, size, tail[0], tail[1], head[0], head[1], args.needle_width, (*args.needle_base, 255))
    draw_line(buf, size, center, center, head[0], head[1], args.needle_width, (*args.needle_tip, 255))

    perp = angle + math.pi / 2
    tip1 = (head[0] + args.tip_width * math.cos(perp), head[1] - args.tip_width * math.sin(perp))
    tip2 = (head[0] - args.tip_width * math.cos(perp), head[1] + args.tip_width * math.sin(perp))
    fill_polygon(buf, size, [head, tip1, tip2], (*args.needle_tip, 255))

    back = (
        center - args.tail_length * math.sin(angle),
        center + args.tail_length * math.cos(angle),
    )
    perp2 = angle + math.pi / 2
    tail1 = (back[0] + args.tail_width * math.cos(perp2), back[1] - args.tail_width * math.sin(perp2))
    tail2 = (back[0] - args.tail_width * math.cos(perp2), back[1] + args.tail_width * math.sin(perp2))
    fill_polygon(buf, size, [tail1, tail2, (center, center)], (*args.tail_cutout, 255))

    draw_disc(buf, size, center, center, size * 0.025, (*args.highlight, 255))
    draw_disc(buf, size, center + size * 0.12, center - size * 0.08, size * 0.012, (*args.highlight, int(255 * 0.75)))

    return buf


def color_mode_defaults(mode: str):
    if mode == "mono":
        return {
            "bg_top": (34, 34, 34),
            "bg_bottom": (12, 12, 12),
            "grid": (200, 200, 200),
            "grid_alpha": 0.2,
            "outer_ring": (220, 220, 220),
            "inner_ring": (240, 240, 240),
            "needle_base": (220, 220, 220),
            "needle_tip": (255, 255, 255),
            "tail_cutout": (20, 20, 20),
            "highlight": (255, 255, 255),
        }
    return {
        "bg_top": (18, 38, 60),
        "bg_bottom": (12, 26, 42),
        "grid": (86, 224, 255),
        "grid_alpha": 0.25,
        "outer_ring": (255, 255, 255),
        "inner_ring": (86, 224, 255),
        "needle_base": (183, 194, 212),
        "needle_tip": (255, 138, 60),
        "tail_cutout": (12, 26, 42),
        "highlight": (248, 249, 251),
    }


def main():
    parser = argparse.ArgumentParser(description="Generate compass avatar PNGs")
    parser.add_argument("--output", required=True, help="Path to save the PNG")
    parser.add_argument("--size", type=int, default=512)
    parser.add_argument("--mode", choices=["color", "mono"], default="color")
    parser.add_argument("--needle-angle", type=float, default=18)
    parser.add_argument("--needle-width", type=float, default=18)
    parser.add_argument("--tip-width", type=float, default=22)
    parser.add_argument("--tail-length", type=float, default=110)
    parser.add_argument("--tail-width", type=float, default=28)
    parser.add_argument("--grid-spacing", type=int, default=64)
    parser.add_argument("--bg-top", type=hex_to_rgb)
    parser.add_argument("--bg-bottom", type=hex_to_rgb)
    parser.add_argument("--grid", type=hex_to_rgb)
    parser.add_argument("--outer-ring", type=hex_to_rgb)
    parser.add_argument("--inner-ring", type=hex_to_rgb)
    parser.add_argument("--needle-base", type=hex_to_rgb)
    parser.add_argument("--needle-tip", type=hex_to_rgb)
    parser.add_argument("--tail-cutout", type=hex_to_rgb)
    parser.add_argument("--highlight", type=hex_to_rgb)
    parser.add_argument("--grid-alpha", type=float)
    args = parser.parse_args()

    defaults = color_mode_defaults(args.mode)
    for key, value in defaults.items():
        if getattr(args, key, None) is None:
            setattr(args, key, value)

    buf = render_avatar(args.size, args.mode, args)
    write_png(args.output, args.size, args.size, buf)


if __name__ == "__main__":
    main()
