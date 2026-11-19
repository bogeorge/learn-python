"""
Project 1: Simple Calculator
Week 1, Beginner Level

A basic calculator that performs arithmetic operations.
This project practices:
- User input
- Variables
- Conditional statements
- Basic math operations
"""

def simple_calculator():
    """
    Main calculator function that runs the program.
    """
    print("=" * 40)
    print("SIMPLE CALCULATOR")
    print("=" * 40)
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulus (%)")
    print("=" * 40)
    
    # Get user input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /, **, %): ").strip()
        
        # Perform calculation based on operation
        result = None
        if operation == "+":
            result = num1 + num2
            operation_name = "Addition"
        elif operation == "-":
            result = num1 - num2
            operation_name = "Subtraction"
        elif operation == "*":
            result = num1 * num2
            operation_name = "Multiplication"
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
            operation_name = "Division"
        elif operation == "**":
            result = num1 ** num2
            operation_name = "Exponentiation"
        elif operation == "%":
            result = num1 % num2
            operation_name = "Modulus"
        else:
            print(f"Error: Invalid operation '{operation}'")
            print("Please use one of: +, -, *, /, **, %")
            return
        
        # Display result
        print("\n" + "=" * 40)
        print(f"RESULT: {operation_name}")
        print(f"{num1} {operation} {num2} = {result}")
        print("=" * 40)
        
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")


def advanced_calculator():
    """
    Advanced version with more features.
    """
    print("=" * 40)
    print("ADVANCED CALCULATOR")
    print("=" * 40)
    
    while True:
        print("\nChoose an operation:")
        print("1. Basic Arithmetic")
        print("2. Area Calculator")
        print("3. Temperature Converter")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            simple_calculator()
        elif choice == "2":
            area_calculator()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def area_calculator():
    """
    Calculate area of different shapes.
    """
    print("\n" + "=" * 40)
    print("AREA CALCULATOR")
    print("=" * 40)
    print("Available shapes:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    
    shape = input("Enter shape (1-3): ").strip()
    
    try:
        if shape == "1":  # Rectangle
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print(f"Area of rectangle: {length} × {width} = {area}")
            
        elif shape == "2":  # Circle
            radius = float(input("Enter radius: "))
            area = 3.14159 * (radius ** 2)  # πr²
            print(f"Area of circle: π × {radius}² = {area:.2f}")
            
        elif shape == "3":  # Triangle
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"Area of triangle: ½ × {base} × {height} = {area}")
            
        else:
            print("Invalid shape selection.")
            
    except ValueError:
        print("Error: Please enter valid numbers!")


def temperature_converter():
    """
    Convert between Celsius and Fahrenheit.
    """
    print("\n" + "=" * 40)
    print("TEMPERATURE CONVERTER")
    print("=" * 40)
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter conversion (1-2): ").strip()
    
    try:
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.1f}°F")
            
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.1f}°C")
            
        else:
            print("Invalid choice.")
            
    except ValueError:
        print("Error: Please enter a valid number!")


def run_tests():
    """
    Test the calculator functions with example values.
    """
    print("Running calculator tests...")
    
    # Test basic operations
    test_cases = [
        (10, 5, "+", 15, "Addition"),
        (10, 5, "-", 5, "Subtraction"),
        (10, 5, "*", 50, "Multiplication"),
        (10, 5, "/", 2, "Division"),
        (2, 3, "**", 8, "Exponentiation"),
        (10, 3, "%", 1, "Modulus"),
    ]
    
    for num1, num2, op, expected, name in test_cases:
        print(f"\nTest: {num1} {op} {num2}")
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "**":
            result = num1 ** num2
        elif op == "%":
            result = num1 % num2
            
        if result == expected:
            print(f"✓ {name}: {result} (Correct)")
        else:
            print(f"✗ {name}: {result} (Expected: {expected})")
    
    print("\nTests completed!")


def main():
    """
    Main function to run the calculator program.
    """
    print("Welcome to Python Calculator!")
    print("Choose calculator type:")
    print("1. Simple Calculator (Basic operations)")
    print("2. Advanced Calculator (More features)")
    print("3. Run Tests")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            simple_calculator()
        elif choice == "2":
            advanced_calculator()
        elif choice == "3":
            run_tests()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    # Run the calculator when this file is executed
    main()