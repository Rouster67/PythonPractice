import sys

def add_and_print(a, b):
    result = a + b
    print("Sum:", result)

if len(sys.argv) != 3:
    print("Usage: python main.py <number1> <number2>")
    sys.exit(1)

try:
    number1 = float(sys.argv[1])
    number2 = float(sys.argv[2])
except ValueError:
    print("Error: Both arguments should be valid numbers.")
    sys.exit(1)

add_and_print(number1, number2)
