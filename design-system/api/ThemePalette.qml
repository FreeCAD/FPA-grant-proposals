// ThemePalette.qml - QML Theme Palette Singleton
// Provides design tokens as Qt.application properties for easy QML access

pragma Singleton
import QtQuick 2.15

QtObject {
    property string currentTheme: "dark"

    // Color palette
    property color colorBackgroundPrimary: "#1e1e1e"
    property color colorBackgroundSecondary: "#252526"
    property color colorBackgroundTertiary: "#2d2d30"
    property color colorSurface: "#3c3c3c"
    property color colorBorder: "#3e3e42"
    property color colorBorderStrong: "#007acc"
    property color colorTextPrimary: "#cccccc"
    property color colorTextSecondary: "#9d9d9d"
    property color colorTextDisabled: "#5a5a5a"
    property color colorAccentPrimary: "#007acc"
    property color colorAccentHover: "#1e8ad2"
    property color colorAccentActive: "#005a9e"
    property color colorSuccess: "#4ec9b0"
    property color colorWarning: "#dcdcaa"
    property color colorError: "#f14c4c"
    property color colorInfo: "#569cd6"

    // Typography
    property string fontFamilyPrimary: "Segoe UI"
    property string fontFamilyMono: "Cascadia Code"
    property real fontSizeXs: 10
    property real fontSizeSm: 11
    property real fontSizeBase: 12
    property real fontSizeLg: 13
    property real fontSizeXl: 14
    property real fontSizeXxl: 16
    property int fontWeightNormal: 400
    property int fontWeightMedium: 500
    property int fontWeightBold: 600

    // Spacing
    property real spacingXs: 2
    property real spacingSm: 4
    property real spacingMd: 6
    property real spacingLg: 8
    property real spacingXl: 12
    property real spacingXxl: 16
    property real spacingXxxl: 24

    // Sizing
    property real buttonHeight: 24
    property real buttonHeightSm: 20
    property real buttonHeightLg: 28
    property real inputHeight: 24
    property real iconSizeSm: 16
    property real iconSizeMd: 20
    property real iconSizeLg: 24
    property real toolbarHeight: 32
    property real menubarHeight: 26
    property real statusbarHeight: 24
    property real panelWidth: 250
    property real panelMinWidth: 180
    property real panelMaxWidth: 400

    // Border radius
    property real radiusSm: 2
    property real radiusMd: 3
    property real radiusLg: 4

    function setTheme(theme) {
        currentTheme = theme
        if (theme === "light") {
            colorBackgroundPrimary = "#ffffff"
            colorBackgroundSecondary = "#f5f5f5"
            colorBackgroundTertiary = "#e8e8e8"
            colorSurface = "#dcdcdc"
            colorBorder = "#c0c0c0"
            colorBorderStrong = "#0078d4"
            colorTextPrimary = "#1e1e1e"
            colorTextSecondary = "#6e6e6e"
            colorTextDisabled = "#a0a0a0"
            colorAccentPrimary = "#0078d4"
            colorAccentHover = "#106ebe"
            colorAccentActive = "#005a9e"
            colorSuccess = "#107c10"
            colorWarning = "#ca5010"
            colorError = "#d13438"
            colorInfo = "#0078d4"
        } else {
            colorBackgroundPrimary = "#1e1e1e"
            colorBackgroundSecondary = "#252526"
            colorBackgroundTertiary = "#2d2d30"
            colorSurface = "#3c3c3c"
            colorBorder = "#3e3e42"
            colorBorderStrong = "#007acc"
            colorTextPrimary = "#cccccc"
            colorTextSecondary = "#9d9d9d"
            colorTextDisabled = "#5a5a5a"
            colorAccentPrimary = "#007acc"
            colorAccentHover = "#1e8ad2"
            colorAccentActive = "#005a9e"
            colorSuccess = "#4ec9b0"
            colorWarning = "#dcdcaa"
            colorError = "#f14c4c"
            colorInfo = "#569cd6"
        }
    }
}
