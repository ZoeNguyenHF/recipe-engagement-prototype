# Customization Feature - Revert Guide

## Overview
This guide explains how to revert the customization feature added to the rating drawer for Milestone 5.

## What Was Added
The customization feature displays what protein the customer ordered when they rate a recipe. The customization is pre-filled from order data and shown automatically when:
1. Adding a new rating by clicking the "Add your rating" button or rating banner stars
2. Editing their existing review

## How to Revert

All changes are marked with comments:
```javascript
// CUSTOMIZATION FEATURE - MILESTONE 5 - REVERT POINT
... code to remove ...
// END CUSTOMIZATION FEATURE
```

### Method 1: Manual Removal
1. Open `/Users/zoe.nguyen/Q2 App Prototype/q2-prototype-working version.html`
2. Search for `CUSTOMIZATION FEATURE - MILESTONE 5 - REVERT POINT`
3. Delete all code blocks between the start and end comments (inclusive of the comments)

### Method 2: Search and Replace
Search for the following pattern and delete all occurrences:
```
// CUSTOMIZATION FEATURE - MILESTONE 5 - REVERT POINT
[any lines]
// END CUSTOMIZATION FEATURE
```

## Changes Made

### 1. Recipe Data (Line ~980)
Added customisation field to recipe with id: 2:
```javascript
isDelivered: true, // Recipe was delivered to user
customisation: "salmon", // Pre-filled customisation from order
```

### 2. State Declaration (Line ~14076)
```javascript
const [selectedCustomisation, setSelectedCustomisation] = useState(null);
```

### 3. UI Section in Feedback Drawer (Line ~17322)
- Added "Your customisation" display section
- Shows "You made this with [protein]" text
- Appears between theme ratings and comment textarea
- Only visible when `features.customisationLabel` is enabled AND customisation exists

### 4. Submission Handler (Line ~17453)
- Added `customisation: selectedCustomisation` to feedback object
- Added reset on close

### 5. Backdrop Close Handler (Line ~16915)
- Added `setSelectedCustomisation(null)` reset

### 6. "Add Your Rating" Button (Line ~14502)
- Pre-fills customisation from `recipe.customisation`

### 7. Rating Banner Stars (Line ~14798)
- Pre-fills customisation from `recipe.customisation`

### 8. Edit Button Handler (Line ~15618)
- Added loading existing customisation: `setSelectedCustomisation(userSubmittedFeedback.customisation || null)`

### 9. User Review Object (Line ~15304)
- Added `customisation: userSubmittedFeedback.customisation || null`

## Testing After Revert
1. Open the prototype in Milestone 5
2. Click "Add your rating" or rating banner stars
3. Verify the customization section is NOT visible in the drawer
4. Submit a rating and check that no customization text appears on the review

## Feature Details (for reference)

### How It Works
- Customisation is stored in recipe data (e.g., `customisation: "salmon"`)
- When rating drawer opens, it automatically loads from `recipe.customisation`
- No user interaction needed - it's display-only

### Display Format
In the rating drawer:
```
Your customisation
You made this with salmon
```

In the review card:
```
"2 days ago | customised with salmon"
```

### Visibility
- Only shows when Milestone 5 feature `customisationLabel` is enabled
- Only displays if the recipe has a `customisation` value
- Appears in both new rating and when editing existing review
