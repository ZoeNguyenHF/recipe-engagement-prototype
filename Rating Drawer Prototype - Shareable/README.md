# Rating Drawer Prototype

This folder contains a standalone prototype for the Rating Drawer feature with multiple design options.

## How to Use

1. **Open the prototype**: Simply open `index.html` in your web browser (double-click the file)
2. **Switch between options**: Use the left sidebar to switch between:
   - **Control**: Original design
   - **Option 1**: Enhanced rating with animations
   - **Option 2**: Horizontal scrolling cards
   - **Option 3**: Chat-style conversational interface

3. **Reset an option**: Hover over any design option and click the refresh icon (↻) to reset it to the beginning flow for testing

## Features

### Control
- Standard rating drawer
- Show more recipes option
- Past orders navigation

### Option 1
- Lottie animations on star ratings
- Particle burst effects
- Enhanced visual feedback

### Option 2
- Horizontal scrolling card layout
- Particle effects for 4-5 star ratings
- Smooth scroll to next recipe after rating

### Option 3 (Chat Interface)
- Conversational chatbot interface
- Typing indicators and gradual text appearance
- Recipe carousel with smooth transitions
- Completion screen with clickable recipe thumbnails
- "Your top rated" label on 4-5 star recipes

## Testing Tips

- Click the **refresh icon** (↻) next to each option to restart the flow
- Rate recipes to see different animations and transitions
- Try clicking recipe thumbnails in Option 3's completion screen
- Navigate between previous/current/next recipes in the carousel (Option 3)

## File Structure

```
/
├── index.html                 # Main prototype file
├── recipes/                   # Recipe images folder
│   └── HelloFresh *.jpg      # Recipe photos
├── chat bot.png              # Chat bot avatar
├── Star.png                  # Star decoration
├── 3D_Beyond_the_Box.png     # 3D box illustration
├── Trophy coin.png           # Trophy coin animation
└── README.md                 # This file
```

## Browser Compatibility

This prototype works best in modern browsers:
- Chrome (recommended)
- Firefox
- Safari
- Edge

## Notes

- All images are included in this folder
- No internet connection required (runs fully offline)
- React is loaded from CDN for the prototype
- All interactions are functional and demonstrate the complete flows

---

**Version**: V3
**Last Updated**: April 2025
