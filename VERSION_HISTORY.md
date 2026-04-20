# Version History

## index-with-saved-recipes-feature.html
**Date:** February 26, 2025
**Status:** Stable snapshot

### Features Included:
- ✅ Cart drawer with tabs (Cart / Saved)
- ✅ "Your saved recipes" carousel in cart with flying animation
- ✅ Saved tab with two sections:
  - "Available this week" - All bookmarked recipes
  - "Not available this week" - Demo recipes (IDs: 8, 9, 10)
- ✅ Functional bookmark icons across all views
- ✅ Flying animation when adding from saved carousel
- ✅ Unsave toast with "Undo" button
- ✅ Recipe position preservation on undo
- ✅ Stepper controls in Saved tab
- ✅ Toast width matches Confirm button (343px)
- ✅ View remains stable when adding recipes

### Initial Saved Recipes:
- Recipes 1, 3, 5, 6, 7 - Available this week
- Recipes 8, 9, 10 - Not available this week (demo)

---

## index.html
**Status:** Current working file

Continue building new features on this file.

---

## How to Compare Versions

### Using diff:
```bash
diff index.html index-with-saved-recipes-feature.html
```

### Side-by-side comparison:
```bash
diff -y index.html index-with-saved-recipes-feature.html | less
```

### Open both files:
- Stable version: `open index-with-saved-recipes-feature.html`
- Working version: `open index.html`

### Revert to stable version:
```bash
cp index-with-saved-recipes-feature.html index.html
```
