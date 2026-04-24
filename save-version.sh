#!/bin/bash

# Quick version save script for Q2 App Prototype
# Usage: ./save-version.sh "your commit message"

cd "/Users/zoe.nguyen/Q2 App Prototype"

# If no message provided, use a default one
if [ -z "$1" ]; then
    MESSAGE="Update prototype - $(date '+%Y-%m-%d %H:%M:%S')"
else
    MESSAGE="$1"
fi

# Show what's changed
echo "📋 Files changed:"
git status --short

echo ""
echo "💾 Saving version with message: $MESSAGE"
echo ""

# Stage all changes
git add -A

# Commit with message
git commit -m "$MESSAGE

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

# Show the result
echo ""
echo "✅ Version saved successfully!"
echo ""
echo "📚 Recent versions:"
git log --oneline -5
