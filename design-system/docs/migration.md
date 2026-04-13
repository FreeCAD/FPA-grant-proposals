# Migration Guide

Guide for migrating existing FreeCAD UI code to use the design system.

## Why Migrate?

- **Consistency**: Match the official FreeCAD theme
- **Maintainability**: Centralized updates when theme changes
- **Accessibility**: Built-in accessibility support
- **Future-proof**: Support for QML and multi-platform

## Migration Steps

### 1. Replace Hardcoded Colors

**Before:**
```python
widget.setStyleSheet("""
    QPushButton {
        background-color: #007acc;
        color: #cccccc;
    }
""")
```

**After:**
```python
from FreeCAD import Gui

tokens = Gui.getThemeTokens([
    "color-accent-primary",
    "color-text-primary"
])

widget.setStyleSheet(f"""
    QPushButton {{
        background-color: {tokens["color-accent-primary"]};
        color: {tokens["color-text-primary"]};
    }}
""")
```

### 2. Replace Hardcoded Sizes

**Before:**
```python
button.setFixedHeight(24)
```

**After:**
```python
from FreeCAD import Gui

height = int(Gui.getThemeToken("size-button-height"))
button.setFixedHeight(height)
```

### 3. Use Component Classes

**Before:**
```python
button = QPushButton("OK")
```

**After:**
```python
button = QPushButton("OK")
button.setProperty("class", "primary")
```

### 4. Update Layout Spacing

**Before:**
```python
layout.setSpacing(8)
```

**After:**
```python
from FreeCAD import Gui

spacing = int(Gui.getThemeToken("spacing-lg"))
layout.setSpacing(spacing)
```

## Common Patterns

### Dialog Migration

```python
# Before
class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QDialog {
                background-color: #252526;
            }
            QPushButton {
                background-color: #007acc;
                min-height: 24px;
            }
        """)

# After
class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.applyDesignSystemStyle()

    def applyDesignSystemStyle(self):
        from FreeCAD import Gui
        tokens = Gui.getThemeTokens([
            "color-background-secondary",
            "color-accent-primary",
            "size-button-height"
        ])
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {tokens["color-background-secondary"]};
            }}
            QPushButton[class="primary"] {{
                background-color: {tokens["color-accent-primary"]};
                min-height: {tokens["size-button-height"]};
            }}
        """)
```

### Widget Migration

```python
# Before
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: #1e1e1e;
            color: #cccccc;
            font-size: 12px;
        """)

# After
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.applyDesignSystemStyle()

    def applyDesignSystemStyle(self):
        from FreeCAD import Gui
        tokens = Gui.getThemeTokens([
            "color-background-primary",
            "color-text-primary",
            "font-size-base"
        ])
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {tokens["color-background-primary"]};
                color: {tokens["color-text-primary"]};
                font-size: {tokens["font-size-base"]};
            }}
        """)
```

### QML Migration

```qml
// Before
Rectangle {
    color: "#1e1e1e"
    
    Text {
        color: "#cccccc"
        font.pixelSize: 12
    }
}

// After
Rectangle {
    color: Qt.application.palette.colorBackgroundPrimary
    
    Text {
        color: Qt.application.palette.colorTextPrimary
        font.pixelSize: Qt.application.palette.fontSizeBase
    }
}
```

## Breaking Changes

### Token Naming

Old names are deprecated but still supported:

| Old Name | New Name |
|----------|----------|
| `bg-primary` | `color-background-primary` |
| `text-main` | `color-text-primary` |
| `accent-blue` | `color-accent-primary` |

### CSS Values

QSS custom properties must be used instead of direct values:

```python
# Before (won't work with new system)
widget.setStyleSheet("color: #cccccc;")

# After
widget.setStyleSheet("color: var(--color-text-primary);")
```

## Verification

After migration, verify:

1. Colors match the official theme
2. Spacing is consistent with design system
3. Components use correct classes
4. Accessibility features still work
5. No console warnings or errors

## Getting Help

If you encounter issues during migration:

1. Check the [API Reference](api-reference.md)
2. Review [Component Guidelines](../components)
3. Report issues to the FreeCAD forums
