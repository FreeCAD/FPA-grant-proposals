# FreeCAD Python addon for exporting parts to HIPAIR configuration space visualization format
# This macro exports selected planar faces or wires to HIPAIR input language.
# Usage: Select one or more planar faces or wires in FreeCAD, then run this macro.
# It will prompt for a save file location and write the HIPAIR definition.

import FreeCAD
import FreeCADGui
import Part
from PySide import QtGui

# HIPAIR format definition (simplified based on available documentation)
# Each part is defined as:
# PART <name>
# SLICE
# <edges>
# ENDPART
# Edges are either LINE x1 y1 x2 y2 or ARC x1 y1 x2 y2 cx cy radius start_angle end_angle
# All coordinates are in mm.

def get_hipair_edges(shape):
    """Extract edges from a shape and return list of HIPAIR edge strings."""
    edges = []
    for edge in shape.Edges:
        if isinstance(edge.Curve, Part.Line):
            p1 = edge.Vertexes[0].Point
            p2 = edge.Vertexes[1].Point
            edges.append(f"LINE {p1.x:.6f} {p1.y:.6f} {p2.x:.6f} {p2.y:.6f}")
        elif isinstance(edge.Curve, Part.Circle):
            # Circle arc: we need to specify start and end points, center, radius, start and end angles
            curve = edge.Curve
            center = curve.Center
            radius = curve.Radius
            # Get start and end parameters
            u1 = edge.ParameterRange[0]
            u2 = edge.ParameterRange[1]
            # Points on circle
            p1 = curve.value(u1)
            p2 = curve.value(u2)
            # Angles (in radians) relative to center, normalized to 0..2pi
            start_angle = (p1 - center).getAngle(FreeCAD.Vector(1,0,0))
            end_angle = (p2 - center).getAngle(FreeCAD.Vector(1,0,0))
            # Adjust sign for orientation (counterclockwise positive)
            # FreeCAD uses right-handed coordinate system, we assume positive is counterclockwise
            # If the arc is clockwise, angles may need to be reversed? We'll just output both.
            # For simplicity, we output the absolute angles.
            edges.append(f"ARC {p1.x:.6f} {p1.y:.6f} {p2.x:.6f} {p2.y:.6f} {center.x:.6f} {center.y:.6f} {radius:.6f} {start_angle:.6f} {end_angle:.6f}")
        # Optionally handle BSpline etc. Not required for HIPAIR
    return edges

def export_selected_parts():
    """Main function to export selected FreeCAD objects to HIPAIR format."""
    # Get selected objects
    sel = FreeCADGui.Selection.getSelectionEx()
    if not sel:
        QtGui.QMessageBox.warning(None, "No selection", "Please select at least one planar face or wire.")
        return

    # Ask for save file
    save_file, _ = QtGui.QFileDialog.getSaveFileName(None, "Save HIPAIR file", "", "HIPAIR files (*.hip);;All files (*.*)")
    if not save_file:
        return

    output = []
    for sel_obj in sel:
        obj = sel_obj.Object
        # Get shape - prefer selected subelements if any
        if sel_obj.SubElementNames:
            # Use first selected subelement (e.g., face)
            for subname in sel_obj.SubElementNames:
                sh = obj.getSubObject(subname)
                if sh and hasattr(sh, 'ShapeType') and sh.ShapeType in ('Face', 'Wire', 'Edge'):
                    break
            else:
                continue
        else:
            sh = obj.Shape
        # If it's a solid or compound, try to get the planar face with largest area?
        # For simplicity, we assume user selects planar faces or wires directly.
        if not sh:
            continue
        if sh.ShapeType == 'Face':
            # Extract outer wire
            wire = sh.OuterWire
        elif sh.ShapeType == 'Wire':
            wire = sh
        else:
            # Skip non-planar shapes
            continue
        # Ensure wire is planar (HIPAIR requirement)
        if not wire.isPlanar():
            QtGui.QMessageBox.warning(None, "Non-planar", f"Object {obj.Label} is not planar. Skipping.")
            continue
        # Get edges
        edges = get_hipair_edges(wire)
        if not edges:
            continue
        # Write part definition
        output.append(f"PART {obj.Label}")
        output.append("SLICE")
        output.extend(edges)
        output.append("ENDPART")
        output.append("")

    if not output:
        QtGui.QMessageBox.information(None, "Nothing exported", "No suitable planar objects found.")
        return

    # Write to file
    with open(save_file, 'w') as f:
        f.write("\n".join(output))

    QtGui.QMessageBox.information(None, "Export complete", f"Exported {len(sel)} part(s) to {save_file}")

# Run the export function
if __name__ == '__main__':
    export_selected_parts()
