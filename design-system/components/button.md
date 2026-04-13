# Button Component

## Overview

Buttons trigger actions and are one of the most fundamental UI components. FreeCAD uses several button variants for different contexts.

## Variants

### Primary Button
The primary action button, used for the main action in a dialog or panel.

| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | `--color-accent-primary` (#007acc) | `--color-text-primary` (#cccccc) | none |
| Hover | `--color-accent-hover` (#1e8ad2) | `--color-text-primary` | none |
| Active | `--color-accent-active` (#005a9e) | `--color-text-primary` | none |
| Disabled | `--color-surface` (#3c3c3c) | `--color-text-disabled` (#5a5a5a) | none |

### Secondary Button
Used for secondary actions that complement the primary action.

| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | `--color-surface` (#3c3c3c) | `--color-text-primary` | `--color-border` |
| Hover | `--color-background-tertiary` (#2d2d30) | `--color-text-primary` | `--color-border` |
| Active | `--color-background-secondary` (#252526) | `--color-text-primary` | `--color-border` |
| Disabled | `--color-surface` | `--color-text-disabled` | `--color-border` |

### Icon Button
Used in toolbars and compact areas where icons are preferred.

| State | Background | Icon | Border |
|-------|------------|------|--------|
| Default | transparent | `--color-text-primary` | none |
| Hover | `--color-surface` (#3c3c3c) | `--color-text-primary` | none |
| Active | `--color-background-tertiary` (#2d2d30) | `--color-accent-primary` | `--color-border-strong` |
| Disabled | transparent | `--color-text-disabled` | none |

## Sizing

| Size | Height | Min Width | Padding | Font Size |
|------|--------|-----------|---------|-----------|
| Small | `--size-button-height-sm` (20px) | 50px | 4px 8px | `--font-size-sm` (11px) |
| Default | `--size-button-height` (24px) | 60px | 4px 12px | `--font-size-base` (12px) |
| Large | `--size-button-height-lg` (28px) | 80px | 6px 16px | `--font-size-lg` (13px) |

## Border Radius

All buttons use `--radius-md` (3px) border radius.

## Typography

- Font Family: `--font-family-primary`
- Font Weight: `--font-weight-medium` (500)
- Text Transform: none (preserve case)

## Spacing

Internal padding follows spacing tokens:
- Horizontal padding: `--spacing-md` to `--spacing-lg`
- Vertical padding: `--spacing-sm` to `--spacing-md`

## QSS Implementation

```qss
/* Primary Button */
QPushButton[class="primary"] {
    background-color: --color-accent-primary;
    color: --color-text-primary;
    border: none;
    border-radius: --radius-md;
    padding: --spacing-sm --spacing-lg;
    min-height: --size-button-height;
    font-family: --font-family-primary;
    font-size: --font-size-base;
    font-weight: --font-weight-medium;
}

QPushButton[class="primary"]:hover {
    background-color: --color-accent-hover;
}

QPushButton[class="primary"]:pressed {
    background-color: --color-accent-active;
}

QPushButton[class="primary"]:disabled {
    background-color: --color-surface;
    color: --color-text-disabled;
}

/* Secondary Button */
QPushButton[class="secondary"] {
    background-color: --color-surface;
    color: --color-text-primary;
    border: 1px solid --color-border;
    border-radius: --radius-md;
    padding: --spacing-sm --spacing-lg;
    min-height: --size-button-height;
}

/* Icon Button */
QPushButton[class="icon"] {
    background-color: transparent;
    border: none;
    border-radius: --radius-sm;
    padding: --spacing-xs;
    min-width: --size-icon-lg;
    min-height: --size-icon-lg;
    icon-size: --size-icon-md;
}

QPushButton[class="icon"]:hover {
    background-color: --color-surface;
}
```

## Accessibility

- All buttons must have accessible text labels
- Use `toolTip` for additional context
- Focus indicators use `--shadow-focus` ring
- Minimum touch target: 24x24px

## Usage Examples

### Python Usage
```python
from PySide.QtGui import QPushButton

button = QPushButton("Apply")
button.setProperty("class", "primary")
button.setToolTip("Apply current settings")
```

### QML Usage
```qml
import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    text: "Apply"
    palette.button: Qt.application.palette.colorAccentPrimary
    palette.buttonText: Qt.application.palette.colorTextPrimary
}
```
