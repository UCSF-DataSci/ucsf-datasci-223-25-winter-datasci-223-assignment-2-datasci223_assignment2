#!/usr/bin/env python3
"""
Basic test for cohort_analysis.py

This script tests:
1. That the script runs without errors
"""

import os
import pytest
import subprocess
from pathlib import Path

def test_script_runs():
    """Test that the script runs without errors."""
    script_path = Path(__file__).parent.parent.parent / "3_cohort_analysis.py"
    result = subprocess.run(["python", str(script_path)], capture_output=True, text=True)
    assert result.returncode == 0

if __name__ == "__main__":
    pytest.main(["-v", __file__]) 