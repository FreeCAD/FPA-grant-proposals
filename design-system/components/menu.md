# Menu Component

## Overview

Menus provide organized access to application commands.

## Types

### Menu Bar
Horizontal menu bar at top of main window.

### Dropdown Menu
Menu that appears when menu item is clicked.

### Context Menu
Menu that appears on right-click.

### Popup Menu
Generic popup menu.

## Menu Bar

| Property | Value |
|----------|-------|
| Background | `--color-background-secondary` (#252526) |
| Height | `--size-menubar-height` (26px) |
| Padding | 0 `--spacing-sm` |
| Item Height | `--size-menubar-height` |
| Item Padding | 0 `--spacing-md` |
| Font | `--font-size-sm` |
| Text Color | `--color-text-primary` |

### Item States

| State | Background | Text |
|-------|------------|------|
| Default | transparent | `--color-text-primary` |
| Hover | `--color-surface` (#3c3c3c) | `--color-text-primary` |
| Active (open) | `--color-background-tertiary` | `--color-accent-primary` |

## Dropdown Menu

| Property | Value |
|----------|-------|
| Background | `--color-background-secondary` |
| Border | 1px `--color-border` |
| Border Radius | `--radius-md` |
| Shadow | `--shadow-md` |
| Padding | `--spacing-xs` 0 |
| Min Width | 150px |

### Menu Item

| Property | Value |
|----------|-------|
| Height | 22px |
| Padding | 0 `--spacing-lg` |
| Spacing | `--spacing-sm` between icon and text |
| Font | `--font-size-sm` |

### Menu Item States

| State | Background | Text |
|-------|------------|------|
| Default | transparent | `--color-text-primary` |
| Hover | `--color-surface` | `--color-text-primary` |
| Selected | `--color-accent-primary` | `--color-text-primary` |
| Disabled | transparent | `--color-text-disabled` |

## Separator

- Height: 1px
- Margin: `--spacing-xs` `--spacing-lg`
- Color: `--color-border`

## Submenu Indicator

- Arrow: Right-pointing, `--size-icon-sm` (16px)
- Color: `--color-text-secondary`
- Position: Right edge, `--spacing-md` from edge

## QSS Implementation

```qss
/* Menu Bar */
QMenuBar {
    background-color: --color-background-secondary;
    border-bottom: 1px solid --color-border;
    padding: 0 --spacing-sm;
}

QMenuBar::item {
    background-color: transparent;
    padding: 0 --spacing-md;
    min-height: --size-menubar-height;
    font-size: --font-size-sm;
    color: --color-text-primary;
}

QMenuBar::item:selected {
    background-color: --color-surface;
}

QMenuBar::item:pressed {
    background-color: --color-background-tertiary;
    color: --color-accent-primary;
}

/* Dropdown Menu */
QMenu {
    background-color: --color-background-secondary;
    border: 1px solid --color-border;
    border-radius: --radius-md;
    padding: --spacing-xs 0;
}

QMenu::item {
    padding: 4px --spacing-lg;
    min-height: 22px;
    font-size: --font-size-sm;
    color: --color-text-primary;
}

QMenu::item:selected {
    background-color: --color-surface;
}

QMenu::item:disabled {
    color: --color-text-disabled;
}

QMenu::separator {
    height: 1px;
    background-color: --color-border;
    margin: --spacing-xs --spacing-lg;
}

QMenu::indicator {
    width: --size-icon-sm;
    height: --size-icon-sm;
    margin-left: --spacing-sm;
}
```

## Best Practices

1. Group related items with separators
2. Use keyboard mnemonics for common commands
3. Provide access keys for all items
4. Use icons for toolbar-like menus
5. Keep menu depth to maximum 2 levels
6. Disable rather than hide unavailable commands
