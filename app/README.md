# App

Two versions. Start with the simple one.

## app_simple.py — Day 1

One button per check. You click it, you see the result.

```
python app_simple.py
```

### How to add a new check

**Step 1.** Write a function in `src/ifc_checker.py`. It takes a model, returns a list of strings:

```python
def check_window_height(model, min_height_mm=1200):
    results = []
    for window in model.by_type("IfcWindow"):
        height_m = window.OverallHeight
        height_mm = round(height_m * 1000) if height_m else None
        if height_mm and height_mm >= min_height_mm:
            results.append(f"[PASS] {window.Name}: {height_mm} mm")
        else:
            results.append(f"[FAIL] {window.Name}: {height_mm} mm")
    return results
```

**Step 2.** Open `app_simple.py`. Import your function (line 10) and add it to the CHECKS list (line 14):

```python
from ifc_checker import check_door_width, check_window_height

CHECKS = [
    ("Check Door Width", check_door_width),
    ("Check Window Height", check_window_height),
]
```

**Step 3.** Restart the app. Your new button appears. Click it.

## app.py — Day 2+

3D viewer. Failed elements show in red. Don't use this until we agree on a shared data format (Tuesday).

```
python app.py
```

## Files

```
app/
├── app_simple.py       ← Day 1: one button per check
├── app.py              ← Day 2+: 3D viewer (don't touch yet)
└── src/
    ├── ifc_checker.py  ← YOUR CODE GOES HERE
    └── ifc_visualizer.py  ← don't touch
```
