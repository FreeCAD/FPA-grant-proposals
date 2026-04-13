# Panel Component

## Overview

Panels (dock widgets) provide collapsible, resizable areas for tools and information.

## Panel Types

### Dock Panel
Can be docked to any edge of the main window.

### Floating Panel
Detached from main window, acts as standalone window.

### Task Panel
Specialized panel for task-specific workflows.

## Structure

```
Panel
├── TitleBar
│   ├── Title
│   ├── CollapseButton
│   └── FloatButton (optional)
├── ContentArea
│   └── ScrollArea (optional)
└── ResizeHandle (edges)
```

## Visual Specifications

### Panel Container

| Property | Value |
|----------|-------|
| Background | `--color-background-secondary` (#252526) |
| Border | 1px `--color-border` |
| Width | `--size-panel-width` (250px) default |
| Min Width | `--size-panel-min-width` (180px) |
| Max Width | `--size-panel-max-width` (400px) |

### Title Bar

| Property | Value |
|----------|-------|
| Height | 24px |
| Background | `--color-background-tertiary` (#2d2d30) |
| Title Color | `--color-text-primary` |
| Title Font | `--font-size-sm`, `--font-weight-medium` |
| Title Padding | 0 `--spacing-md` |

### Content Area

| Property | Value |
|----------|-------|
| Background | `--color-background-secondary` |
| Padding | `--spacing-sm` |

## Collapsed State

| Property | Value |
|----------|-------|
| Width | 24px (when docked to left/right) |
| Height | 24px (when docked to top/bottom) |
| Show only | Collapse button, rotated title |

## QSS Implementation

```qss
/* Dock Widget */
QDockWidget {
    background-color: --color-background-secondary;
    border: 1px solid --color-border;
    titlebar-close-icon: url(icons/close.svg);
    titlebar-normal-icon: url(icons/dock.svg);
}

QDockWidget::title {
    background-color: --color-background-tertiary;
    text-align: left;
    padding: 0 --spacing-md;
    min-height: --size-toolbar-height;
}

QDockWidget::title:hover {
    background-color: --color-surface;
}

/* Panel Content */
QDockWidget QScrollArea > QWidget > QWidget {
    background-color: --color-background-secondary;
    border: none;
}

/* Panel Title Bar Buttons */
QDockWidget QToolButton {
    background-color: transparent;
    border: none;
    icon-size: --size-icon-sm;
}

QDockWidget QToolButton:hover {
    background-color: --color-surface;
}
```

## Python API

```python
from FreeCAD import Gui

# Get all panels
panels = Gui.getMainWindow().findChildren(QDockWidget)

# Access panel properties
for panel in panels:
    width = panel.width()
    tokens = Gui.getThemeTokens(["size-panel-width", "color-background-secondary"])

# Customize panel
panel.setMinimumWidth(200)
panel.setMaximumWidth(500)
```

## Best Practices

1. Set reasonable min/max width constraints
2. Persist panel sizes and positions
3. Support keyboard shortcuts for toggle
4. Use consistent panel styles across application
5. Consider lazy loading for complex panels
