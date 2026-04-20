# Recipe Engagement Q2 Plan - Presentation

A lightweight presentation showcasing the Q2 Rating features using the Shopping Journey template structure.

## Structure

```
presentation/
├── index.html              # Main presentation file
├── styles.css              # Styling (from Shopping Journey Q2)
├── script.js               # Navigation logic
└── README.md              # This file
```

## Features Covered

### Rating (2 features)

1. **Community Rating** - Display ratings during meal selection for social proof
2. **Rating entries** - Multiple entry points across the user journey

## Template Structure

This presentation uses the Shopping Journey Q2 template format with:
- **Left sidebar navigation** - Simple, clean section structure
- **Full-width prototype frame** - Interactive Q2 prototype embedded
- **Right sidebar metadata** - Feature name, hypothesis, and viewing instructions
- **Lightweight design** - Only essential Rating section included

## Content Format

Each feature page includes:
- **Feature name** - Clear identification
- **Hypothesis** - If/then/because statement explaining the expected impact
- **View in prototype** - Instructions for exploring the feature in the embedded prototype

## Features Detail

### Community Rating
**Hypothesis:** If we display community ratings prominently during meal selection, then users will make more confident purchase decisions and increase conversion rates, because social proof reduces uncertainty and validates recipe quality at the moment of decision.

**In Prototype:** Browse recipe cards to see star ratings and review counts. Click into recipe details for expanded rating information.

### Rating Entries
**Hypothesis:** If we provide multiple strategic rating entry points across the user journey (menu, home, cookbook, past orders, cooking flow, and post-delivery), then we will increase rating submission volume by 50-70%, because meeting users at contextually relevant moments reduces friction and captures feedback when the experience is fresh in their minds.

**Entry Points:**
- Menu & Home: Rate CTA on recipe cards
- Past Orders: Rate completed meals from order history
- Recipe Details: Rate from delivered recipe detail views
- Cooking Flow: Rate during or after cooking experience

## Usage

**IMPORTANT: Server Setup**

The presentation MUST be served from the parent directory (`Q2 App Prototype/`) to ensure all prototype images load correctly:

```bash
cd "/Users/zoe.nguyen/Q2 App Prototype"
python3 -m http.server 8080
```

Then open: **http://localhost:8080/presentation/index.html**

**Never serve from the presentation folder directly** - this breaks image paths in the embedded prototype.

## Browser Compatibility

- Works in all modern browsers (Chrome, Firefox, Safari, Edge)
- Responsive design adapts to different screen sizes
- Prototype iframe is full-width for optimal interaction

## Technical Notes

- Navigation is handled by `script.js` from Shopping Journey Q2 template
- All styling is in `styles.css` from Shopping Journey Q2 template
- Each page displays the full Q2 prototype in an iframe
- The prototype frame includes a gray background (#e8e8e8) for visual separation
- Sidebar metadata provides context without requiring screenshots
- **Critical**: The server must run from the parent directory (`Q2 App Prototype/`) for image paths to work
- Prototype images are referenced with relative paths (e.g., `recipes/`, `*.png`) from the prototype file location

## Prototype File Management

**CRITICAL - File Usage:**

- **Presentation Uses**: `../q2-prototype.html` - All iframes in the presentation point to this file
- **Features**: This file includes cooking mode, deep-linking to Step 6, rating system, and all Q2 features
- **Deep-linking**: The URL hash `#cooking-step-6` will automatically open the first recipe's cooking flow at Step 6

**If you need to make changes to the prototype:**
1. Make a copy of q2-prototype.html with a different name (e.g., q2-prototype-test.html)
2. Work on the copy and test thoroughly
3. Only when fully tested and working, replace q2-prototype.html
4. NEVER directly edit q2-prototype.html while the presentation is actively being used
5. Always test by opening the prototype directly before testing in the presentation

## Design Philosophy

This lightweight approach focuses on:
- **Simplicity** - Only 2 core rating features
- **Hypothesis-driven** - Clear if/then/because statements
- **Interactive** - Users explore features directly in the prototype
- **Context-rich** - Sidebar provides guidance without cluttering the view
