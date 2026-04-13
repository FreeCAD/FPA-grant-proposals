#!/usr/bin/env python3
"""
FreeCAD Stylesheet Build Script

Compiles SCSS stylesheets to QSS using qtsass.
"""

import argparse
import os
import sys

try:
    import qtsass
except ImportError:
    print("Error: qtsass is required. Install with: pip install qtsass")
    sys.exit(1)

STYLES_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(STYLES_DIR, "output")
THEMES_DIR = os.path.join(STYLES_DIR, "themes")


def compile_scss(input_file, output_file, indent=4):
    """Compile a SCSS file to QSS."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    print(f"Compiling: {input_file} -> {output_file}")
    
    qtsass.compile(
        inputfile=input_file,
        outputfile=output_file,
        indent=indent,
        compress=False
    )
    
    print(f"  Done!")


def compile_all():
    """Compile all SCSS files to QSS."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    main_scss = os.path.join(STYLES_DIR, "main.scss")
    main_qss = os.path.join(OUTPUT_DIR, "main.qss")
    
    compile_scss(main_scss, main_qss)
    
    for theme_file in os.listdir(THEMES_DIR):
        if theme_file.endswith(".scss"):
            theme_name = theme_file.replace(".scss", "")
            scss_path = os.path.join(THEMES_DIR, theme_file)
            qss_path = os.path.join(OUTPUT_DIR, f"{theme_name}.qss")
            compile_scss(scss_path, qss_path)
    
    print("\nAll stylesheets compiled successfully!")


def compile_theme(theme_name):
    """Compile a specific theme."""
    scss_path = os.path.join(THEMES_DIR, f"{theme_name}.scss")
    qss_path = os.path.join(OUTPUT_DIR, f"{theme_name}.qss")
    
    if not os.path.exists(scss_path):
        print(f"Error: Theme '{theme_name}' not found at {scss_path}")
        sys.exit(1)
    
    compile_scss(scss_path, qss_path)
    print(f"Theme '{theme_name}' compiled successfully!")


def main():
    parser = argparse.ArgumentParser(description="Build FreeCAD QSS stylesheets")
    parser.add_argument("--all", action="store_true", help="Compile all themes")
    parser.add_argument("--theme", type=str, help="Compile specific theme")
    parser.add_argument("--watch", action="store_true", help="Watch mode for development")
    
    args = parser.parse_args()
    
    if args.all:
        compile_all()
    elif args.theme:
        compile_theme(args.theme)
    else:
        parser.print_help()
        print("\nExample: python build.py --all")


if __name__ == "__main__":
    main()
