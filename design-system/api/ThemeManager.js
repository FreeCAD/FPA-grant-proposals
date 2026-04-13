// ThemeManager.js - QML Theme API Module
// Provides programmatic access to design tokens in QML

.pragma library

var _currentTheme = "dark";

var _darkTokens = {
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
    "color-info": "#569cd6"
};

var _lightTokens = {
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
    "color-info": "#0078d4"
};

var _themes = {
    "dark": _darkTokens,
    "light": _lightTokens
};

function getToken(name) {
    var tokens = _themes[_currentTheme] || _darkTokens;
    if (name in tokens) {
        return tokens[name];
    }
    console.warn("ThemeManager: Token '" + name + "' not found");
    return "";
}

function getTokens(names) {
    var result = {};
    if (names) {
        for (var i = 0; i < names.length; i++) {
            result[names[i]] = getToken(names[i]);
        }
    } else {
        var tokens = _themes[_currentTheme] || _darkTokens;
        for (var key in tokens) {
            result[key] = tokens[key];
        }
    }
    return result;
}

function setTheme(name) {
    if (name in _themes) {
        _currentTheme = name;
        return true;
    }
    console.warn("ThemeManager: Theme '" + name + "' not found");
    return false;
}

function getCurrentTheme() {
    return _currentTheme;
}

function getAvailableThemes() {
    return Object.keys(_themes);
}

// Color palette helper - returns color object from token
function getColor(name) {
    return getToken(name);
}

// Spacing helper - returns numeric value in pixels
function getSpacing(name) {
    var value = getToken(name);
    if (typeof value === "string" && value.indexOf("px") !== -1) {
        return parseInt(value);
    }
    return 0;
}

// Size helper - returns numeric value in pixels
function getSize(name) {
    var value = getToken(name);
    if (typeof value === "string" && value.indexOf("px") !== -1) {
        return parseInt(value);
    }
    return 0;
}

// Font size helper - returns numeric value in pixels
function getFontSize(name) {
    var value = getToken(name);
    if (typeof value === "string" && value.indexOf("px") !== -1) {
        return parseInt(value);
    }
    return 12;
}

// Border radius helper - returns numeric value or percentage
function getRadius(name) {
    return getToken(name);
}

// Shadow helper
function getShadow(name) {
    return getToken(name);
}
