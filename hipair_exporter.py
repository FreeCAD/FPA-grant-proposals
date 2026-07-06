# FreeCAD Python addon to export assemblies to HIPAIR format
# Usage: run as macro or import in FreeCAD Python console

import FreeCAD as App
import Part


def export_to_hipair(filename, doc=None):
    """Export the active document or given document to HIPAIR file."""
    if doc is None:
        doc = App.ActiveDocument
    if doc is None:
        print("No active document.")
        return

    with open(filename, 'w') as f:
        f.write("# HIPAIR input file generated from FreeCAD\n")
        for obj in doc.Objects:
            if hasattr(obj, 'Shape') and obj.Shape:
                shape = obj.Shape
                if shape.ShapeType in ['Face', 'Wire', 'Edge']:
                    # Treat as a single slice part
                    part_name = obj.Label.replace(' ', '_')
                    f.write(f"PART {part_name}\n")
                    f.write("BEGIN_SLICE\n")
                    # Collect all edges
                    edges = []
                    if shape.ShapeType == 'Edge':
                        edges = [shape]
                    elif shape.ShapeType == 'Wire':
                        edges = shape.Edges
                    elif shape.ShapeType == 'Face':
                        edges = shape.Wires[0].Edges if shape.Wires else []
                    for edge in edges:
                        write_edge(f, edge)
                    f.write("END_SLICE\n")
                    f.write("ENDPART\n")


def write_edge(f, edge):
    """Write a single edge to HIPAIR format."""
    curve = edge.Curve
    if isinstance(curve, Part.Line):
        p1 = edge.Vertexes[0].Point
        p2 = edge.Vertexes[1].Point
        # Assume planar in XY, ignore Z
        f.write(f"LINE {p1.x:.6f} {p1.y:.6f} {p2.x:.6f} {p2.y:.6f}\n")
    elif isinstance(curve, Part.Circle) or isinstance(curve, Part.ArcOfCircle):
        # Get parameters from edge
        # For arc, we need start and end angles
        if isinstance(curve, Part.Circle):
            # Full circle: we treat as arc with 0 to 360
            startangle = 0.0
            endangle = 360.0
        else:
            # ArcOfCircle
            startangle = curve.FirstParameter
            endangle = curve.LastParameter
            # Convert to degrees if curve is parameterized in rad? FreeCAD uses mm for length, rad for angle
            # But HIPAIR likely uses degrees; we convert if needed.
            # We'll assume degrees, so convert rad to degrees
            startangle = startangle * 180.0 / 3.141592653589793
            endangle = endangle * 180.0 / 3.141592653589793
        center = curve.Center
        radius = curve.Radius
        f.write(f"ARC {center.x:.6f} {center.y:.6f} {radius:.6f} {startangle:.6f} {endangle:.6f}\n")
    else:
        # Unsupported curve type
        print(f"Unsupported curve type: {curve}")


def export_selected_to_hipair(filename):
    """Export selected objects to HIPAIR."""
    doc = App.ActiveDocument
    if not doc:
        return
    sel = Gui.Selection.getSelection()
    if not sel:
        print("No selection.")
        return
    with open(filename, 'w') as f:
        f.write("# HIPAIR input file generated from FreeCAD\n")
        for obj in sel:
            if hasattr(obj, 'Shape') and obj.Shape:
                shape = obj.Shape
                # similar logic as above
                part_name = obj.Label.replace(' ', '_')
                f.write(f"PART {part_name}\n")
                f.write("BEGIN_SLICE\n")
                edges = []
                if shape.ShapeType == 'Edge':
                    edges = [shape]
                elif shape.ShapeType == 'Wire':
                    edges = shape.Edges
                elif shape.ShapeType == 'Face':
                    edges = shape.Wires[0].Edges if shape.Wires else []
                for edge in edges:
                    write_edge(f, edge)
                f.write("END_SLICE\n")
                f.write("ENDPART\n")

# Simple macro entry point
def run():
    doc = App.ActiveDocument
    if not doc:
        print("No active document.")
        return
    filename = doc.FileName.replace('.FCStd', '.hipair')
    if not filename or filename == doc.FileName:
        filename = doc.Name + ".hipair"
    export_to_hipair(filename, doc)
    print(f"Exported to {filename}")

if __name__ == '__main__':
    run()
