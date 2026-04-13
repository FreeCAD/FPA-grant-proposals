"""
Tests for FreeCAD Design System Theme API

Run with: python -m pytest tests/ -v
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api import (
    getThemeToken,
    getThemeTokens,
    setTheme,
    getCurrentTheme,
    getAvailableThemes,
    getTokenCategories,
    validateTokenName,
    parseTokenValue,
)


class TestThemeTokens(unittest.TestCase):
    """Test design token retrieval functions."""

    def setUp(self):
        setTheme("dark")

    def test_get_single_token(self):
        """Test retrieving a single token."""
        token = getThemeToken("color-accent-primary")
        self.assertEqual(token, "#007acc")

    def test_get_token_with_dash(self):
        """Test token name with dash separator."""
        token = getThemeToken("font-size-base")
        self.assertEqual(token, "12px")

    def test_get_multiple_tokens(self):
        """Test retrieving multiple tokens."""
        tokens = getThemeTokens(["color-background-primary", "color-text-primary"])
        self.assertIn("color-background-primary", tokens)
        self.assertIn("color-text-primary", tokens)
        self.assertEqual(tokens["color-background-primary"], "#1e1e1e")
        self.assertEqual(tokens["color-text-primary"], "#cccccc")

    def test_get_all_tokens(self):
        """Test retrieving all tokens."""
        tokens = getThemeTokens()
        self.assertGreater(len(tokens), 50)
        self.assertIn("color-accent-primary", tokens)
        self.assertIn("font-size-base", tokens)
        self.assertIn("spacing-lg", tokens)

    def test_invalid_token_raises_error(self):
        """Test that invalid token raises KeyError."""
        with self.assertRaises(KeyError):
            getThemeToken("invalid-token-name")

    def test_token_values_are_consistent(self):
        """Test that dark theme tokens are consistent."""
        tokens = getThemeTokens()
        self.assertEqual(tokens["color-background-primary"], "#1e1e1e")
        self.assertEqual(tokens["color-accent-primary"], "#007acc")


class TestThemeSwitching(unittest.TestCase):
    """Test theme switching functionality."""

    def test_default_theme(self):
        """Test default theme is dark."""
        theme = getCurrentTheme()
        self.assertEqual(theme, "dark")

    def test_set_dark_theme(self):
        """Test setting dark theme."""
        result = setTheme("dark")
        self.assertTrue(result)
        self.assertEqual(getCurrentTheme(), "dark")

    def test_set_light_theme(self):
        """Test setting light theme."""
        result = setTheme("light")
        self.assertTrue(result)
        self.assertEqual(getCurrentTheme(), "light")

    def test_light_theme_different_values(self):
        """Test light theme has different values."""
        setTheme("light")
        token = getThemeToken("color-background-primary")
        self.assertEqual(token, "#ffffff")

    def test_invalid_theme_returns_false(self):
        """Test invalid theme name returns False."""
        result = setTheme("invalid-theme")
        self.assertFalse(result)

    def test_available_themes(self):
        """Test available themes list."""
        themes = getAvailableThemes()
        self.assertIn("dark", themes)
        self.assertIn("light", themes)


class TestTokenUtilities(unittest.TestCase):
    """Test utility functions."""

    def test_token_categories(self):
        """Test token categorization."""
        categories = getTokenCategories()
        self.assertIn("color", categories)
        self.assertIn("font", categories)
        self.assertIn("spacing", categories)
        self.assertIn("size", categories)
        self.assertIn("radius", categories)
        self.assertIn("shadow", categories)

    def test_validate_valid_token(self):
        """Test validation of valid tokens."""
        self.assertTrue(validateTokenName("color-accent-primary"))
        self.assertTrue(validateTokenName("font-size-base"))
        self.assertTrue(validateTokenName("spacing-lg"))

    def test_validate_invalid_token(self):
        """Test validation of invalid tokens."""
        self.assertFalse(validateTokenName("invalid-token"))
        self.assertFalse(validateTokenName(""))

    def test_parse_color_value(self):
        """Test parsing color values."""
        result = parseTokenValue("#007acc")
        self.assertEqual(result, "#007acc")

    def test_parse_pixel_value(self):
        """Test parsing pixel values."""
        result = parseTokenValue("12px")
        self.assertEqual(result, 12)

    def test_parse_float_value(self):
        """Test parsing float values."""
        result = parseTokenValue("10.5px")
        self.assertEqual(result, 10.5)

    def test_parse_string_value(self):
        """Test parsing string values."""
        result = parseTokenValue("Segoe UI, Arial")
        self.assertEqual(result, "Segoe UI, Arial")


class TestColorTokens(unittest.TestCase):
    """Test color token values."""

    def setUp(self):
        setTheme("dark")

    def test_background_colors(self):
        """Test background color tokens."""
        tokens = getThemeTokens([
            "color-background-primary",
            "color-background-secondary",
            "color-background-tertiary",
        ])
        self.assertEqual(tokens["color-background-primary"], "#1e1e1e")
        self.assertEqual(tokens["color-background-secondary"], "#252526")
        self.assertEqual(tokens["color-background-tertiary"], "#2d2d30")

    def test_text_colors(self):
        """Test text color tokens."""
        tokens = getThemeTokens([
            "color-text-primary",
            "color-text-secondary",
            "color-text-disabled",
        ])
        self.assertEqual(tokens["color-text-primary"], "#cccccc")
        self.assertEqual(tokens["color-text-secondary"], "#9d9d9d")
        self.assertEqual(tokens["color-text-disabled"], "#5a5a5a")

    def test_accent_colors(self):
        """Test accent color tokens."""
        tokens = getThemeTokens([
            "color-accent-primary",
            "color-accent-hover",
            "color-accent-active",
        ])
        self.assertEqual(tokens["color-accent-primary"], "#007acc")
        self.assertEqual(tokens["color-accent-hover"], "#1e8ad2")
        self.assertEqual(tokens["color-accent-active"], "#005a9e")

    def test_semantic_colors(self):
        """Test semantic color tokens."""
        tokens = getThemeTokens([
            "color-success",
            "color-warning",
            "color-error",
            "color-info",
        ])
        self.assertEqual(tokens["color-success"], "#4ec9b0")
        self.assertEqual(tokens["color-warning"], "#dcdcaa")
        self.assertEqual(tokens["color-error"], "#f14c4c")
        self.assertEqual(tokens["color-info"], "#569cd6")


class TestTypographyTokens(unittest.TestCase):
    """Test typography token values."""

    def setUp(self):
        setTheme("dark")

    def test_font_sizes(self):
        """Test font size tokens."""
        tokens = getThemeTokens([
            "font-size-xs",
            "font-size-sm",
            "font-size-base",
            "font-size-lg",
            "font-size-xl",
            "font-size-xxl",
        ])
        self.assertEqual(tokens["font-size-xs"], "10px")
        self.assertEqual(tokens["font-size-sm"], "11px")
        self.assertEqual(tokens["font-size-base"], "12px")
        self.assertEqual(tokens["font-size-lg"], "13px")
        self.assertEqual(tokens["font-size-xl"], "14px")
        self.assertEqual(tokens["font-size-xxl"], "16px")

    def test_font_weights(self):
        """Test font weight tokens."""
        tokens = getThemeTokens([
            "font-weight-normal",
            "font-weight-medium",
            "font-weight-bold",
        ])
        self.assertEqual(tokens["font-weight-normal"], "400")
        self.assertEqual(tokens["font-weight-medium"], "500")
        self.assertEqual(tokens["font-weight-bold"], "600")


class TestSpacingTokens(unittest.TestCase):
    """Test spacing token values."""

    def setUp(self):
        setTheme("dark")

    def test_spacing_tokens(self):
        """Test spacing tokens."""
        tokens = getThemeTokens([
            "spacing-xs",
            "spacing-sm",
            "spacing-md",
            "spacing-lg",
            "spacing-xl",
            "spacing-xxl",
            "spacing-xxxl",
        ])
        self.assertEqual(tokens["spacing-xs"], "2px")
        self.assertEqual(tokens["spacing-sm"], "4px")
        self.assertEqual(tokens["spacing-md"], "6px")
        self.assertEqual(tokens["spacing-lg"], "8px")
        self.assertEqual(tokens["spacing-xl"], "12px")
        self.assertEqual(tokens["spacing-xxl"], "16px")
        self.assertEqual(tokens["spacing-xxxl"], "24px")


class TestSizeTokens(unittest.TestCase):
    """Test sizing token values."""

    def setUp(self):
        setTheme("dark")

    def test_button_sizes(self):
        """Test button size tokens."""
        tokens = getThemeTokens([
            "size-button-height",
            "size-button-height-sm",
            "size-button-height-lg",
        ])
        self.assertEqual(tokens["size-button-height"], "24px")
        self.assertEqual(tokens["size-button-height-sm"], "20px")
        self.assertEqual(tokens["size-button-height-lg"], "28px")

    def test_icon_sizes(self):
        """Test icon size tokens."""
        tokens = getThemeTokens([
            "size-icon-sm",
            "size-icon-md",
            "size-icon-lg",
        ])
        self.assertEqual(tokens["size-icon-sm"], "16px")
        self.assertEqual(tokens["size-icon-md"], "20px")
        self.assertEqual(tokens["size-icon-lg"], "24px")


class TestBorderRadiusTokens(unittest.TestCase):
    """Test border radius token values."""

    def setUp(self):
        setTheme("dark")

    def test_border_radius_tokens(self):
        """Test border radius tokens."""
        tokens = getThemeTokens([
            "radius-sm",
            "radius-md",
            "radius-lg",
            "radius-round",
        ])
        self.assertEqual(tokens["radius-sm"], "2px")
        self.assertEqual(tokens["radius-md"], "3px")
        self.assertEqual(tokens["radius-lg"], "4px")
        self.assertEqual(tokens["radius-round"], "50%")


if __name__ == "__main__":
    unittest.main()
