# Tree View Component

## Overview

Tree views display hierarchical data with expandable/collapsible nodes.

## Structure

```
TreeView
├── Header
│   └── HeaderItem[]
├── TreeNode[]
│   ├── ExpandIndicator
│   ├── Icon
│   ├── Label
│   └── ChildNodes[]
└── ScrollBar (if needed)
```

## Header

| Property | Value |
|----------|-------|
| Background | `--color-background-tertiary` (#2d2d30) |
| Height | 26px |
| Padding | 0 `--spacing-md` |
| Border Bottom | 1px `--color-border` |
| Text Color | `--color-text-primary` |
| Font | `--font-size-sm`, `--font-weight-medium` |

## Tree Node

| Property | Value |
|----------|-------|
| Indent | 16px per level |
| Row Height | 20px |
| Padding | 0 `--spacing-xs` |
| Vertical Spacing | 1px |

### Node States

| State | Background | Text |
|-------|------------|------|
| Default | transparent | `--color-text-primary` |
| Hover | `--color-surface` (#3c3c3c) | `--color-text-primary` |
| Selected | `--color-accent-primary` (#007acc) | `--color-text-primary` |
| Selected + Hover | `--color-accent-hover` (#1e8ad2) | `--color-text-primary` |

### Expand/Collapse Indicator

| State | Icon |
|-------|------|
| Collapsed | Right-pointing arrow |
| Expanded | Down-pointing arrow |
| Size | `--size-icon-sm` (16px) |
| Color | `--color-text-secondary` |

## Multi-Select

| State | Background | Border |
|-------|------------|--------|
| Selected | `--color-accent-primary` | none |
| Focused + Selected | `--color-accent-primary` | 1px `--color-border-strong` |

## QSS Implementation

```qss
/* Tree View */
QTreeView {
    background-color: --color-background-primary;
    border: none;
    alternate-background-color: --color-background-secondary;
    show-decoration-selected: 1;
    gridline-color: --color-border;
    font-family: --font-family-primary;
    font-size: --font-size-sm;
}

/* Header */
QTreeView::header {
    background-color: --color-background-tertiary;
    border-bottom: 1px solid --color-border;
    padding: 0 --spacing-md;
    min-height: 26px;
}

QTreeView::header::section {
    background-color: --color-background-tertiary;
    color: --color-text-primary;
    font-size: --font-size-sm;
    font-weight: --font-weight-medium;
    padding: 0 --spacing-md;
    border: none;
    border-right: 1px solid --color-border;
}

/* Tree Item */
QTreeView::item {
    height: 20px;
    padding: 0 --spacing-xs;
}

QTreeView::item:hover {
    background-color: --color-surface;
}

QTreeView::item:selected {
    background-color: --color-accent-primary;
}

QTreeView::item:selected:active {
    background-color: --color-accent-hover;
}

/* Expand/Collapse Indicator */
QTreeView::branch {
    background-color: transparent;
}

QTreeView::branch:has-children:closed {
    image: url(icons/branch-closed.svg);
}

QTreeView::branch:has-children:open {
    image: url(icons/branch-open.svg);
}

/* Text */
QTreeView::text {
    color: --color-text-primary;
}

/* Disabled State */
QTreeView:item:!enabled {
    color: --color-text-disabled;
}
```

## Python API

```python
from PySide.QtGui import QTreeView
from FreeCAD import Gui

tree = QTreeView()

# Get theme tokens
bg_color = Gui.getThemeToken("color-background-primary")
sel_color = Gui.getThemeToken("color-accent-primary")

# Apply styling
tree.setStyleSheet(f"""
    QTreeView {{
        background-color: {bg_color};
    }}
    QTreeView::item:selected {{
        background-color: {sel_color};
    }}
""")
```

## Best Practices

1. Enable alternating row colors for readability
2. Support keyboard navigation (arrows, Enter, Space)
3. Provide context menu for common actions
4. Lazy load children for large trees
5. Show selection across branches when multi-selecting
6. Persist expand/collapse state
