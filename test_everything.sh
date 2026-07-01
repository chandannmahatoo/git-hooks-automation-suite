#!/bin/bash
echo "=========================================="
echo "🧪 Git Hooks Automation Suite - Test Suite"
echo "=========================================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Counters
TOTAL=0
PASSED=0
FAILED=0

test_step() {
    TOTAL=$((TOTAL + 1))
    echo -e "${BLUE}▶ Test $TOTAL: $1${NC}"
    if eval "$2" 2>/dev/null; then
        echo -e "${GREEN}✅ PASSED${NC}"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}❌ FAILED${NC}"
        FAILED=$((FAILED + 1))
    fi
    echo ""
}

echo "1️⃣ Testing Package Structure"
echo "-----------------------------"
test_step "src/__init__.py exists" "test -f src/__init__.py"
test_step "src/validators/__init__.py exists" "test -f src/validators/__init__.py"
test_step "tests/__init__.py exists" "test -f tests/__init__.py"

echo "2️⃣ Testing Python Imports"
echo "--------------------------"
test_step "Import src package" "python3 -c 'import src'"
test_step "Import PythonValidator" "python3 -c 'from src.validators import PythonValidator'"
test_step "Import main module" "python3 -c 'from src import main'"

echo "3️⃣ Testing Validator Functionality"
echo "----------------------------------"

# Create test files
echo "print('Valid Python code')" > test_valid.py
echo "print 'Invalid Python code'" > test_invalid.py
echo "def test():" >> test_invalid.py
echo "    return True" >> test_invalid.py

test_step "Valid Python syntax passes" "python3 -m py_compile test_valid.py"
test_step "Invalid Python syntax fails" "! python3 -m py_compile test_invalid.py"

# Test PythonValidator class
cat > test_validator.py << 'PYEOF'
from src.validators import PythonValidator
import sys
from pathlib import Path

with open("test_valid.py", "w") as f:
    f.write("print('Valid')\n")

validator = PythonValidator()
result = validator.validate_files([Path("test_valid.py")])
sys.exit(0 if result else 1)
PYEOF

test_step "PythonValidator class works" "python3 test_validator.py"

# Clean up
rm -f test_valid.py test_invalid.py test_validator.py

echo "4️⃣ Testing Pre-commit Hook"
echo "--------------------------"
test_step "Hook is executable" "test -x .git/hooks/pre-commit"

# Test valid commit - use a real commit (not dry-run)
echo "print('Test valid commit')" > valid_test.py
git add valid_test.py 2>/dev/null
git commit -m "Test valid commit" 2>&1 > /dev/null
if [ $? -eq 0 ]; then
    test_step "Valid commit passes hook" "true"
else
    test_step "Valid commit passes hook" "false"
fi

# Test invalid commit
echo "print 'Test invalid commit'" > invalid_test.py
git add invalid_test.py 2>/dev/null
git commit -m "Test invalid commit" 2>&1 > /dev/null
if [ $? -ne 0 ]; then
    test_step "Invalid commit blocked by hook" "true"
else
    test_step "Invalid commit blocked by hook" "false"
fi

# Clean up
git reset HEAD~1 2>/dev/null  # Undo the valid commit
git reset HEAD invalid_test.py 2>/dev/null
rm -f valid_test.py invalid_test.py

echo "5️⃣ Testing CLI Entry Point"
echo "--------------------------"
test_step "src/main.py exists" "test -f src/main.py"
test_step "main() function exists" "grep -q 'def main()' src/main.py"

echo "6️⃣ Testing Installation"
echo "-----------------------"
test_step "setup.py exists" "test -f setup.py"
test_step "requirements.txt exists" "test -f requirements.txt"
test_step "README.md exists" "test -f README.md"

echo "7️⃣ Testing Pre-commit Framework (Optional)"
echo "----------------------------------------"
if command -v pre-commit &> /dev/null; then
    test_step "Pre-commit is installed" "pre-commit --version"
    test_step "Pre-commit config exists" "test -f .pre-commit-config.yaml"
else
    echo -e "${YELLOW}⚠️  pre-commit not installed - skipping pre-commit tests${NC}"
    echo -e "${YELLOW}   Install with: pip install pre-commit${NC}"
    echo ""
fi

echo "=========================================="
echo "📊 Test Summary"
echo "=========================================="
echo -e "Total tests:  ${BLUE}$TOTAL${NC}"
echo -e "Passed:       ${GREEN}$PASSED${NC}"
echo -e "Failed:       ${RED}$FAILED${NC}"

if [ $FAILED -eq 0 ]; then
    echo -e "\n${GREEN}🎉 ALL TESTS PASSED!${NC}"
    echo "Your project is working perfectly! 🚀"
    exit 0
else
    echo -e "\n${RED}❌ Some tests failed.${NC}"
    echo "Please check the errors above."
    exit 1
fi
