"""
Integration tests for the pre-commit hook
"""

import subprocess
from pathlib import Path


def test_valid_python_commit():
    """Test that valid Python files pass the hook"""
    result = subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "Test valid"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    assert result.returncode == 0


def test_invalid_python_blocks_commit():
    """Test that invalid Python files block the commit"""
    # Create invalid file
    invalid_file = Path("test_invalid.py")
    invalid_file.write_text("print 'syntax error'")
    
    subprocess.run(["git", "add", str(invalid_file)])
    result = subprocess.run(
        ["git", "commit", "-m", "Should fail"],
        capture_output=True,
        text=True
    )
    
    assert result.returncode != 0
    invalid_file.unlink()  # Cleanup