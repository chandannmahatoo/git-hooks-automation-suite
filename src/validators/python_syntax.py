"""
Python syntax validation logic
"""

import subprocess
import sys
from pathlib import Path
from typing import List


class PythonValidator:
    """Validates Python syntax using py_compile"""
    
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
                
        return all_passed
    
    def _check_syntax(self, file: Path) -> bool:
        """Check Python syntax using py_compile"""
        try:
            # Python's built-in syntax checker
            result = subprocess.run(
                [sys.executable, "-m", "py_compile", str(file)],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode != 0:
                print(f"❌ Syntax error in {file}:")
                print(result.stderr)
                return False
            return True
        except Exception as e:
            print(f"❌ Error checking {file}: {e}")
            return False
