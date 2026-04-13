# Toolbar Component

## Overview

Toolbars provide quick access to frequently used commands. FreeCAD toolbars can be docked, floating, or nested.

## Structure

```
Toolbar
├── ToolbarHandle (optional, for reordering)
├── ToolButton[]
├── Separator (optional)
└── MoreButton (if overflow)
```

## Toolbar Container

| Property | Value |
|----------|-------|
| Background | `--color-background-secondary` (#252526) |
| Border | none (top: 1px `--color-border` when docked) |
| Height | `--size-toolbar-height` (32px) |
| Padding | `--spacing-sm` horizontal |

## Tool Button

| State | Background | Icon | Border |
|-------|------------|------|--------|
| Default | transparent | `--color-text-primary` | none |
| Hover | `--color-surface` (#3c3c3c) | `--color-text-primary` | none |
| Active (checked) | `--color-background-tertiary` (#2d2d30) | `--color-accent-primary` | left: 2px `--color-accent-primary` |
| Disabled | transparent | `--color-text-disabled` (#5a5a5a) | none |

## Icon Sizing

| Context | Icon Size |
|---------|-----------|
| Standard toolbar | `--size-icon-md` (20px) |
| Large toolbar | `--size-icon-lg` (24px) |
| Small/compact | `--size-icon-sm` (16px) |

## Separator

Vertical separator between tool groups:
- Width: 1px
- Color: `--color-border`
- Margin: `--spacing-xs` vertical

## QSS Implementation

```qss
/* Main Toolbar */
QToolBar {
    background-color: --color-background-secondary;
    border: none;
    border-top: 1px solid --color-border;
    padding: --spacing-xs --spacing-sm;
    spacing: --spacing-xs;
    max-height: --size-toolbar-height;
}

/* Toolbar when floating */
QToolBar[docked="false"] {
    border: 1px solid --color-border;
    border-radius: --radius-md;
}

/* Tool Button */
QToolButton {
    background-color: transparent;
    border: none;
    border-radius: --radius-sm;
    padding: --spacing-xs;
    min-width: --size-icon-lg;
    min-height: --size-icon-lg;
    icon-size: --size-icon-md;
}

QToolButton:hover {
    background-color: --color-surface;
}

QToolButton:on,
QToolButton:checked {
    background-color: --color-background-tertiary;
    border-left: 2px solid --color-accent-primary;
}

QToolButton:disabled {
    icon-color: --color-text-disabled;
}

/* Separator */
QToolBar::separator {
    width: 1px;
    background-color: --color-border;
    margin: --spacing-xs 0;
}
```

## Python API

```python
from FreeCAD import Gui

toolbar = Gui.getMainWindow().toolBar("File")
# Access theme tokens
bg_color = Gui.getThemeToken("color-background-secondary")
```

## Accessibility

- All tool buttons require `toolTip` for hover context
- Use `WhatsThis` for extended help
- Group related tools with separators
- Maintain 8px minimum spacing between groups
