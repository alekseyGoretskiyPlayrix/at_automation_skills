import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestMathOperations:
    """Class to test various methods of the MathOperations class."""

    @pytest.mark.smoke
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 8),  # Test with positive numbers
        (-2, -3, -5),  # Test with negative numbers
        (10, -5, 5),  # Test with numbers of different signs
        (0, 7, 7),  # Test when the first number is 0
        (8, 0, 8),  # Test when the second number is 0
        (-4, 4, 0),  # Test with opposite numbers
        (6, 6, 12)  # Test with identical numbers
    ])
    def test_math_operation_sum(self, math_ops, a, b, expected):
        """
        Test the addition method of MathOperations.

        Args:
            math_ops (MathOperations): An instance of MathOperations.
            a (int): The first operand.
            b (int): The second operand.
            expected (int): The expected sum.

        Verifies that the sum of `a` and `b` matches the expected result.
        """
        assert math_ops.math_operation_sum(a, b) == expected

    @pytest.mark.regression
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),  # Test with positive numbers where the first is greater
        (3, 5, -2),  # Test with positive numbers where the second is greater
        (-2, -3, 1),  # Test with negative numbers
        (10, -5, 15),  # Test with numbers of different signs
        (0, 7, -7),  # Test when the first number is 0
        (8, 0, 8),  # Test when the second number is 0
        (-4, 4, -8),  # Test with opposite numbers
        (6, 6, 0)  # Test with identical numbers
    ])
    def test_math_operation_subtract(self, math_ops, a, b, expected):
        """
        Test the subtraction method of MathOperations.

        Args:
            math_ops (MathOperations): An instance of MathOperations.
            a (int): The first operand (minuend).
            b (int): The second operand (subtrahend).
            expected (int): The expected result of subtraction.

        Verifies that `a - b` matches the expected result.
        """
        assert math_ops.math_operation_subtract(a, b) == expected

    @pytest.mark.smoke
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 15),  # Test with positive numbers
        (-2, -3, 6),  # Test with negative numbers
        (10, -5, -50),  # Test with numbers of different signs
        (0, 7, 0),  # Test when the first number is 0
        (8, 0, 0),  # Test when the second number is 0
        (-4, 4, -16),  # Test with opposite numbers
        (6, 6, 36)  # Test with identical numbers
    ])
    def test_math_operation_multiplication(self, math_ops, a, b, expected):
        """
        Test the multiplication method of MathOperations.

        Args:
            math_ops (MathOperations): An instance of MathOperations.
            a (int): The first operand.
            b (int): The second operand.
            expected (int): The expected product.

        Verifies that the product of `a` and `b` matches the expected result.
        """
        assert math_ops.math_operation_multiplication(a, b) == expected

    @pytest.mark.regression
    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2.0),  # Test with positive integers where division has no remainder
        (7, 2, 3.5),  # Test with positive integers where division results in a float
        (-8, 4, -2.0),  # Test with a negative numerator
        (8, -4, -2.0),  # Test with a negative denominator
        (-9, -3, 3.0),  # Test with both numerator and denominator negative
        (0, 5, 0.0),  # Test when numerator is zero
    ])
    def test_math_operation_division(self, math_ops, a, b, expected):
        """
        Test the division method of MathOperations.

        Args:
            math_ops (MathOperations): An instance of MathOperations.
            a (int): The numerator.
            b (int): The denominator.
            expected (float): The expected result of division.

        Verifies that `a / b` matches the expected result.
        """
        assert math_ops.math_operation_division(a, b) == expected

    @pytest.mark.smoke
    @pytest.mark.parametrize("a, b", [
        (10, 0),  # Test division by zero
    ])
    def test_math_operation_division_by_zero(self, math_ops, a, b):
        """
        Test that division by zero raises a ValueError.

        Args:
            math_ops (MathOperations): An instance of MathOperations.

        Verifies that attempting to divide by zero raises a ValueError.
        """
        with pytest.raises(ValueError, match="Division by zero is not allowed."):
            math_ops.math_operation_division(a, b)

    @pytest.mark.regression
    @pytest.mark.parametrize("operation, a, b, expected", [
        ("add", 1, 2, 3),
        ("subtract", 5, 3, 2),
        ("multiply", 2, 4, 8),
        ("divide", 10, 2, 5),
    ])
    def test_math_operation_combined(self, math_ops, operation, a, b, expected):
        """
        Test multiple mathematical operations in a single test method.

        Args:
            math_ops (MathOperations): An instance of MathOperations.
            operation (str): The type of operation to perform. Options are "add", "subtract", "multiply", "divide".
            a (int): The first operand.
            b (int): The second operand.
            expected (int or float): The expected result of the operation.

        This test method uses parameterization to validate different mathematical operations,
        ensuring that the correct method is invoked based on the `operation` parameter.
        Verifies that the output matches the `expected` value for each operation.
        """
        if operation == "add":
            assert math_ops.math_operation_sum(a, b) == expected
        elif operation == "subtract":
            assert math_ops.math_operation_subtract(a, b) == expected
        elif operation == "multiply":
            assert math_ops.math_operation_multiplication(a, b) == expected
        elif operation == "divide":
            assert math_ops.math_operation_division(a, b) == expected
