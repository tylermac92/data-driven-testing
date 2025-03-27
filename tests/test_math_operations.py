import csv
import os
import pytest
from math_operations import add, subtract, multiply, divide

def load_test_data():
    test_data = []
    csv_path = os.path.join(os.path.dirname(__file__), "..", "test_data.csv")
    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            a = float(row["a"])
            b = float(row["b"])
            expected = row["expected"]
            try:
                expected = float(expected)
            except ValueError:
                expected = expected
            test_data.append((row["operation"], a, b, expected))
    return test_data

@pytest.mark.parametrize("operation,a,b,expected", load_test_data())
def test_operations(operation, a, b, expected):
    if operation == "add":
        result = add(a,b)
        assert result == expected, f"Addition failed: {a} + {b} != {expected}"
    elif operation == "subtract":
        result = subtract(a,b)
        assert result == expected, f"Subtraction failed: {a} - {b} != {expected}"
    elif operation == "multiply":
        result = multiply(a,b)
        assert result == expected, f"Multiplication failed: {a} * {b} != {expected}"
    elif operation == "divide":
        if expected == "Error":
            with pytest.raises(ValueError):
                divide(a,b)
        else:
            result = divide(a,b)
            assert result == expected, f"Division failed: {a} / {b} != {expected}"
    else:
        pytest.fail(f"Unknown operation: {operation}")