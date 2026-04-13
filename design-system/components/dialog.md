# Dialog Component

## Overview

Dialogs are modal or modeless windows that present information or request user input.

## Types

### Modal Dialog
Blocks interaction with parent window until dismissed.

### Modeless Dialog
Allows interaction with parent while open (e.g., tool options).

### Message Box
Simple dialogs for confirmations, warnings, errors.

## Dialog Structure

```
Dialog
├── TitleBar (native or custom)
│   ├── Title
│   └── CloseButton
├── ContentArea
│   ├── Header (optional)
│   ├── Body
│   └── Footer (optional, for action buttons)
└── ButtonBox (optional)
```

## Visual Specifications

### Window Frame

| Property | Value |
|----------|-------|
| Background | `--color-background-secondary` (#252526) |
| Border | 1px `--color-border` |
| Border Radius | `--radius-lg` (4px) |
| Shadow | `--shadow-lg` |

### Title Bar (Custom)

| Property | Value |
|----------|-------|
| Height | 28px |
| Background | `--color-background-tertiary` (#2d2d30) |
| Title Color | `--color-text-primary` |
| Title Font | `--font-size-base`, `--font-weight-medium` |

### Content Padding

| Edge | Padding |
|------|---------|
| Top | `--spacing-lg` |
| Right/Left | `--spacing-lg` |
| Bottom | `--spacing-md` |

## Standard Dialog Sizes

| Dialog Type | Default Width | Min Width | Min Height |
|-------------|---------------|-----------|------------|
| Small (Message) | 320px | 200px | 100px |
| Medium | 480px | 400px | 300px |
| Large | 640px | 500px | 400px |
| Extra Large | 800px | 600px | 500px |

## QSS Implementation

```qss
/* Dialog Window */
QDialog,
QMainWindow {
    background-color: --color-background-secondary;
    border: 1px solid --color-border;
    border-radius: --radius-lg;
}

/* Custom Title Bar */
QDialog #titleBar {
    background-color: --color-background-tertiary;
    min-height: 28px;
    max-height: 28px;
    border-top-left-radius: --radius-lg;
    border-top-right-radius: --radius-lg;
}

QDialog #titleBar QLabel {
    color: --color-text-primary;
    font-size: --font-size-base;
    font-weight: --font-weight-medium;
    padding-left: --spacing-md;
}

/* Dialog Content */
QDialog #content {
    padding: --spacing-lg;
}

/* Dialog Buttons */
QDialogButtonBox {
    button-layout: 3; /* Mac layout: Stacked */
}
```

## Message Box Variants

### Information
- Icon: `--color-info` (#569cd6)
- Used for: Informational messages

### Warning
- Icon: `--color-warning` (#dcdcaa)
- Used for: Caution messages

### Error
- Icon: `--color-error` (#f14c4c)
- Used for: Error messages

### Question
- Icon: `--color-accent-primary` (#007acc)
- Used for: Confirmation requests

## Python API

```python
from PySide.QtGui import QDialog, QMessageBox
from FreeCAD import Gui

# Create dialog
dialog = QDialog()
dialog.setProperty("class", "dialog-large")

# Message box
reply = QMessageBox.question(
    None,
    "Confirm",
    "Delete selected items?",
    QMessageBox.Yes | QMessageBox.No
)
```

## Best Practices

1. Keep dialogs focused and avoid scrolling
2. Provide clear action buttons (Apply, Cancel, Close)
3. Use appropriate dialog size for content
4. Support keyboard navigation (Tab, Enter, Escape)
5. Preserve user settings between sessions
