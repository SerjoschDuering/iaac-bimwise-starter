# IAAC AI Week - Building Compliance Platform

**Welcome to your startup!** 🚀

You're building an automated platform that checks building models (IFC files) against regulations. By Friday, you'll pitch this product to investors.

---

## 📁 Project Structure

```
student-template/
│
├── 00_data/                      # Your data assets
│   ├── ifc_models/              # Building models to test with
│   │   └── 01_Duplex_Apartment.ifc
│   └── regulations/             # Spanish building codes (9 excerpts)
│       └── sample_regulations_es.md
│
├── exercises/                    # 📓 Jupyter notebooks
│   └── 01_explore_ifc.ipynb     # Learn IFC structure
│
├── app/                          # 🚀 Your product
│   ├── app_simple.py            # Simple version (text results)
│   ├── app.py                   # Full version (3D viz)
│   ├── README.md                # How to add checks
│   └── src/                     # ✏️ Your code goes here
│       ├── ifc_checker.py       # ADD YOUR CHECKS HERE
│       └── ifc_visualizer.py    # (don't modify)
│
├── README.md                     # ← You are here
└── requirements.txt              # Python dependencies
```

---

## 🎯 App Architecture

### Day 1 Afternoon: Simple Version
```
┌─────────────────────────────────────┐
│   IFC Compliance Checker            │
├─────────────────────────────────────┤
│                                     │
│  [Upload IFC File] [Run Checks]    │
│                                     │
│  ╔═══════════════════════════════╗ │
│  ║ Summary                       ║ │
│  ║ ✅ Passed: 12                 ║ │
│  ║ ❌ Failed: 3                  ║ │
│  ║ ⚠️  Unknown: 1                ║ │
│  ║                               ║ │
│  ║ Details                       ║ │
│  ║ ✅ Door Width - Door #1: 900mm║ │
│  ║ ❌ Door Width - Door #2: 700mm║ │
│  ║ ✅ Room Area - Living: 25 m²  ║ │
│  ║ ❌ Room Area - Bath: 7.5 m²   ║ │
│  ╚═══════════════════════════════╝ │
└─────────────────────────────────────┘

FILE: app_simple.py
RUN:  python app_simple.py
```

### Day 2+: Full Version with 3D
```
┌──────────────────────────────────────────────────────────┐
│   IFC Compliance Checker                                 │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────────────┐  ┌────────────────────────┐  │
│  │   3D Model Viewer    │  │  ╔══════════════════╗  │  │
│  │                      │  │  ║ ✅ Passed: 12    ║  │  │
│  │       ┌─────┐        │  │  ║ ❌ Failed: 3     ║  │  │
│  │      ╱│░░░░░│╲       │  │  ║ ⚠️  Unknown: 1   ║  │  │
│  │     ╱ │░RED░│ ╲      │  │  ╚══════════════════╝  │  │
│  │    │  └─────┘  │     │  │                        │  │
│  │    │           │     │  │  ┌──────────────────┐ │  │
│  │    │  ┌─────┐  │     │  │  │✅ Door Width     │ │  │
│  │    │  │GRAY │  │     │  │  │  Door #1: 900mm  │ │  │
│  │     ╲ └─────┘ ╱      │  │  ├──────────────────┤ │  │
│  │      ╲       ╱       │  │  │❌ Door Width     │ │  │
│  │       ───────        │  │  │  Door #2: 700mm  │ │  │
│  │                      │  │  ├──────────────────┤ │  │
│  │  RED = Failed ❌     │  │  │✅ Room Area      │ │  │
│  │  GRAY = Passed ✅    │  │  │  Living: 25 m²   │ │  │
│  └──────────────────────┘  └────────────────────────┘  │
│                                                          │
│  [Upload IFC] [Run Checks] [Load Demo]                  │
└──────────────────────────────────────────────────────────┘

FILE: app.py
RUN:  python app.py
```

**Key Difference:** Failed elements are **highlighted in RED** in the 3D model!

---

## 🚀 Quick Start

### 1. Setup (5 minutes)

**Requirements:**
- Python 3.10+
- VS Code, Cursor, or Jupyter

**Install:**
```bash
# Clone repo
git clone <repo-url>
cd student-template

# Create environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Test
python -c "import ifcopenshell, gradio; print('✅ Ready!')"
```

### 2. Explore IFC (Monday Morning)

```bash
jupyter notebook exercises/01_explore_ifc.ipynb
```

**You'll learn:**
- What's inside an IFC file (doors, walls, spaces)
- How to extract properties (widths, areas, heights)
- See the building in 3D

### 3. Build Your First Check (Monday Afternoon)

```bash
cd app
python app_simple.py
```

**Then add your check to `src/ifc_checker.py`:**

```python
def check_stair_width(model, min_width=1.2):
    """Check stairs are wide enough."""
    results = []
    stairs = model.by_type("IfcStair")

    for stair in stairs:
        width = get_property_value(stair, "Qto_StairBaseQuantities", "Width")

        results.append({
            "element_id": stair.GlobalId,
            "element_type": "IfcStair",
            "element_name": stair.Name or "Unnamed Stair",
            "rule": "Stair Width",
            "requirement": f">= {min_width} m",
            "actual": f"{width:.2f} m" if width else "N/A",
            "passed": width >= min_width if width else None,
        })

    return results
```

**Add to `run_all_checks()`:**
```python
all_results.extend(check_stair_width(model))
```

Refresh the app → your check runs! ✅

---

## 📊 Data Flow

```
┌─────────────┐
│ IFC File    │  (Building model uploaded by user)
│ .ifc        │
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────────┐
│  src/ifc_checker.py                  │
│  ────────────────────                │
│  • Load IFC with ifcopenshell        │
│  • Run all check functions           │
│  • Return list of results            │
│    [{passed: True/False, ...}, ...]  │
└──────┬───────────────────────────────┘
       │
       ├──────────────┬─────────────────┐
       ▼              ▼                 ▼
┌─────────────┐ ┌─────────────┐ ┌──────────────┐
│ app_simple  │ │   app.py    │ │ (Your agent) │
│             │ │             │ │              │
│ Text list   │ │ 3D viz with │ │ Tuesday+     │
│ of results  │ │ red fails   │ │              │
└─────────────┘ └─────────────┘ └──────────────┘
```

---

## 🗓️ Your Week

### **Monday: Make It Work**
- 📓 Notebook: Understand IFC files
- 🔧 Build: Write compliance checks
- 👀 See: Results in simple app
- 🎨 Upgrade: 3D visualization

### **Tuesday: Make It Talk**
- 🤖 Add AI agent orchestration
- 📋 Lock shared data schema
- 🔄 Iterate on checks

### **Wednesday: Make It Connect**
- ☁️ Deploy to HuggingFace Spaces
- 🔍 Add RAG (agent reads regulations)
- 🏗️ Platform architecture

### **Thursday: Make It Real**
- 🔗 Integration sprint
- ✨ Polish the product
- 🎤 Pitch rehearsal

### **Friday: Present**
- 🎯 Demo to "investors"
- 🚀 Show your product

---

## 🎓 What You Modify

### ✏️ YOU WRITE CODE HERE:
- `app/src/ifc_checker.py` ← Add check functions

### 🔒 DON'T MODIFY (black boxes):
- `app.py`, `app_simple.py` ← Gradio interfaces
- `src/ifc_visualizer.py` ← 3D export

**Clean separation of concerns!** You focus on compliance logic.

---

## 🆘 Common Issues

**"Property not found"**
→ IFC files are vendor-specific. Use fallback patterns:
```python
width = get_property_value(door, "Qto_DoorBaseQuantities", "Width")
if width is None:
    width = get_property_value(door, "PSet_DoorCommon", "Width")
if width is None:
    width = door.OverallWidth  # Try direct attribute
```

**"Import error"**
→ Make sure virtual environment is activated:
```bash
source venv/bin/activate
which python  # Should show venv/bin/python
```

**"Gradio won't start"**
→ Check port 7860 is free:
```bash
lsof -ti:7860 | xargs kill  # Kill existing Gradio
python app_simple.py
```

---

## 📚 Resources

- **IFC Spec:** https://standards.buildingsmart.org/IFC/
- **ifcopenshell:** http://ifcopenshell.org/
- **Gradio:** https://gradio.app/docs/
- **Online IFC Viewer:** https://ifcviewer.com (upload & explore models)

---

## 🏢 Company Simulation

**You ARE a startup.** Instructors = board. Experienced students = tech leads ("Captains").

**Board meetings** = end of each day. New requirements drop. Teams adapt.

**Miro** = shared workspace. Document your tools, schemas, architecture there.

---

**Ready? Start with:** `jupyter notebook 01_monday/01_exercise/01_explore_ifc.ipynb` 🚀
