# Design Tokens Reference

Design tokens are the atomic values that define FreeCAD's visual language.

## Token Format

Tokens follow the format:
```
--{category}-{property}-{variant}
```

Examples:
- `--color-background-primary`
- `--font-size-base`
- `--spacing-lg`

## Color Tokens

### Background Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--color-background-primary` | `#1e1e1e` | Main application background |
| `--color-background-secondary` | `#252526` | Panel and dialog backgrounds |
| `--color-background-tertiary` | `#2d2d30` | Elevated surfaces, cards |

### Surface Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--color-surface` | `#3c3c3c` | Interactive surface backgrounds |
| `--color-border` | `#3e3e42` | Default borders |
| `--color-border-strong` | `#007acc` | Focus and active borders |

### Text Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--color-text-primary` | `#cccccc` | Primary text color |
| `--color-text-secondary` | `#9d9d9d` | Secondary/muted text |
| `--color-text-disabled` | `#5a5a5a` | Disabled state text |

### Accent Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--color-accent-primary` | `#007acc` | Primary accent color (blue) |
| `--color-accent-hover` | `#1e8ad2` | Accent hover state |
| `--color-accent-active` | `#005a9e` | Accent pressed state |

### Semantic Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--color-success` | `#4ec9b0` | Success states |
| `--color-warning` | `#dcdcaa` | Warning states |
| `--color-error` | `#f14c4c` | Error states |
| `--color-info` | `#569cd6` | Information states |

## Typography Tokens

### Font Families

| Token | Value | Usage |
|-------|-------|-------|
| `--font-family-primary` | `"Segoe UI", Arial, sans-serif` | Primary UI font |
| `--font-family-mono` | `"Cascadia Code", "Consolas", monospace` | Monospace/code font |

### Font Sizes

| Token | Value | Usage |
|-------|-------|-------|
| `--font-size-xs` | `10px` | Extra small text |
| `--font-size-sm` | `11px` | Small text |
| `--font-size-base` | `12px` | Base body text |
| `--font-size-lg` | `13px` | Large text |
| `--font-size-xl` | `14px` | Heading text |
| `--font-size-xxl` | `16px` | Section headings |

### Font Weights

| Token | Value | Usage |
|-------|-------|-------|
| `--font-weight-normal` | `400` | Normal weight |
| `--font-weight-medium` | `500` | Medium weight |
| `--font-weight-bold` | `600` | Bold weight |

## Spacing Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--spacing-xs` | `2px` | Extra tight spacing |
| `--spacing-sm` | `4px` | Small spacing |
| `--spacing-md` | `6px` | Default spacing |
| `--spacing-lg` | `8px` | Large spacing |
| `--spacing-xl` | `12px` | Extra large spacing |
| `--spacing-xxl` | `16px` | Section spacing |
| `--spacing-xxxl` | `24px` | Major section spacing |

## Sizing Tokens

### Component Heights

| Token | Value | Usage |
|-------|-------|-------|
| `--size-button-height` | `24px` | Standard button height |
| `--size-button-height-sm` | `20px` | Small button height |
| `--size-button-height-lg` | `28px` | Large button height |
| `--size-input-height` | `24px` | Input field height |
| `--size-toolbar-height` | `32px` | Toolbar height |
| `--size-menubar-height` | `26px` | Menu bar height |
| `--size-statusbar-height` | `24px` | Status bar height |

### Icon Sizes

| Token | Value | Usage |
|-------|-------|-------|
| `--size-icon-sm` | `16px` | Small icon size |
| `--size-icon-md` | `20px` | Medium icon size |
| `--size-icon-lg` | `24px` | Large icon size |

### Panel Sizes

| Token | Value | Usage |
|-------|-------|-------|
| `--size-panel-width` | `250px` | Default panel width |
| `--size-panel-min-width` | `180px` | Minimum panel width |
| `--size-panel-max-width` | `400px` | Maximum panel width |

## Border Radius Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | `2px` | Small radius |
| `--radius-md` | `3px` | Medium radius (default) |
| `--radius-lg` | `4px` | Large radius |
| `--radius-round` | `50%` | Circular elements |

## Shadow Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.2)` | Subtle shadow |
| `--shadow-md` | `0 2px 4px rgba(0,0,0,0.3)` | Medium shadow |
| `--shadow-lg` | `0 4px 8px rgba(0,0,0,0.4)` | Large shadow |
| `--shadow-focus` | `0 0 0 2px rgba(0,122,204,0.4)` | Focus ring |

## Accessing Tokens Programmatically

### Python

```python
from FreeCAD import Gui

# Single token
color = Gui.getThemeToken("color-accent-primary")

# Multiple tokens
tokens = Gui.getThemeTokens([
    "color-background-primary",
    "color-text-primary"
])

# All tokens
all_tokens = Gui.getThemeTokens()
```

### QML

```qml
import QtQuick 2.15

Rectangle {
    color: Qt.application.palette.colorBackgroundPrimary
}

Text {
    color: Qt.application.palette.colorTextPrimary
    font.pixelSize: Qt.application.palette.fontSizeBase
}
```
