# src/Mod/Sketcher/App/SketcherGeometry.py

def add_default_constraints(sketch):
    # Fetch all lines in the sketch
    lines = sketch.get_lines()
    
    # Iterate over each line and add constraints conditionally
    for line in lines:
        # Check if the line is horizontal
        if line.is_horizontal():
            sketch.add_constraint('Horizontal', line)
        
        # Check if the line is vertical
        if line.is_vertical():
            sketch.add_constraint('Vertical', line)

def fix_broken_constraints(sketch):
    # Fetch all constraints in the sketch
    constraints = sketch.get_constraints()
    
    # Iterate over each constraint and attempt to fix it
    for constraint in constraints:
        if constraint.is_broken():
            # Save user-defined constraints
            user_defined_constraints = sketch.get_user_defined_constraints()
            
            # Delete and re-add the constraint
            sketch.delete_constraint(constraint)
            sketch.add_constraint(constraint.type, constraint.geometry)
            
            # Restore user-defined constraints
            for user_constraint in user_defined_constraints:
                sketch.add_constraint(user_constraint.type, user_constraint.geometry)

def standardize_sketch_properties(sketch):
    # Set default display properties
    sketch.set_display_mode('Flat Lines')
    sketch.show_support(True)
    sketch.show_construction(True)
    sketch.show_internal_geometry(True)