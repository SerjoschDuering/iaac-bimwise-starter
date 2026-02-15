# IFC Compliance Checker App

## Structure

```
04_app/
├── app_simple.py          # Day 1: Simple text results
├── app.py                 # Day 2+: 3D visualization with failures highlighted
└── src/
    ├── ifc_checker.py     # ✏️ ADD YOUR CHECKS HERE
    ├── ifc_visualizer.py  # 🔒 3D export (don't modify)
    └── visualize.py       # 🔒 Notebook viz (don't modify)
```

## Usage

### Day 1 Afternoon - Simple Version
```bash
python app_simple.py
```
- Upload IFC file
- See pass/fail as text list
- **Your job:** Add checks to `src/ifc_checker.py`

### Day 2+ - Full Version with 3D
```bash
python app.py
```
- Upload IFC file
- See failures highlighted in RED in 3D model
- Passed elements are semi-transparent gray

## Adding Your Own Checks

Edit `src/ifc_checker.py` → add functions like:

```python
def check_stair_width(model, min_width=1.2):
    results = []
    stairs = model.by_type("IfcStair")

    for stair in stairs:
        # Extract width property
        width = get_property_value(stair, "Qto_StairBaseQuantities", "Width")

        # Build result
        results.append({
            "element_id": stair.GlobalId,
            "element_type": "IfcStair",
            "element_name": stair.Name or f"Stair #{stair.id()}",
            "rule": "Stair Width",
            "requirement": f">= {min_width} m",
            "actual": f"{width:.2f} m" if width else "N/A",
            "passed": width >= min_width if width else None,
        })

    return results
```

Then add to `run_all_checks()`:
```python
all_results.extend(check_stair_width(model))
```

## Output Schema (MANDATORY)

Every check function must return a list of dicts with:
- `element_id`: IFC GlobalId (str)
- `element_type`: e.g., "IfcDoor" (str)
- `element_name`: Human-readable name (str)
- `rule`: What you're checking (str)
- `requirement`: What it should be (str)
- `actual`: What it is (str)
- `passed`: True/False/None (bool or None)

Failed elements (`passed: False`) are highlighted RED in the 3D viewer.
