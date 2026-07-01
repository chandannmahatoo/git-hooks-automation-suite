#!/usr/bin/env python3
"""
Main entry point for Python syntax validation
"""

import sys
import argparse
from pathlib import Path
from validators.python_syntax import PythonValidator


def main():
    parser = argparse.ArgumentParser(
        description="Python syntax validator for pre-commit hooks"
    )
    parser.add_argument(
        '--validate',
        nargs='+',
        help='Python files to validate'
    )
    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Check all Python files in src/'
    )
    
    args = parser.parse_args()
    validator = PythonValidator()
    
    if args.check_all:
        files = list(Path('src').rglob('*.py'))
    elif args.validate:
        files = [Path(f) for f in args.validate]
    else:
        print("No files specified. Use --validate or --check-all")
        sys.exit(0)
    
    success = validator.validate_files(files)
    
    if not success:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()