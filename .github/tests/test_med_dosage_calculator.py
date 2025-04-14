#!/usr/bin/env python3
"""
Basic tests for med_dosage_calculator.py

This script tests:
1. That the script runs without errors
2. That all bug markers are present in the code
3. That the script can handle basic input
"""

import os
import pytest
import subprocess
from pathlib import Path

def test_script_runs():
    """Test that the script runs without errors."""
    script_path = Path(__file__).parent.parent.parent / "2_med_dosage_calculator.py"
    result = subprocess.run(["python", str(script_path)], capture_output=True, text=True)
    assert result.returncode == 0

def test_bug_markers_present():
    """Test that all bug markers are present in the code."""
    script_path = Path(__file__).parent.parent.parent / "2_med_dosage_calculator.py"
    with open(script_path) as f:
        content = f.read()
    
    # Check for bug markers
    assert "# BUG: Missing commas between list items" in content
    assert "# BUG: No error handling for file not found" in content
    assert "# BUG: No check if 'weight' key exists" in content
    assert "# BUG: No check if 'medication' key exists" in content
    assert "# BUG: Adding 's' to medication name, which doesn't match DOSAGE_FACTORS keys" in content
    assert "# BUG: Using addition instead of multiplication" in content
    assert "# BUG: No check if 'is_first_dose' key exists" in content
    assert "# BUG: Incorrect condition - should check if medication is in LOADING_DOSE_MEDICATIONS" in content
    assert "# BUG: Using addition instead of multiplication for loading dose" in content
    assert "# BUG: Typos in medication names" in content
    assert "# BUG: No check if 'final_dosage' key exists" in content
    assert "# BUG: No error handling for load_patient_data failure" in content
    assert "# BUG: No check if required keys exist" in content

def test_basic_input():
    """Test that the script can handle basic input."""
    script_path = Path(__file__).parent.parent.parent / "2_med_dosage_calculator.py"
    
    # Create a temporary input file
    input_data = [
        {
            "name": "test patient",
            "weight": 70.0,
            "medication": "epinephrine",
            "condition": "test",
            "is_first_dose": False,
            "allergies": []
        }
    ]
    
    with open("test_input.json", "w") as f:
        import json
        json.dump(input_data, f)
    
    try:
        result = subprocess.run(
            ["python", str(script_path), "test_input.json"],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
    finally:
        # Cleanup
        if os.path.exists("test_input.json"):
            os.remove("test_input.json")

if __name__ == "__main__":
    pytest.main(["-v", __file__])