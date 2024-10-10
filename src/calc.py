import logging

class Calculator:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def add(self, a, b):
        self._validate_input(a, b)
        result = a + b
        logging.info(f"Adding {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        self._validate_input(a, b)
        result = a - b
        logging.info(f"Subtracting {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        self._validate_input(a, b)
        result = a * b
        logging.info(f"Multiplying {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        self._validate_input(a, b)
        if b == 0:
            logging.error("Attempted to divide by zero")
            raise ValueError("Cannot divide by zero")
        result = a / b
        logging.info(f"Dividing {a} / {b} = {result}")
        return result

    def _validate_input(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logging.error(f"Invalid input types: {a} ({type(a)}), {b} ({type(b)})")
            raise TypeError("Inputs must be int or float")