"""
Tests for FreeCAD Design System API
"""

import sys
import os
import importlib.util

api_dir = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("api", os.path.join(api_dir, "__init__.py"))
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)

getThemeToken = api.getThemeToken
getThemeTokens = api.getThemeTokens
setTheme = api.setTheme
getCurrentTheme = api.getCurrentTheme
getAvailableThemes = api.getAvailableThemes
getTokenCategories = api.getTokenCategories
validateTokenName = api.validateTokenName
parseTokenValue = api.parseTokenValue
_DARK_TOKENS = api._DARK_TOKENS
_LIGHT_TOKENS = api._LIGHT_TOKENS


def test_getThemeToken():
    token = getThemeToken("color-background-primary")
    assert token == "#1e1e1e", f"Expected #1e1e1e, got {token}"


def test_getThemeToken_invalid():
    try:
        getThemeToken("invalid-token")
        assert False, "Should have raised KeyError"
    except KeyError:
        pass


def test_getThemeTokens_specific():
    tokens = getThemeTokens(["color-background-primary", "font-size-base"])
    assert "color-background-primary" in tokens
    assert "font-size-base" in tokens
    assert tokens["color-background-primary"] == "#1e1e1e"
    assert tokens["font-size-base"] == "12px"


def test_getThemeTokens_all():
    tokens = getThemeTokens()
    assert len(tokens) > 0
    assert "color-background-primary" in tokens
    assert "color-accent-primary" in tokens


def test_setTheme():
    result = setTheme("dark")
    assert result is True
    assert getCurrentTheme() == "dark"

    result = setTheme("light")
    assert result is True
    assert getCurrentTheme() == "light"


def test_setTheme_invalid():
    result = setTheme("invalid")
    assert result is False


def test_getAvailableThemes():
    themes = getAvailableThemes()
    assert "dark" in themes
    assert "light" in themes


def test_getTokenCategories():
    categories = getTokenCategories()
    assert "color" in categories
    assert "font" in categories
    assert "spacing" in categories
    assert "size" in categories
    assert len(categories["color"]) > 0


def test_validateTokenName():
    assert validateTokenName("color-background-primary") is True
    assert validateTokenName("invalid") is False


def test_parseTokenValue():
    assert parseTokenValue("#1e1e1e") == "#1e1e1e"
    assert parseTokenValue("12px") == 12
    assert parseTokenValue("2.5px") == 2.5
    assert parseTokenValue("auto") == "auto"


def test_light_theme_tokens():
    setTheme("light")
    token = getThemeToken("color-background-primary")
    assert token == "#ffffff", f"Expected #ffffff for light theme, got {token}"
    setTheme("dark")


def test_token_consistency():
    dark_token_count = len(_DARK_TOKENS)
    light_token_count = len(_LIGHT_TOKENS)
    assert dark_token_count == light_token_count, (
        f"Token count mismatch: dark={dark_token_count}, light={light_token_count}"
    )

    dark_keys = set(_DARK_TOKENS.keys())
    light_keys = set(_LIGHT_TOKENS.keys())
    assert dark_keys == light_keys, "Token keys must match between themes"


def test_required_tokens_exist():
    required_tokens = [
        "color-background-primary",
        "color-accent-primary",
        "color-text-primary",
        "font-size-base",
        "spacing-md",
        "size-button-height",
    ]
    for token in required_tokens:
        assert token in _DARK_TOKENS, f"Required token {token} missing"


if __name__ == "__main__":
    test_getThemeToken()
    test_getThemeToken_invalid()
    test_getThemeTokens_specific()
    test_getThemeTokens_all()
    test_setTheme()
    test_setTheme_invalid()
    test_getAvailableThemes()
    test_getTokenCategories()
    test_validateTokenName()
    test_parseTokenValue()
    test_light_theme_tokens()
    test_token_consistency()
    test_required_tokens_exist()
    print("All tests passed!")
