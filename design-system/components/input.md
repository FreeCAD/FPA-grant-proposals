# Input Component

## Overview

Input components allow users to enter and edit data.

## Types

### Text Input
Single-line text field for short inputs.

### Text Area
Multi-line text field for longer content.

### Number Input
Numeric input with optional spin controls.

### Combo Box
Dropdown selection from predefined options.

### Check Box
Binary on/off selection.

### Radio Button
Single selection from a group.

### Slider
Continuous value selection.

## Text Input Specifications

### Appearance

| Property | Value |
|----------|-------|
| Background | `--color-background-primary` (#1e1e1e) |
| Border | 1px `--color-border` |
| Border (Focus) | 1px `--color-border-strong` |
| Border Radius | `--radius-md` (3px) |
| Height | `--size-input-height` (24px) |
| Padding | `--spacing-xs` `--spacing-sm` |
| Font | `--font-family-primary`, `--font-size-base` |
| Text Color | `--color-text-primary` |
| Placeholder Color | `--color-text-secondary` |

### States

| State | Border | Background |
|-------|--------|------------|
| Default | `--color-border` | `--color-background-primary` |
| Hover | `--color-border` | `--color-background-primary` |
| Focus | `--color-border-strong` | `--color-background-primary` |
| Disabled | `--color-border` | `--color-background-tertiary` |
| Error | `--color-error` | `--color-background-primary` |

## Number Input (Spin Box)

### Appearance

| Property | Value |
|----------|-------|
| Background | `--color-background-primary` |
| Border | 1px `--color-border` |
| Height | `--size-input-height` (24px) |
| Up/Down Width | 16px |
| Up/Down Background | `--color-surface` |

### Up/Down Button States

| State | Background | Arrow Color |
|-------|------------|-------------|
| Default | `--color-surface` | `--color-text-secondary` |
| Hover | `--color-background-tertiary` | `--color-text-primary` |
| Pressed | `--color-accent-primary` | `--color-text-primary` |
| Disabled | `--color-background-tertiary` | `--color-text-disabled` |

## Combo Box

### Appearance

| Property | Value |
|----------|-------|
| Background | `--color-background-primary` |
| Border | 1px `--color-border` |
| Height | `--size-input-height` (24px) |
| Dropdown Width | 16px |
| Arrow Icon |向下 arrow, `--color-text-secondary` |

## QSS Implementation

```qss
/* Text Input */
QLineEdit {
    background-color: --color-background-primary;
    border: 1px solid --color-border;
    border-radius: --radius-md;
    padding: --spacing-xs --spacing-sm;
    min-height: --size-input-height;
    color: --color-text-primary;
    font-family: --font-family-primary;
    font-size: --font-size-base;
    selection-background-color: --color-accent-primary;
    selection-color: --color-text-primary;
}

QLineEdit:hover {
    border-color: --color-border;
}

QLineEdit:focus {
    border-color: --color-border-strong;
}

QLineEdit:disabled {
    background-color: --color-background-tertiary;
    color: --color-text-disabled;
}

/* Text Area */
QTextEdit {
    background-color: --color-background-primary;
    border: 1px solid --color-border;
    border-radius: --radius-md;
    padding: --spacing-sm;
    color: --color-text-primary;
    font-family: --font-family-primary;
    font-size: --font-size-base;
}

/* Spin Box */
QSpinBox, QDoubleSpinBox {
    background-color: --color-background-primary;
    border: 1px solid --color-border;
    border-radius: --radius-md;
    min-height: --size-input-height;
    padding-right: 16px;
}

QSpinBox::up-button, QDoubleSpinBox::up-button {
    background-color: --color-surface;
    border-left: 1px solid --color-border;
    border-top-right-radius: --radius-md;
    width: 16px;
}

QSpinBox::down-button, QDoubleSpinBox::down-button {
    background-color: --color-surface;
    border-left: 1px solid --color-border;
    border-bottom-right-radius: --radius-md;
    width: 16px;
}

/* Combo Box */
QComboBox {
    background-color: --color-background-primary;
    border: 1px solid --color-border;
    border-radius: --radius-md;
    min-height: --size-input-height;
    padding: --spacing-xs --spacing-sm;
}

QComboBox:focus {
    border-color: --color-border-strong;
}

QComboBox::drop-down {
    border: none;
    width: 16px;
}
```

## Accessibility

- All inputs must have associated labels
- Use `placeholderText` for hints
- Provide `toolTip` for complex fields
- Support keyboard navigation
- Error messages must be announced to screen readers

## Best Practices

1. Validate input in real-time where appropriate
2. Show clear error messages
3. Support common formats (dates, numbers)
4. Provide sensible defaults
5. Limit input length where appropriate
