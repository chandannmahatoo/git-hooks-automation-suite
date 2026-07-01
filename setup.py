"""
Setup configuration for Git Hooks Automation Suite
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
readme_file = Path(__file__).parent / "README.md"
if readme_file.exists():
    long_description = readme_file.read_text(encoding="utf-8")
else:
    long_description = "Git Hooks Automation Suite - Python syntax validation with pre-commit hooks"

setup(
    name="git-hooks-automation-suite",
    version="1.0.0",
    author="Chandan Kumar Mahato",
    author_email="chandannmahatoo@example.com",
    description="Automated Python syntax validation with Git pre-commit hooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chandannmahatoo/git-hooks-automation-suite",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "venv"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Add your dependencies here
        # "pre-commit>=3.0.0",  # Uncomment if using pre-commit framework
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "git-hooks-validate=src.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)