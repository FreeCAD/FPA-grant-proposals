# API Reference

Complete reference for the FreeCAD Design System APIs.

## Python API

### Module: FreeCADGui

#### `Gui.getThemeToken(name)`

Get a single design token value.

**Parameters:**
- `name` (str): Token name without the `--` prefix

**Returns:**
- `str`: Token value

**Example:**
```python
from FreeCAD import Gui

accent = Gui.getThemeToken("color-accent-primary")
# Returns: "#007acc"
```

#### `Gui.getThemeTokens(names=None)`

Get multiple design token values.

**Parameters:**
- `names` (list of str, optional): List of token names. If None, returns all tokens.

**Returns:**
- `dict`: Dictionary mapping token names to values

**Example:**
```python
from FreeCAD import Gui

# Get specific tokens
tokens = Gui.getThemeTokens(["color-background-primary", "font-size-base"])
# Returns: {"color-background-primary": "#1e1e1e", "font-size-base": "12px"}

# Get all tokens
all_tokens = Gui.getThemeTokens()
```

#### `Gui.setTheme(name)`

Set the active theme.

**Parameters:**
- `name` (str): Theme name ("dark" or "light")

**Example:**
```python
from FreeCAD import Gui

Gui.setTheme("dark")
```

#### `Gui.getCurrentTheme()`

Get the name of the currently active theme.

**Returns:**
- `str`: Current theme name

**Example:**
```python
from FreeCAD import Gui

current = Gui.getCurrentTheme()
# Returns: "dark"
```

## QML API

### Global Object: Qt.application

The design system exposes theme properties through `Qt.application`.

#### Color Properties

| Property | Type | Description |
|----------|------|-------------|
| `palette.colorBackgroundPrimary` | color | Main background |
| `palette.colorBackgroundSecondary` | color | Panel background |
| `palette.colorBackgroundTertiary` | color | Elevated surface |
| `palette.colorSurface` | color | Interactive surface |
| `palette.colorBorder` | color | Default border |
| `palette.colorBorderStrong` | color | Focus border |
| `palette.colorTextPrimary` | color | Primary text |
| `palette.colorTextSecondary` | color | Secondary text |
| `palette.colorAccentPrimary` | color | Primary accent |
| `palette.colorSuccess` | color | Success state |
| `palette.colorWarning` | color | Warning state |
| `palette.colorError` | color | Error state |
| `palette.colorInfo` | color | Info state |

#### Typography Properties

| Property | Type | Description |
|----------|------|-------------|
| `palette.fontSizeXs` | real | Extra small font |
| `palette.fontSizeSm` | real | Small font |
| `palette.fontSizeBase` | real | Base font size |
| `palette.fontSizeLg` | real | Large font |
| `palette.fontSizeXl` | real | Extra large font |
| `palette.fontFamilyPrimary` | string | Primary font |
| `palette.fontFamilyMono` | string | Monospace font |

#### Sizing Properties

| Property | Type | Description |
|----------|------|-------------|
| `palette.buttonHeight` | real | Button height |
| `palette.inputHeight` | real | Input height |
| `palette.iconSizeSm` | real | Small icon |
| `palette.iconSizeMd` | real | Medium icon |
| `palette.iconSizeLg` | real | Large icon |
| `palette.toolbarHeight` | real | Toolbar height |

### QML Usage Example

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    color: Qt.application.palette.colorBackgroundPrimary
    
    Column {
        spacing: Qt.application.palette.spacingMd
        
        Text {
            text: "Heading"
            font.pixelSize: Qt.application.palette.fontSizeXl
            font.weight: Font.Medium
            color: Qt.application.palette.colorTextPrimary
        }
        
        TextField {
            placeholderText: "Enter text..."
            height: Qt.application.palette.inputHeight
        }
        
        Button {
            text: "Submit"
            height: Qt.application.palette.buttonHeight
            background: Rectangle {
                color: Qt.application.palette.colorAccentPrimary
                radius: 3
            }
        }
    }
}
```

## JavaScript API (QML)

### ThemeManager Singleton

```qml
import "ThemeManager.js" as ThemeManager

Item {
    Component.onCompleted: {
        var tokens = ThemeManager.getTokens()
        console.log("Background:", tokens["color-background-primary"])
    }
}
```

### ThemeManager.js

```javascript
.pragma library

var _tokens = {};

function initTokens() {
    _tokens = {
        "color-background-primary": "#1e1e1e",
        "color-accent-primary": "#007acc",
        // ... all tokens
    };
}

function getToken(name) {
    return _tokens[name] || "";
}

function getTokens() {
    return Object.assign({}, _tokens);
}
```

## Backward Compatibility

The API provides backward compatibility with existing FreeCAD code:

### Legacy QPalette Access

Existing code using `QPalette` continues to work:

```python
from PySide.QtGui import QApplication

app = QApplication.instance()
palette = app.palette()

# These continue to work
bg = palette.color(QPalette.Window)
text = palette.color(QPalette.WindowText)
```

### Migration Path

1. Legacy code continues to work unchanged
2. New code should use the theme API
3. Gradual migration is supported via compatibility layer
