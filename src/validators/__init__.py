"""
Validators Package - Python code validation utilities
"""

from src.validators.python_syntax import PythonValidator

__all__ = [
    "PythonValidator",
]

def validate_file(filepath):
    """Convenience function to validate a Python file"""
    from pathlib import Path
    validator = PythonValidator()
    return validator.validate_files([Path(filepath)])

def validate_files(filepaths):
    """Convenience function to validate multiple Python files"""
    from pathlib import Path
    validator = PythonValidator()
    return validator.validate_files([Path(f) for f in filepaths])
