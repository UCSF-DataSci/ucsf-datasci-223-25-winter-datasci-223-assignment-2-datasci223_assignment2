#!/usr/bin/env python3
"""
Basic tests for patient_data_cleaner.py

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
    script_path = Path(__file__).parent.parent.parent / "1_patient_data_cleaner.py"
    result = subprocess.run(["python", str(script_path)], capture_output=True, text=True)
    assert result.returncode == 0

def test_bug_markers_present():
    """Test that all bug markers are present in the code."""
    script_path = Path(__file__).parent.parent.parent / "1_patient_data_cleaner.py"
    with open(script_path) as f:
        content = f.read()
    
    # Check for bug markers
    assert "# BUG: No error handling for file not found" in content
    assert "# BUG: Typo in key 'nage' instead of 'name'" in content
    assert "# BUG: Wrong method name (fill_na vs fillna)" in content
    assert "# BUG: Wrong method name (drop_duplcates vs drop_duplicates)" in content
    assert "# BUG: Wrong comparison operator (= vs ==)" in content
    assert "# BUG: Logic error - keeps patients under 18 instead of filtering them out" in content
    assert "# BUG: Missing return statement for empty list" in content
    assert "# BUG: No error handling for load_patient_data failure" in content
    assert "# BUG: No check if cleaned_patients is None" in content
    assert "# BUG: Using 'name' key but we changed it to 'nage'" in content

def test_basic_input():
    """Test that the script can handle basic input."""
    script_path = Path(__file__).parent.parent.parent / "1_patient_data_cleaner.py"
    
    # Create a temporary input file
    input_data = [
        {"name": "test patient", "age": "25", "gender": "male", "diagnosis": "test"}
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