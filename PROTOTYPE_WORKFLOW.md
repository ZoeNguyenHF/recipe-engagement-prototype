# Q2 App Prototype - Workflow Instructions

Quick reference guide for working on this prototype project.

---

## 1. Version Control Setup

### Check Git Status
```bash
git status
```

### Current Setup
- **Repository**: Initialized ✅
- **Branch**: main
- **Remote**: Not configured

### Add Remote Repository (if needed)
```bash
# Add GitHub remote
git remote add origin https://github.com/username/q2-app-prototype.git

# Verify remote
git remote -v

# Push to remote
git push -u origin main
```

---

## 2. Opening the Prototype Locally

### Option 1: Direct Browser Open
**Quickest method for viewing**
```bash
# Navigate to project folder and double-click index.html
# Or drag index.html to your browser
```
📍 Direct URL: `file:///Users/zoe.nguyen/Q2%20App%20Prototype/index.html`

### Option 2: HTTP Server (Recommended)
**Best for testing and development**
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m http.server 8000
```
🌐 Open in browser: **http://localhost:8000**

### Option 3: VS Code Live Server
**Best for hot-reload during development**
1. Install "Live Server" extension in VS Code
2. Right-click `index.html` → "Open with Live Server"
3. Auto-opens at `http://127.0.0.1:5500` (or similar)

---

## 3. Figma + Zest Design System Mapping

### When Implementing from Figma Designs

Use the Claude Code skill for design-to-code mapping:

```bash
# In Claude Code, run:
/zest-design-system-map
```

**Or use the full skill name:**
```
specx-base:design-system-mapping-zest-design-system-map
```

### What This Skill Provides
- ✅ Mapping between Figma Zest design system and codebase components
- ✅ Web + React Native component references
- ✅ Design token mappings (colors, spacing, typography)
- ✅ Component availability check
- ✅ Validation of design-code alignment

### If In Doubt
Use GitHub CLI to search for component references:
```bash
gh search code "component-name" --repo=your-org/your-repo
```

### Existing Zest Design Tokens in `index.html`

**Colors:**
```css
--zds-page-elevation-default
--zds-page-elevation-strong
--zds-page-elevation-raised
--zds-neutral-foreground-default
--zds-neutral-foreground-dark
--zds-neutral-foreground-darker
--zds-neutral-foreground-darkest
--zds-brand-primary-default     /* #067a46 */
--zds-brand-accent-default      /* #bbf06a */
```

**Components:**
```css
--zds-tag-*                     /* Tag styling */
--zds-button-*                  /* Button styling */
--zds-badge-*                   /* Badge styling */
--zds-stepper-*                 /* Stepper controls */
--zds-icon-*                    /* Icon colors */
--zds-bottom-navigation-*       /* Bottom nav styling */
--zds-divider-*                 /* Divider colors */
```

---

## 4. Starting a New Section - Checklist

Use this checklist every time you begin working on a new feature or section:

```markdown
- [ ] Pull latest changes: git pull
- [ ] Create feature branch: git checkout -b feature/section-name
- [ ] Open prototype: python3 -m http.server 8000
- [ ] Open in browser: http://localhost:8000
- [ ] If implementing from Figma: Run /zest-design-system-map in Claude
- [ ] Make changes in index.html
- [ ] Test changes in browser (refresh page)
- [ ] Verify Zest tokens are used (not hardcoded colors)
- [ ] Commit changes: git add . && git commit -m "Description"
- [ ] Push to remote (if configured): git push origin feature/section-name
```

---

## 5. Project Quick Reference

### Project Structure
```
Q2 App Prototype/
├── index.html              # Main React SPA (7,232 lines)
├── recipes/                # Recipe images (43 files)
│   └── *.jpg               # HelloFresh recipe photos
├── *.png, *.jpg            # Product/promotional images
├── .git/                   # Version control
└── PROTOTYPE_WORKFLOW.md   # This file
```

### Technology Stack
- **Framework**: React 18 (loaded from CDN)
- **Transpiler**: Babel Standalone (in-browser JSX)
- **Styling**: Inline CSS + Zest CSS Variables
- **No Build Tools**: Runs directly as HTML file
- **Figma Integration**: MCP capture script embedded

### Key React Components (in index.html)
- `MerchandisingWidget` - Promotional banners
- `RecipeCard` - Individual recipe display with steppers
- `Phone` - Mobile device preview frame (375x812px)
- Customization drawers - Protein goals, protein info
- Cart management - Upsell flows and add-ons
- Bottom navigation - Category filtering
- Carousel - Hero promo banners with gradients

### Asset Locations
- **Local images**: `/recipes/` folder + root directory
- **Figma assets**: Served via `figma.com/api/mcp/asset/` URLs
- **Google Fonts**: Roboto font family

---

## 6. Common Commands

### Development
```bash
# Start local server
python3 -m http.server 8000

# View in browser
open http://localhost:8000    # macOS
```

### Git Workflow
```bash
# Check status
git status

# Create branch
git checkout -b feature/your-feature-name

# Stage changes
git add .

# Commit
git commit -m "Brief description of changes"

# View commit history
git log --oneline -10

# Push to remote (if configured)
git push origin branch-name
```

### Finding Components
```bash
# Search in index.html
grep -n "component-name" index.html

# List all React components
grep -n "const.*=.*\(\) =>" index.html
```

---

## 7. Tips & Best Practices

### Design System
- ✅ Always use Zest CSS variables for colors
- ❌ Avoid hardcoded hex colors or RGB values
- ✅ Check `/zest-design-system-map` for component availability

### Version Control
- Commit frequently with descriptive messages
- Use feature branches for new sections
- Keep commits focused on single features

### Testing
- Test on mobile viewport (375x812px)
- Check both light interactions and edge cases
- Verify images load correctly from local/Figma sources

### Performance
- Images are loaded on-demand
- React runs in development mode (switch to production for final deploy)
- Consider optimizing large recipe images if needed

---

## Need Help?

- **Zest Design System**: Run `/zest-design-system-map` in Claude Code
- **Git Issues**: Check `.git/config` or ask Claude for assistance
- **Figma Questions**: Use Figma MCP tools or consult design team
- **React Errors**: Check browser console (F12 → Console tab)

---

Last updated: 2026-02-24
