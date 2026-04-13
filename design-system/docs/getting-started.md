# Getting Started with FreeCAD Design System

This guide will help you get started with the FreeCAD Design System.

## Overview

The FreeCAD Design System provides:
- **Design Tokens**: Centralized style values
- **UI Components**: Reusable component specifications
- **Stylesheets**: QSS stylesheets with SCSS preprocessing
- **API**: Programmatic access to theme properties

## Using Design Tokens

### In QSS Stylesheets

```css
QPushButton {
    background-color: var(--color-accent-primary);
    color: var(--color-text-primary);
    border-radius: var(--radius-md);
}
```

### In Python Code

```python
from FreeCAD import Gui

# Get a single token
accent_color = Gui.getThemeToken("color-accent-primary")

# Get multiple tokens
colors = Gui.getThemeTokens(["color-background", "color-text"])
```

### In QML Code

```qml
import QtQuick 2.15

Rectangle {
    color: Qt.application.palette.colorBackgroundPrimary
}
```

## Applying Stylesheets

### Load Main Stylesheet

```python
from PySide.QtGui import QApplication
from FreeCAD import Gui

# Load compiled stylesheet
with open("design-system/styles/output/main.qss", "r") as f:
    qss = f.read()

app = QApplication.instance()
app.setStyleSheet(qss)
```

### Using FreeCAD's Built-in Mechanism

```python
from FreeCADGui import getMainWindow

# Access styling for custom widgets
main_window = getMainWindow()
main_window.setStyleSheet(qss)
```

## Component Usage

### Button Example

```python
from PySide.QtGui import QPushButton

# Create a primary button
apply_btn = QPushButton("Apply")
apply_btn.setProperty("class", "primary")
apply_btn.setToolTip("Apply current settings")

# Create an icon button
icon_btn = QPushButton()
icon_btn.setProperty("class", "icon")
icon_btn.setIcon(some_icon)
```

### Input Example

```python
from PySide.QtGui import QLineEdit, QSpinBox

# Standard text input
name_input = QLineEdit()
name_input.setPlaceholderText("Enter name...")

# Number input
count_input = QSpinBox()
count_input.setRange(0, 100)
count_input.setValue(10)
```

## Next Steps

- Read the [Design Tokens](tokens.md) reference
- Explore [Component Guidelines](components.md)
- Review the [API Reference](api-reference.md)
- Check [Best Practices](best-practices.md)
