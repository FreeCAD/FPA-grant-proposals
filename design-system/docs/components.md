# Component Guidelines

Guidelines for using and implementing UI components in FreeCAD.

## General Principles

1. **Consistency**: Use design system components to maintain visual consistency
2. **Accessibility**: Ensure all components are keyboard accessible and screen reader friendly
3. **Responsiveness**: Design for flexible layouts that adapt to different screen sizes
4. **Performance**: Minimize repaints and reflows when interacting with components

## Component Selection

### Choosing the Right Component

| Task | Recommended Component |
|------|----------------------|
| Trigger an action | `QPushButton` |
| Show available actions | `QMenu` or `QToolBar` |
| Enter short text | `QLineEdit` |
| Enter long text | `QTextEdit` |
| Select from list | `QComboBox` |
| Toggle on/off | `QCheckBox` |
| Single selection | `QRadioButton` |
| Adjust numeric value | `QSpinBox` or `QSlider` |
| Show hierarchical data | `QTreeView` |
| Show tabular data | `QTableView` |
| Group related controls | `QGroupBox` or `QFrame` |

## Button Guidelines

### Button Hierarchy

1. **Primary Button**: Use for the main action (one per dialog)
2. **Secondary Button**: Use for alternative actions
3. **Icon Button**: Use in toolbars for compact UI

### Button Sizing

- Standard height: `--size-button-height` (24px)
- Small variant: `--size-button-height-sm` (20px) for dense UI
- Large variant: `--size-button-height-lg` (28px) for emphasis

### Button Spacing

- Horizontal padding: `--spacing-lg` (8px)
- Vertical padding: `--spacing-sm` (4px)
- Spacing between buttons: `--spacing-md` (6px)

## Input Guidelines

### Labeling

- Always provide labels for input fields
- Labels should be visible (not placeholder-only)
- Position labels above or to the left of inputs
- Use colons at end of labels (e.g., "Name:")

### Validation

- Validate input on change or on blur
- Show error messages below the input
- Use red (`--color-error`) for error indicators
- Provide clear, actionable error messages

### Placeholders

- Use placeholder text for hints
- Placeholders should complement, not replace labels
- Don't use placeholder as the only instruction

## Layout Guidelines

### Spacing

- Use spacing tokens for consistent margins
- Small gap: `--spacing-sm` (4px)
- Medium gap: `--spacing-md` (6px)
- Large gap: `--spacing-lg` (8px)

### Padding

- Dialog content: `--spacing-lg` (8px)
- Panel content: `--spacing-sm` (4px)
- Toolbar items: `--spacing-xs` (2px)

### Alignment

- Group related controls together
- Align input fields vertically
- Right-align numeric inputs in tables

## Responsive Design

### Panel Resizing

- Minimum width: `--size-panel-min-width` (180px)
- Default width: `--size-panel-width` (250px)
- Maximum width: `--size-panel-max-width` (400px)

### Window Sizing

- Minimum window size: 800x600 pixels
- Default size should fit most common tasks
- Support maximize and restore states

## States Reference

### Interactive States

| State | Description | Visual Cue |
|-------|-------------|------------|
| Default | Normal appearance | Base styling |
| Hover | Mouse over element | Background change |
| Active/Pressed | Element being clicked | Darker background |
| Focused | Keyboard focus | Focus ring |
| Disabled | Not interactive | Reduced opacity |

### Selection States

| State | Description |
|-------|-------------|
| Unselected | Default appearance |
| Selected | Highlighted with accent color |
| Multi-selected | Multiple items selected |

## Accessibility Checklist

- [ ] All interactive elements have accessible names
- [ ] Keyboard navigation is supported (Tab, Enter, Escape)
- [ ] Focus indicators are visible
- [ ] Color is not the only indicator of state
- [ ] Text contrast meets WCAG 2.1 AA standards
- [ ] Touch targets are at least 24x24 pixels
- [ ] Screen reader labels are provided where needed
