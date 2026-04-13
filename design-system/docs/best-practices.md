# Best Practices

Guidelines for creating consistent, maintainable UI code in FreeCAD.

## General Principles

### Do: Use Design Tokens

Always use design tokens for colors, spacing, and typography:

```python
from FreeCAD import Gui

tokens = Gui.getThemeTokens(["color-accent", "spacing-lg", "font-size-base"])
```

### Don't: Use Hardcoded Values

Avoid hardcoded values in UI code:

```python
# Bad
widget.setStyleSheet("background-color: #007acc;")

# Good
tokens = Gui.getThemeTokens(["color-accent-primary"])
widget.setStyleSheet(f"background-color: {tokens['color-accent-primary']};")
```

## Widget Creation

### Do: Set Component Classes

Use the `class` property for semantic styling:

```python
button.setProperty("class", "primary")
```

### Don't: Use Inline Styles

Avoid setting individual style properties directly:

```python
# Bad
button.setBackgroundRole(QPalette.Button)
button.setForegroundRole(QPalette.ButtonText)

# Good
button.setProperty("class", "primary")
button.setStyleSheet(f"QPushButton[class="primary"] {{ background-color: {token}; }}")
```

## Layout

### Do: Use Design System Spacing

```python
from FreeCAD import Gui

layout.setSpacing(int(Gui.getThemeToken("spacing-lg")))
layout.setContentsMargins(
    int(Gui.getThemeToken("spacing-lg")),
    int(Gui.getThemeToken("spacing-lg")),
    int(Gui.getThemeToken("spacing-lg")),
    int(Gui.getThemeToken("spacing-lg"))
)
```

### Do: Maintain Consistent Sizing

```python
button.setFixedHeight(int(Gui.getThemeToken("size-button-height")))
input.setFixedHeight(int(Gui.getThemeToken("size-input-height")))
```

## Theming

### Do: Support Theme Changes

```python
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.apply_styles()
        FreeCADGui.getMainWindow().installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.PaletteChange:
            self.apply_styles()
        return super().eventFilter(obj, event)
```

### Do: Provide Fallbacks

```python
from FreeCAD import Gui

try:
    accent = Gui.getThemeToken("color-accent-primary")
except:
    accent = "#007acc"  # Fallback value
```

## Accessibility

### Do: Provide Accessible Names

```python
button.setAccessibleName("Apply changes")
button.setToolTip("Click to apply current settings")
```

### Do: Support Keyboard Navigation

```python
# Make widget focusable
widget.setFocusPolicy(Qt.StrongFocus)

# Handle keyboard events
def keyPressEvent(self, event):
    if event.key() == Qt.Key_Return:
        self.accept()
    super().keyPressEvent(event)
```

### Don't: Rely on Color Alone

```python
# Bad
error_label.setStyleSheet("color: red;")

# Good
error_label.setStyleSheet("color: var(--color-error);")
error_label.setAccessibleDescription("Error: Invalid input")
```

## Performance

### Do: Minimize Style Recalculation

```python
# Batch updates
widget.setUpdatesEnabled(False)
try:
    for item in items:
        item.update_content()
finally:
    widget.setUpdatesEnabled(True)
```

### Do: Cache Token Lookups

```python
class MyWidget:
    _tokens = None
    
    @classmethod
    def get_tokens(cls):
        if cls._tokens is None:
            from FreeCAD import Gui
            cls._tokens = Gui.getThemeTokens()
        return cls._tokens
```

## Testing

### Do: Test Multiple Themes

```python
def test_widget():
    from FreeCAD import Gui
    
    for theme in ["dark", "light"]:
        Gui.setTheme(theme)
        widget = create_widget()
        assert verify_contrast(widget)
```

### Do: Verify Contrast Ratios

Use automated tools to verify WCAG compliance:

```python
def verify_contrast(fg_color, bg_color):
    # Calculate contrast ratio
    # Return True if >= 4.5:1 for normal text
    # Return True if >= 3:1 for large text
```

## Documentation

### Do: Document Custom Components

```python
class CustomWidget(QWidget):
    """
    Custom widget for displaying XYZ.
    
    Usage:
        widget = CustomWidget()
        widget.setData(data)
        
    Signals:
        dataChanged: Emitted when data changes
    """
```

### Do: Include Token Usage in Docstrings

```python
def create_panel():
    """
    Create a styled panel.
    
    Uses design tokens:
        - color-background-secondary (panel background)
        - color-border (panel border)
        - spacing-lg (content padding)
    """
```

## Code Style

### Follow Existing Conventions

```python
# Use consistent naming
widget = MyCustomWidget()  # PascalCase for classes
button_id = "apply_button"  # snake_case for variables

# Use f-strings for token substitution
stylesheet = f"""
    QWidget {{
        background-color: {tokens['color-bg']};
    }}
"""
```

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Qt Style Sheets Documentation](https://doc.qt.io/qt-5/stylesheet-reference.html)
- [FreeCAD Design System](.)
