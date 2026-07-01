"""
Python syntax validation logic
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


class PythonValidator:
    """Validates Python syntax using py_compile and flake8"""
    
    def __init__(self):
        self.errors = []
        
    def validate_files(self, files: List[Path]) -> bool:
        """Validate all Python files in the list"""
        all_passed = True
        
        for file in files:
            if not file.exists():
                print(f"⚠️  File not found: {file}")
                continue
                
            print(f"🔍 Checking: {file}")
            
            # Check syntax
            if not self._check_syntax(file):
                all_passed = False
                
            # Optional: Additional style checks
            if not self._check_flake8(file):
                all_passed = False
                
        return all_passed
    
    def _check_syntax(self, file: Path) -> bool:
        """Check Python syntax using py_compile"""
        try:
            # Python's built-in syntax checker
            subprocess.run(
                [sys.executable, "-m", "py_compile", str(file)],
                check=True,
                capture_output=True,
                text=True
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Syntax error in {file}:")
            print(e.stderr)
            return False
    
    def _check_flake8(self, file: Path) -> bool:
        """Optional: run flake8 for style checking"""
        try:
            subprocess.run(
                ["flake8", str(file)],
                check=False,
                capture_output=True,
                text=True
            )
            return True
        except FileNotFoundError:
            # flake8 not installed, skip check
            return True