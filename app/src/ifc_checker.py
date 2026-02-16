"""IFC Compliance Checker — YOUR CODE GOES HERE"""

import ifcopenshell


# ─── Write your check functions below ──────────────────────────
# Each function takes a model, returns a list of strings.
# One string per element you checked.

def check_door_width(model, min_width_mm=800):
    """Check that all doors are at least 800mm wide."""
    results = []
    for door in model.by_type("IfcDoor"):
        width_m = door.OverallWidth  # IFC stores in meters
        width_mm = round(width_m * 1000) if width_m else None
        if width_mm is None:
            results.append(f"[???] {door.Name}: width unknown")
        elif width_mm >= min_width_mm:
            results.append(f"[PASS] {door.Name}: {width_mm} mm (min {min_width_mm} mm)")
        else:
            results.append(f"[FAIL] {door.Name}: {width_mm} mm (min {min_width_mm} mm)")
    return results


# def check_room_area(model):
#     """Your next check..."""
#     results = []
#     for space in model.by_type("IfcSpace"):
#         ...
#     return results
