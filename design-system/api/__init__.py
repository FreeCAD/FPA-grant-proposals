"""
FreeCAD Design System Theme API

This module provides programmatic access to design tokens and theme properties.
It integrates with FreeCAD's existing Style Parameters mechanism.

Usage:
    from FreeCAD import Gui
    
    # Get single token
    bg = Gui.getThemeToken("color-background-primary")
    
    # Get multiple tokens
    tokens = Gui.getThemeTokens(["color-accent", "font-size-base"])
    
    # Set theme
    Gui.setTheme("dark")
"""

import json
import os
from typing import Dict, List, Optional, Union

_THEME_DIR = os.path.join(os.path.dirname(__file__), "..", "styles")
_DEFAULT_THEME = "dark"

_DARK_TOKENS = {
    "color-background-primary": "#1e1e1e",
    "color-background-secondary": "#252526",
    "color-background-tertiary": "#2d2d30",
    "color-surface": "#3c3c3c",
    "color-border": "#3e3e42",
    "color-border-strong": "#007acc",
    "color-text-primary": "#cccccc",
    "color-text-secondary": "#9d9d9d",
    "color-text-disabled": "#5a5a5a",
    "color-accent-primary": "#007acc",
    "color-accent-hover": "#1e8ad2",
    "color-accent-active": "#005a9e",
    "color-success": "#4ec9b0",
    "color-warning": "#dcdcaa",
    "color-error": "#f14c4c",
    "color-info": "#569cd6",
    "font-family-primary": '"Segoe UI", Arial, sans-serif',
    "font-family-mono": '"Cascadia Code", "Consolas", monospace',
    "font-size-xs": "10px",
    "font-size-sm": "11px",
    "font-size-base": "12px",
    "font-size-lg": "13px",
    "font-size-xl": "14px",
    "font-size-xxl": "16px",
    "font-weight-normal": "400",
    "font-weight-medium": "500",
    "font-weight-bold": "600",
    "spacing-xs": "2px",
    "spacing-sm": "4px",
    "spacing-md": "6px",
    "spacing-lg": "8px",
    "spacing-xl": "12px",
    "spacing-xxl": "16px",
    "spacing-xxxl": "24px",
    "size-button-height": "24px",
    "size-button-height-sm": "20px",
    "size-button-height-lg": "28px",
    "size-input-height": "24px",
    "size-icon-sm": "16px",
    "size-icon-md": "20px",
    "size-icon-lg": "24px",
    "size-toolbar-height": "32px",
    "size-menubar-height": "26px",
    "size-statusbar-height": "24px",
    "size-panel-width": "250px",
    "size-panel-min-width": "180px",
    "size-panel-max-width": "400px",
    "radius-sm": "2px",
    "radius-md": "3px",
    "radius-lg": "4px",
    "radius-round": "50%",
    "shadow-sm": "0 1px 2px rgba(0,0,0,0.2)",
    "shadow-md": "0 2px 4px rgba(0,0,0,0.3)",
    "shadow-lg": "0 4px 8px rgba(0,0,0,0.4)",
    "shadow-focus": "0 0 0 2px rgba(0,122,204,0.4)",
}

_LIGHT_TOKENS = {
    "color-background-primary": "#ffffff",
    "color-background-secondary": "#f5f5f5",
    "color-background-tertiary": "#e8e8e8",
    "color-surface": "#dcdcdc",
    "color-border": "#c0c0c0",
    "color-border-strong": "#0078d4",
    "color-text-primary": "#1e1e1e",
    "color-text-secondary": "#6e6e6e",
    "color-text-disabled": "#a0a0a0",
    "color-accent-primary": "#0078d4",
    "color-accent-hover": "#106ebe",
    "color-accent-active": "#005a9e",
    "color-success": "#107c10",
    "color-warning": "#ca5010",
    "color-error": "#d13438",
    "color-info": "#0078d4",
    "font-family-primary": '"Segoe UI", Arial, sans-serif',
    "font-family-mono": '"Cascadia Code", "Consolas", monospace',
    "font-size-xs": "10px",
    "font-size-sm": "11px",
    "font-size-base": "12px",
    "font-size-lg": "13px",
    "font-size-xl": "14px",
    "font-size-xxl": "16px",
    "font-weight-normal": "400",
    "font-weight-medium": "500",
    "font-weight-bold": "600",
    "spacing-xs": "2px",
    "spacing-sm": "4px",
    "spacing-md": "6px",
    "spacing-lg": "8px",
    "spacing-xl": "12px",
    "spacing-xxl": "16px",
    "spacing-xxxl": "24px",
    "size-button-height": "24px",
    "size-button-height-sm": "20px",
    "size-button-height-lg": "28px",
    "size-input-height": "24px",
    "size-icon-sm": "16px",
    "size-icon-md": "20px",
    "size-icon-lg": "24px",
    "size-toolbar-height": "32px",
    "size-menubar-height": "26px",
    "size-statusbar-height": "24px",
    "size-panel-width": "250px",
    "size-panel-min-width": "180px",
    "size-panel-max-width": "400px",
    "radius-sm": "2px",
    "radius-md": "3px",
    "radius-lg": "4px",
    "radius-round": "50%",
    "shadow-sm": "0 1px 2px rgba(0,0,0,0.1)",
    "shadow-md": "0 2px 4px rgba(0,0,0,0.15)",
    "shadow-lg": "0 4px 8px rgba(0,0,0,0.2)",
    "shadow-focus": "0 0 0 2px rgba(0,120,212,0.4)",
}

_THEMES = {
    "dark": _DARK_TOKENS,
    "light": _LIGHT_TOKENS,
}

_TOKEN_CACHE: Dict[str, str] = {}
_CURRENT_THEME: str = _DEFAULT_THEME


def getThemeToken(name: str) -> str:
    """
    Get a single design token value.
    
    Args:
        name: Token name without the '--' prefix (e.g., 'color-background-primary')
    
    Returns:
        Token value as string (e.g., '#1e1e1e' or '12px')
    
    Raises:
        KeyError: If token name is not found
    
    Example:
        >>> from FreeCAD import Gui
        >>> Gui.getThemeToken("color-accent-primary")
        '#007acc'
    """
    global _TOKEN_CACHE, _CURRENT_THEME
    
    if name in _TOKEN_CACHE:
        return _TOKEN_CACHE[name]
    
    theme = _THEMES.get(_CURRENT_THEME, _DARK_TOKENS)
    if name not in theme:
        raise KeyError(f"Design token '{name}' not found")
    
    _TOKEN_CACHE[name] = theme[name]
    return theme[name]


def getThemeTokens(names: Optional[List[str]] = None) -> Dict[str, str]:
    """
    Get multiple design token values.
    
    Args:
        names: List of token names. If None, returns all tokens.
    
    Returns:
        Dictionary mapping token names to values
    
    Example:
        >>> from FreeCAD import Gui
        >>> Gui.getThemeTokens(["color-background-primary", "font-size-base"])
        {'color-background-primary': '#1e1e1e', 'font-size-base': '12px'}
    """
    global _CURRENT_THEME
    
    theme = _THEMES.get(_CURRENT_THEME, _DARK_TOKENS)
    
    if names is None:
        return dict(theme)
    
    return {name: getThemeToken(name) for name in names}


def setTheme(name: str) -> bool:
    """
    Set the active theme.
    
    Args:
        name: Theme name ('dark' or 'light')
    
    Returns:
        True if theme was set successfully, False otherwise
    
    Example:
        >>> from FreeCAD import Gui
        >>> Gui.setTheme("dark")
        True
    """
    global _CURRENT_THEME, _TOKEN_CACHE
    
    if name not in _THEMES:
        return False
    
    _CURRENT_THEME = name
    _TOKEN_CACHE = {}
    return True


def getCurrentTheme() -> str:
    """
    Get the name of the currently active theme.
    
    Returns:
        Current theme name ('dark' or 'light')
    
    Example:
        >>> from FreeCAD import Gui
        >>> Gui.getCurrentTheme()
        'dark'
    """
    return _CURRENT_THEME


def getAvailableThemes() -> List[str]:
    """
    Get list of available theme names.
    
    Returns:
        List of theme names
    
    Example:
        >>> from FreeCAD import Gui
        >>> Gui.getAvailableThemes()
        ['dark', 'light']
    """
    return list(_THEMES.keys())


def getThemeStylesheet(theme: Optional[str] = None) -> str:
    """
    Get compiled stylesheet for a theme.
    
    Args:
        theme: Theme name. If None, uses current theme.
    
    Returns:
        QSS stylesheet content
    
    Example:
        >>> from FreeCAD import Gui
        >>> qss = Gui.getThemeStylesheet()
    """
    theme_name = theme or _CURRENT_THEME
    qss_path = os.path.join(_THEME_DIR, "output", f"{theme_name}.qss")
    
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as f:
            return f.read()
    
    return ""


def getTokenCategories() -> Dict[str, List[str]]:
    """
    Get all tokens organized by category.
    
    Returns:
        Dictionary mapping categories to token name lists
    """
    categories = {
        "color": [],
        "font": [],
        "spacing": [],
        "size": [],
        "radius": [],
        "shadow": [],
    }
    
    for token in _DARK_TOKENS.keys():
        if token.startswith("color"):
            categories["color"].append(token)
        elif token.startswith("font"):
            categories["font"].append(token)
        elif token.startswith("spacing"):
            categories["spacing"].append(token)
        elif token.startswith("size"):
            categories["size"].append(token)
        elif token.startswith("radius"):
            categories["radius"].append(token)
        elif token.startswith("shadow"):
            categories["shadow"].append(token)
    
    return categories


def validateTokenName(name: str) -> bool:
    """
    Check if a token name is valid.
    
    Args:
        name: Token name to validate
    
    Returns:
        True if token exists, False otherwise
    """
    return name in _DARK_TOKENS


def parseTokenValue(value: str) -> Union[str, int, float]:
    """
    Parse a token value to appropriate type.
    
    Args:
        value: Token value string (e.g., '12px', '#007acc', '400')
    
    Returns:
        Parsed value as string, int, or float
    """
    if value.startswith("#"):
        return value
    
    if value.replace("px", "").replace(".", "").isdigit():
        if "." in value:
            return float(value.replace("px", ""))
        return int(value.replace("px", ""))
    
    return value
