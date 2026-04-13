# FreeCAD Stylesheets

This directory contains QSS stylesheets and the stylesheet preprocessor pipeline.

## Directory Structure

```
styles/
├── main.qss              # Main stylesheet entry point
├── _variables.scss       # Design token variables (qtsass)
├── _base.scss            # Base element styles
├── _components.scss      # Component-specific styles
├── _layouts.scss         # Layout and container styles
├── themes/               # Theme variants
│   ├── dark.scss         # Dark theme (default)
│   └── light.scss        # Light theme (future)
├── build.py              # Build script for qtsass compilation
└── README.md
```

## Qtsass Integration

FreeCAD uses [qtsass](https://github.com/spyder-ide/qtsass) to compile SCSS-like stylesheets to QSS.

### Installation

```bash
pip install qtsass
```

### Build Commands

```bash
# Compile all themes
python build.py --all

# Compile specific theme
python build.py --theme dark

# Watch mode (development)
python build.py --watch
```

### Variable Usage

In SCSS files, design tokens are defined as variables:

```scss
// _variables.scss
$color-background-primary: #1e1e1e;
$color-background-secondary: #252526;
$color-accent-primary: #007acc;
$font-size-base: 12px;

// qtsass will compile these to QSS variables
// --color-background-primary: #1e1e1e;
```

## Theme Compilation

The build script processes SCSS files and outputs QSS files:

1. Reads design tokens from `tokens/` directory
2. Compiles SCSS with qtsass
3. Outputs theme-specific QSS files to `output/` directory

## Usage

### Loading a Stylesheet in FreeCAD

```python
from PySide.QtGui import QApplication
from FreeCAD import Gui

# Get compiled stylesheet
with open("styles/output/main.qss", "r") as f:
    qss = f.read()

# Apply to application
app = QApplication.instance()
app.setStyleSheet(qss)

# Or use FreeCAD's built-in mechanism
Gui.setTheme("Dark")
```

### Programmatic Token Access

```python
from FreeCAD import Gui

# Single token
bg = Gui.getThemeToken("color-background-primary")

# Multiple tokens
tokens = Gui.getThemeTokens(["color-accent", "font-size-base"])

# All tokens
all_tokens = Gui.getThemeTokens()
```

## File Descriptions

### main.qss
Main entry point that imports all other stylesheets.

### _variables.scss
Design token definitions in SCSS format for the qtsass preprocessor.

### _base.scss
Base element styles (QWidget, QPushButton, QLineEdit, etc.)

### _components.scss
Component-specific styles built on base styles.

### _layouts.scss
Layout container styles (QVBoxLayout, QHBoxLayout, QSplitter, etc.)

### themes/
Theme variants with color scheme adjustments.
