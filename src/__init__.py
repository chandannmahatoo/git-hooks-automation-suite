"""
Git Hooks Automation Suite - Main Package
"""

# Import key components for easy access
from src.validators.python_syntax import PythonValidator

# Define what's available when someone imports *
__all__ = [
    "PythonValidator",
]

# Package metadata
__version__ = "1.0.0"
__author__ = "Chandan Kumar Mahato"

# Initialize package-level logger (optional)
import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# Package initialization
def setup():
    """Initialize the package (optional)"""
    logger.info("Initializing git-hooks-automation-suite")

# Auto-run setup when package is imported
# setup()  # Uncomment if needed
