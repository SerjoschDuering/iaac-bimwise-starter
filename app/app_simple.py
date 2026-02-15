"""
Minimal IFC Compliance Checker (Day 1)

Keep this file simple:
- upload an IFC file
- run the checks
- show a short text report
"""

import sys
from pathlib import Path

import gradio as gr

# Allow importing from `app/src/` without extra packaging.
sys.path.insert(0, str(Path(__file__).parent / "src"))
from ifc_checker import run_all_checks

def check_ifc(ifc_file):
    """Run checks on the uploaded IFC and return plain text."""
    if ifc_file is None:
        return "Upload an IFC file to start."

    # Gradio may give a string path or a file object with `.name`.
    ifc_path = ifc_file if isinstance(ifc_file, str) else ifc_file.name

    results = run_all_checks(ifc_path)

    summary = results["summary"]
    output = (
        f"Summary\n"
        f"Passed: {summary['passed']}\n"
        f"Failed: {summary['failed']}\n"
        f"Unknown: {summary['unknown']}\n"
        f"\n"
        f"Details\n"
    )

    for r in results["results"]:
        status = "PASS" if r["passed"] is True else "FAIL" if r["passed"] is False else "UNK"
        output += f"\n[{status}] {r['rule']} - {r['element_name']}: {r['actual']}"

    return output


with gr.Blocks(title="IFC Compliance Checker") as app:
    gr.Markdown("# IFC Compliance Checker")
    gr.Markdown("Upload a building model and see which elements pass/fail regulations.")

    with gr.Row():
        ifc_input = gr.File(label="Upload IFC File", file_types=[".ifc"])
        run_btn = gr.Button("Run Checks", variant="primary")

    results_output = gr.Textbox(label="Results", lines=18)
    run_btn.click(fn=check_ifc, inputs=[ifc_input], outputs=[results_output])

if __name__ == "__main__":
    app.launch(show_api=False)
