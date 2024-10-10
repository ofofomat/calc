import logging
from calc import Calculator

def main():
    calc = Calculator()
    last_result = None

    while True:
        try:
            if last_result is not None:
                use_last = input(f"Last result was {last_result}. Do you want to use it as the first parameter? (y/n): ").strip().lower()
                if use_last == 'y':
                    a = last_result
                else:
                    a = float(input("Enter the first number: "))
            else:
                a = float(input("Enter the first number: "))

            b = float(input("Enter the second number: "))
            operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()

            if operation == 'add':
                last_result = calc.add(a, b)
            elif operation == 'subtract':
                last_result = calc.subtract(a, b)
            elif operation == 'multiply':
                last_result = calc.multiply(a, b)
            elif operation == 'divide':
                last_result = calc.divide(a, b)
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"The result is: {last_result}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except TypeError as te:
            print(f"Error: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()