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

**Step 2.** Open `app_simple.py`. Import your function (line 10):

```python
from ifc_checker import check_door_width, check_window_height
```

**Step 3.** Add two lines for your button (line 33):

```python
btn_window = gr.Button("Check Window Height")
btn_window.click(fn=lambda f: run_check(check_window_height, f), inputs=[ifc_input], outputs=[output])
```

**Step 4.** Restart the app. Your new button appears. Click it.

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
