"""IFC Compliance Checker — one button per check."""

import sys
from pathlib import Path

import gradio as gr
import ifcopenshell

sys.path.insert(0, str(Path(__file__).parent / "src"))
from ifc_checker import check_door_width  # add your imports here


# ─── Register your checks here: (button label, function) ──────
CHECKS = [
    ("Check Door Width", check_door_width),
    # ("Check Room Area", check_room_area),
]


def make_runner(check_fn):
    def run(ifc_file):
        if ifc_file is None:
            return "Upload an IFC file first."
        path = ifc_file if isinstance(ifc_file, str) else ifc_file.name
        model = ifcopenshell.open(path)
        results = check_fn(model)
        return "\n".join(results) if results else "No elements found."
    return run


with gr.Blocks(title="IFC Compliance Checker") as app:
    gr.Markdown("# IFC Compliance Checker")
    gr.Markdown("Upload a building model. Click a check to run it.")

    ifc_input = gr.File(label="Upload IFC File", file_types=[".ifc"])
    output = gr.Textbox(label="Results", lines=15)

    with gr.Row():
        for label, fn in CHECKS:
            btn = gr.Button(label)
            btn.click(fn=make_runner(fn), inputs=[ifc_input], outputs=[output])

if __name__ == "__main__":
    app.launch(show_api=False)
