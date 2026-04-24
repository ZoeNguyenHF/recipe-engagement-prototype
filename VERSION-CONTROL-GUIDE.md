# Version Control Guide

Your project now has a local Git system to track all changes!

## Quick Save (Recommended)

Use the quick save script to save a version:

```bash
./save-version.sh "describe what you changed"
```

Examples:
```bash
./save-version.sh "Updated Option 3 carousel spacing"
./save-version.sh "Fixed rating button colors"
./save-version.sh "Added new design option"
```

If you don't provide a message, it will auto-generate one with the timestamp.

## Manual Git Commands

### Save current version
```bash
git add -A
git commit -m "your message here"
```

### View version history
```bash
git log --oneline
```

### See what changed
```bash
git status
git diff
```

### Go back to a previous version
```bash
# First, find the version you want
git log --oneline

# Then restore it (use the commit hash)
git checkout abc1234 -- "Rate on Order page V1.html"
```

### Create a new branch to try something
```bash
git checkout -b experimental-design
# Make your changes...
# If you like it: git checkout main && git merge experimental-design
# If not: git checkout main (changes stay on the branch)
```

## Tips

- **Save often**: Each time you finish a change, save a version
- **Good messages**: Write clear commit messages so you know what changed
- **Experiment safely**: Use branches to try new ideas without losing your work
- **View history**: Use `git log` to see all your versions

## Current Status

You have a local Git repository tracking all your prototype files. Your versions are saved locally on your machine.

If you want to back up to GitHub or another service, let me know!
