"""IFC Compliance Checker - ADD YOUR CHECKS HERE"""

import ifcopenshell


def run_all_checks(ifc_path):
    """Load IFC and run checks."""
    model = ifcopenshell.open(ifc_path)

    results = []
    # TODO: Add your check functions here

    # Calculate summary
    passed = sum(1 for r in results if r.get("passed") is True)
    failed = sum(1 for r in results if r.get("passed") is False)
    unknown = len(results) - passed - failed

    failed_ids = {r["element_id"] for r in results if r.get("passed") is False}

    return {
        "results": results,
        "summary": {"total": len(results), "passed": passed, "failed": failed, "unknown": unknown},
        "failed_ids": failed_ids,
        "model": model,
    }
