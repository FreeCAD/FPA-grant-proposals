# FreeCAD Design System

## Overview

This directory contains the FreeCAD Design System - a comprehensive set of reusable UI components, visual styles, and usage guidelines designed to ensure consistency across FreeCAD's user interface.

## Design Principles

1. **Consistency**: All UI elements follow the same visual language and interaction patterns
2. **Accessibility**: Components meet WCAG 2.1 AA standards
3. **Maintainability**: Centralized tokens enable easy updates across the entire application
4. **Extensibility**: Design system supports both Qt Widgets and QML technologies
5. **Performance**: Minimal overhead with efficient styling implementation

## Directory Structure

```
design-system/
├── tokens/           # Design tokens (colors, typography, spacing)
├── components/       # Component specifications
├── styles/           # QSS stylesheets and preprocessor
├── docs/             # Documentation and usage guides
└── README.md        # This file
```

## Core Deliverables

1. **UI Component Library** - Reusable components for Figma and Penpot
   - Button, Toolbar, Dialog, Panel, Input, Menu, TreeView, PropertyEditor
   - Located in `components/` directory

2. **Design Token System** - Centralized style parameters
   - Color, typography, spacing, sizing, border radius, shadow tokens
   - Located in `tokens/` directory
   - Python API: `FreeCADGui.getThemeToken(name)`
   - QML API: `Qt.application.palette.*`

3. **Refactored Stylesheets** - Modern QSS pipeline using qtsass
   - SCSS source files in `styles/`
   - Compiled QSS output in `styles/output/`
   - Build script: `styles/build.py`

4. **Theme Access API** - Programmatic access to theme properties
   - Python: `Gui.getThemeToken()`, `Gui.getThemeTokens()`, `Gui.setTheme()`
   - QML: Global palette properties through Qt.application

5. **Documentation** - Usage guidelines and best practices
   - Getting Started, API Reference, Migration Guide
   - Component Guidelines and Best Practices
   - Located in `docs/` directory

## Quick Start

### Using Design Tokens

```python
from FreeCAD import Gui

# Get a single token
accent = Gui.getThemeToken("color-accent-primary")

# Get multiple tokens
tokens = Gui.getThemeTokens(["color-background", "font-size"])

# Get all tokens
all_tokens = Gui.getThemeTokens()
```

### Building Stylesheets

```bash
cd design-system/styles
pip install qtsass
python build.py --all
```

### Loading Stylesheet

```python
with open("design-system/styles/output/main.qss") as f:
    app.setStyleSheet(f.read())
```

## Files

- `components/button.md` - Button component specification
- `components/toolbar.md` - Toolbar component specification
- `components/dialog.md` - Dialog component specification
- `components/panel.md` - Panel component specification
- `components/input.md` - Input component specification
- `components/menu.md` - Menu component specification
- `components/treeview.md` - TreeView component specification
- `components/propertyeditor.md` - PropertyEditor component specification
- `styles/_variables.scss` - SCSS design token variables
- `styles/_base.scss` - Base widget styles
- `styles/_components.scss` - Component-specific styles
- `docs/getting-started.md` - Quick start guide
- `docs/tokens.md` - Token reference
- `docs/api-reference.md` - API documentation
- `docs/migration.md` - Migration guide
- `docs/best-practices.md` - Best practices

## License

All design system assets follow the same license as FreeCAD (LGPL-2.0+)
