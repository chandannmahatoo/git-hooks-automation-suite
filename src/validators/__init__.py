"""
Validators Package - Python code validation utilities
"""

# Import the main validator class
from src.validators.python_syntax import PythonValidator

# Define what's exported
__all__ = [
    "PythonValidator",
]

# Version info
__version__ = "1.0.0"

# Optional: Auto-import common functionality
# This allows: from src.validators import validate_file
def validate_file(filepath):
    """Convenience function to validate a Python file"""
    validator = PythonValidator()
    return validator.validate_files([filepath])

def validate_files(filepaths):
    """Convenience function to validate multiple Python files"""
    validator = PythonValidator()
    return validator.validate_files(filepaths)

# Add to __all__
__all__.extend(["validate_file", "validate_files"])
