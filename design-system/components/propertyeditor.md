# Property Editor Component

## Overview

The property editor displays and edits object properties in a structured format.

## Structure

```
PropertyEditor
├── Header
│   ├── Title
│   └── FilterInput
├── PropertyGroup[]
│   ├── GroupHeader
│   │   ├── CollapseIndicator
│   │   ├── GroupName
│   │   └── GroupIcon
│   └── PropertyItem[]
│       ├── PropertyName
│       ├── PropertyValue
│       └── PropertyIndicator
└── ScrollArea
```

## Header

| Property | Value |
|----------|-------|
| Background | `--color-background-secondary` (#252526) |
| Height | 28px |
| Border Bottom | 1px `--color-border` |
| Padding | `--spacing-sm` |

### Filter Input

| Property | Value |
|----------|-------|
| Height | 20px |
| Background | `--color-background-primary` (#1e1e1e) |
| Border | 1px `--color-border` |
| Border Radius | `--radius-sm` |
| Placeholder | "Filter..." |

## Property Group

### Group Header

| Property | Value |
|----------|-------|
| Background | `--color-background-tertiary` (#2d2d30) |
| Height | 22px |
| Padding | 0 `--spacing-md` |
| Text Color | `--color-text-primary` |
| Font | `--font-size-sm`, `--font-weight-medium` |

### Collapsed State

- Only header visible
- Children hidden
- Expand indicator rotated

### Expanded State

- Header + children visible
- Indicator: down-pointing arrow

## Property Item

| Property | Value |
|----------|-------|
| Row Height | 20px |
| Name Width | 40% of available space |
| Value Width | 60% of available space |
| Padding | 0 `--spacing-sm` |
| Separator | 1px bottom border `--color-border` at 10% opacity |

### States

| State | Background | Text |
|-------|------------|------|
| Default | transparent | `--color-text-primary` |
| Hover | `--color-surface` (#3c3c3c) | `--color-text-primary` |
| Selected | `--color-accent-primary` (#007acc) | `--color-text-primary` |
| Editing | `--color-background-primary` | `--color-text-primary` |
| Read-only | transparent | `--color-text-secondary` |

### Property Name

| Property | Value |
|----------|-------|
| Color | `--color-text-secondary` |
| Font | `--font-size-sm` |
| Alignment | Left |

### Property Value

| Property | Value |
|----------|-------|
| Color | `--color-text-primary` |
| Font | `--font-size-sm` |
| Alignment | Left |
| Editing Control | Varies by type |

## Value Input Types

### Text Value
- QLineEdit with `--color-background-primary`

### Number Value
- QSpinBox or QDoubleSpinBox

### Boolean Value
- QCheckBox or toggle switch

### Enum Value
- QComboBox dropdown

### Color Value
- Color swatch + edit button

### File/Path Value
- Path display + browse button

## QSS Implementation

```qss
/* Property Editor */
QWidget#PropertyEditor {
    background-color: --color-background-secondary;
}

/* Header */
PropertyEditor > QWidget > QWidget {
    background-color: --color-background-secondary;
    border-bottom: 1px solid --color-border;
    min-height: 28px;
    padding: --spacing-sm;
}

/* Filter Input */
QLineEdit#FilterInput {
    background-color: --color-background-primary;
    border: 1px solid --color-border;
    border-radius: --radius-sm;
    padding: 2px --spacing-sm;
    min-height: 20px;
    font-size: --font-size-sm;
}

QLineEdit#FilterInput:focus {
    border-color: --color-border-strong;
}

/* Group Header */
QWidget[class="groupHeader"] {
    background-color: --color-background-tertiary;
    min-height: 22px;
    padding: 0 --spacing-md;
}

QLabel[class="groupHeader"] {
    color: --color-text-primary;
    font-size: --font-size-sm;
    font-weight: --font-weight-medium;
}

/* Property Item */
QWidget[class="propertyItem"] {
    min-height: 20px;
    border-bottom: 1px solid rgba(62, 62, 66, 0.1);
}

QWidget[class="propertyItem"]:hover {
    background-color: --color-surface;
}

QWidget[class="propertyItem"]:selected {
    background-color: --color-accent-primary;
}

/* Property Name */
QLabel[class="propertyName"] {
    color: --color-text-secondary;
    font-size: --font-size-sm;
}

/* Property Value */
QLabel[class="propertyValue"] {
    color: --color-text-primary;
    font-size: --font-size-sm;
}

QLabel[class="propertyValue"][readOnly="true"] {
    color: --color-text-secondary;
}
```

## Python API

```python
from FreeCAD import Gui

# Access property editor styling
tokens = Gui.getThemeTokens([
    "color-background-secondary",
    "color-accent-primary",
    "font-size-sm"
])

# Apply to custom property editor
class MyPropertyEditor(QWidget):
    def __init__(self):
        super().__init__()
        bg = Gui.getThemeToken("color-background-secondary")
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {bg};
            }}
        """)
```

## Best Practices

1. Group related properties logically
2. Provide sensible defaults
3. Validate input before applying
4. Support undo/redo for property changes
5. Show appropriate input controls per type
6. Indicate read-only properties clearly
