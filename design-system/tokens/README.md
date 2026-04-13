# FreeCAD Design Tokens

Design tokens are the atomic values that define FreeCAD's visual language. They provide a single source of truth for colors, typography, spacing, and other style parameters.

## Token Categories

### Color Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--color-background-primary` | `#1e1e1e` | Main application background |
| `--color-background-secondary` | `#252526` | Panel and dialog backgrounds |
| `--color-background-tertiary` | `#2d2d30` | Elevated surfaces, cards |
| `--color-surface` | `#3c3c3c` | Interactive surface backgrounds |
| `--color-border` | `#3e3e42` | Default borders |
| `--color-border-strong` | `#007acc` | Focus and active borders |
| `--color-text-primary` | `#cccccc` | Primary text color |
| `--color-text-secondary` | `#9d9d9d` | Secondary/muted text |
| `--color-text-disabled` | `#5a5a5a` | Disabled state text |
| `--color-accent-primary` | `#007acc` | Primary accent color (blue) |
| `--color-accent-hover` | `#1e8ad2` | Accent hover state |
| `--color-accent-active` | `#005a9e` | Accent pressed state |
| `--color-success` | `#4ec9b0` | Success states |
| `--color-warning` | `#dcdcaa` | Warning states |
| `--color-error` | `#f14c4c` | Error states |
| `--color-info` | `#569cd6` | Information states |

### Typography Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--font-family-primary` | `"Segoe UI", Arial, sans-serif` | Primary UI font |
| `--font-family-mono` | `"Cascadia Code", "Consolas", monospace` | Monospace/code font |
| `--font-size-xs` | `10px` | Extra small text |
| `--font-size-sm` | `11px` | Small text |
| `--font-size-base` | `12px` | Base body text |
| `--font-size-lg` | `13px` | Large text |
| `--font-size-xl` | `14px` | Heading text |
| `--font-size-xxl` | `16px` | Section headings |
| `--font-weight-normal` | `400` | Normal weight |
| `--font-weight-medium` | `500` | Medium weight |
| `--font-weight-bold` | `600` | Bold weight |

### Spacing Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--spacing-xs` | `2px` | Extra tight spacing |
| `--spacing-sm` | `4px` | Small spacing |
| `--spacing-md` | `6px` | Default spacing |
| `--spacing-lg` | `8px` | Large spacing |
| `--spacing-xl` | `12px` | Extra large spacing |
| `--spacing-xxl` | `16px` | Section spacing |
| `--spacing-xxxl` | `24px` | Major section spacing |

### Sizing Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--size-button-height` | `24px` | Standard button height |
| `--size-button-height-sm` | `20px` | Small button height |
| `--size-button-height-lg` | `28px` | Large button height |
| `--size-input-height` | `24px` | Input field height |
| `--size-icon-sm` | `16px` | Small icon size |
| `--size-icon-md` | `20px` | Medium icon size |
| `--size-icon-lg` | `24px` | Large icon size |
| `--size-toolbar-height` | `32px` | Toolbar height |
| `--size-menubar-height` | `26px` | Menu bar height |
| `--size-statusbar-height` | `24px` | Status bar height |
| `--size-panel-width` | `250px` | Default panel width |
| `--size-panel-min-width` | `180px` | Minimum panel width |
| `--size-panel-max-width` | `400px` | Maximum panel width |

### Border Radius Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | `2px` | Small radius |
| `--radius-md` | `3px` | Medium radius (default) |
| `--radius-lg` | `4px` | Large radius |
| `--radius-round` | `50%` | Circular elements |

### Shadow Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.2)` | Subtle shadow |
| `--shadow-md` | `0 2px 4px rgba(0,0,0,0.3)` | Medium shadow |
| `--shadow-lg` | `0 4px 8px rgba(0,0,0,0.4)` | Large shadow |
| `--shadow-focus` | `0 0 0 2px rgba(0,122,204,0.4)` | Focus ring |

## Implementation

Design tokens are implemented via:
- **Qt Style Sheets (QSS)**: CSS-like variables for traditional widgets
- **QSS Preprocessor**: qtsass for SCSS-like development experience
- **Python API**: `FreeCADGui.getThemeToken(name)` for programmatic access
- **QML Integration**: Theme API exposed via `Qt.application` properties

## Token Access API

```python
# Python access to design tokens
from FreeCAD import Gui

# Get a single token value
bg_color = Gui.getThemeToken("color-background-primary")

# Get multiple tokens as dictionary
tokens = Gui.getThemeTokens(["color-accent-primary", "font-size-base"])

# Get all tokens
all_tokens = Gui.getThemeTokens()
```

```qml
// QML access to design tokens
import QtQuick 2.15

Rectangle {
    color: Qt.application.palette.colorBackgroundPrimary
    Text {
        text: "Sample Text"
        font.pixelSize: Qt.application.palette.fontSizeBase
    }
}
```

## Migration Guide

When migrating existing code to use design tokens:

1. Replace hardcoded color values with token references
2. Use spacing tokens for consistent padding/margins
3. Reference typography tokens instead of explicit font settings
4. Test both light and dark theme variants

## Validation

All tokens must pass:
- WCAG 2.1 AA contrast ratio checks
- Consistency verification across components
- Cross-platform rendering validation
