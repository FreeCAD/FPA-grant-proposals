# HIPAIR Exporter for FreeCAD

This addon exports parts and assemblies from FreeCAD to the HIPAIR input format.
HIPAIR is an open-source configuration space visualization tool.

## Features
- Export FreeCAD shapes (faces, wires, edges) to HIPAIR format.
- Handles line segments and arcs.
- Can export all objects in document or selected objects.

## Usage
1. Open FreeCAD.
2. Run the macro `hipair_exporter.py`.
3. The exporter will generate a `.hipair` file in the same directory as the document.

Alternatively, use the Python console:
```python
import hipair_exporter
hipair_exporter.export_to_hipair("output.hipair")
# or export selected:
hipair_exporter.export_selected_to_hipair("output.hipair")
```

## HIPAIR Format
Each part is defined with a name, then a slice containing lines and arcs.
Lines: `LINE x1 y1 x2 y2`
Arcs: `ARC xc yc radius startangle endangle`

Parts are separated by `PART` and `ENDPART`.

## Limitations
- Only planar geometry in XY plane is considered (Z coordinates ignored).
- Only lines and arcs are supported (other curves are skipped).
- FreeCAD assemblies are not recursively traversed (all objects are flat).
