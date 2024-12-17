class MathOperations:

    def math_operation_sum(self, a, b):
        """
        Calculate the sum of two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of a and b.
        """
        return a + b

    def math_operation_subtract(self, a, b):
        """
            Calculate the difference between two numbers.

            Args:
                a (int): The first number.
                b (int): The second number.

            Returns:
                int: The result of subtracting b from a.
            """
        return a - b

    def math_operation_multiplication(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The result of multiplying a and b.
        """
        return a * b

    def math_operation_division(self, a, b):
        """
        Divide one number by another.

        Args:
            a (int or float): The numerator.
            b (int or float): The denominator.

        Returns:
            float: The result of dividing a by b.

        Raises:
            ValueError: If the denominator is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
