#!/usr/bin/env bash
# Syncs active projects from Mac to Pixel for local auditing
PROJECT_ID=$1
PROJECT_PATH=$(python3 -c "import json, sys; data = json.load(open('_state/inventory/projects.json')); print(next((p['path'] for p in data['projects'] if p['id'] == '$PROJECT_ID'), ''))")

if [[ -z "$PROJECT_PATH" ]]; then
    echo "Error: Project ID '$PROJECT_ID' not found."; exit 1
fi

echo "Syncing $PROJECT_ID to Pixel..."
ssh pixel-ai "mkdir -p ~/projects/$PROJECT_ID"
rsync -avz -e "ssh -p 8022" --exclude '.git' --exclude 'node_modules' "$PROJECT_PATH/" "pixel-ai:~/projects/$PROJECT_ID/"
