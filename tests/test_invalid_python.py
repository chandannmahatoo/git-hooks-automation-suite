"""
Invalid Python file for testing - contains syntax errors
"""

def main():  # ✅ Added colon
    """Missing colon was on purpose"""
    print("No parentheses on purpose")  # ✅ Fixed print syntax
    return True  # This will never be reached

if __name__ == "__main__":
    main()  # ✅ Added parentheses
