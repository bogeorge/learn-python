import sys

"""
Week 2, Day 8: Functions Basics

Exercises to practice defining functions, parameters, return values, and basic function usage.
"""


def exercise_1_math_functions():
    """
    Create basic math operation functions.
    
    1. Create add(), subtract(), multiply(), divide() functions
    2. Each should take two numbers as parameters and return the result
    3. Test each function with different inputs
    """
    
    def add(a, b):
        """Return the sum of a and b."""
        return a + b
    
    def subtract(a, b):
        """Return the difference of a minus b."""
        return a - b
    
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b
    
    def divide(a, b):
        """Return the quotient of a divided by b."""
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    
    # Test the functions
    print("Testing math functions:")
    print(f"  add(5, 3) = {add(5, 3)}")
    print(f"  subtract(10, 4) = {subtract(10, 4)}")
    print(f"  multiply(7, 6) = {multiply(7, 6)}")
    print(f"  divide(15, 3) = {divide(15, 3)}")
    print(f"  divide(10, 0) = {divide(10, 0)}")


def exercise_2_string_functions():
    """
    Create string manipulation functions.
    
    1. Create a function that takes a string and returns it in uppercase
    2. Create a function that takes a string and returns it reversed
    3. Create a function that takes a string and returns its length
    4. Create a function that takes two strings and returns them concatenated
    """
    
    def to_uppercase(text):
        """Convert text to uppercase."""
        return text.upper()
    
    def reverse_string(text):
        """Return the reverse of the input string."""
        return text[::-1]
    
    def string_length(text):
        """Return the length of the string."""
        return len(text)
    
    def concatenate_strings(text1, text2):
        """Return the concatenation of two strings."""
        return text1 + text2
    
    # Test the functions
    test_string = "Hello Python"
    
    print("\nTesting string functions:")
    print(f"  Original string: '{test_string}'")
    print(f"  Uppercase: '{to_uppercase(test_string)}'")
    print(f"  Reversed: '{reverse_string(test_string)}'")
    print(f"  Length: {string_length(test_string)}")
    
    str1 = "Hello"
    str2 = " World!"
    print(f"  Concatenate '{str1}' + '{str2}': '{concatenate_strings(str1, str2)}'")


def exercise_3_temperature_conversion():
    """
    Create temperature conversion functions.
    
    1. Create celsius_to_fahrenheit() function
    2. Create fahrenheit_to_celsius() function
    3. Test both functions with sample temperatures
    """
    
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9
    
    def kelvin_to_celsius(kelvin):
        """Convert Kelvin to Celsius."""
        return kelvin - 273.15
    
    # Test the functions
    print("\nTemperature conversions:")
    
    test_celsius = [0, 20, 37, 100]
    for c in test_celsius:
        f = celsius_to_fahrenheit(c)
        print(f"  {c}°C = {f:.1f}°F")
    
    print()
    
    test_fahrenheit = [32, 68, 98.6, 212]
    for f in test_fahrenheit:
        c = fahrenheit_to_celsius(f)
        print(f"  {f}°F = {c:.1f}°C")


def exercise_4_function_practice():
    """
    More function practice with different return types.
    
    1. Create a function that returns whether a number is even or odd
    2. Create a function that returns the maximum of three numbers
    3. Create a function that returns a formatted greeting
    """
    
    def is_even(number):
        """Return True if number is even, False otherwise."""
        return number % 2 == 0
    
    def max_of_three(a, b, c):
        """Return the maximum of three numbers."""
        return max(a, b, c)
    
    def create_greeting(name, age, city):
        """Return a formatted greeting string."""
        return f"Hello {name}! You are {age} years old and live in {city}."
    
    # Test the functions
    print("\nMore function practice:")
    
    numbers = [2, 7, 10, 15]
    for num in numbers:
        result = "even" if is_even(num) else "odd"
        print(f"  {num} is {result}")
    
    print(f"  max_of_three(3, 7, 2) = {max_of_three(3, 7, 2)}")
    print(f"  max_of_three(10, 5, 10) = {max_of_three(10, 5, 10)}")
    
    greeting = create_greeting("Alice", 28, "New York")
    print(f"  Greeting: {greeting}")


def exercise_5_function_parameters():
    """
    Practice with different types of parameters.
    
    1. Create a function with multiple parameters
    2. Create a function that returns multiple values (using tuple)
    3. Create a function with default parameters
    """
    
    def calculate_rectangle(length, width):
        """Calculate area and perimeter of a rectangle."""
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter
    
    def format_person_info(name, age, occupation="unknown"):
        """Format person information with default occupation."""
        return f"{name}, {age}, {occupation}"
    
    # Test the functions
    print("\nFunction parameters practice:")
    
    area, perimeter = calculate_rectangle(5, 3)
    print(f"  Rectangle (5x3): Area = {area}, Perimeter = {perimeter}")
    
    area, perimeter = calculate_rectangle(7.5, 4.2)
    print(f"  Rectangle (7.5x4.2): Area = {area:.2f}, Perimeter = {perimeter:.2f}")
    
    print(f"  Person 1: {format_person_info('Bob', 35)}")
    print(f"  Person 2: {format_person_info('Charlie', 42, 'Engineer')}")


def mini_project_unit_converter():
    """
    Unit Converter with Functions
    
    Create a comprehensive unit converter with multiple conversion options.
    
    Features:
    1. Convert between different units (length, weight, temperature)
    2. Use functions for each conversion type
    3. Provide a menu for user selection
    """
    print("=" * 50)
    print("UNIT CONVERTER")
    print("=" * 50)
    
    def meters_to_feet(meters):
        """Convert meters to feet."""
        return meters * 3.28084
    
    def feet_to_meters(feet):
        """Convert feet to meters."""
        return feet / 3.28084
    
    def kilograms_to_pounds(kg):
        """Convert kilograms to pounds."""
        return kg * 2.20462
    
    def pounds_to_kilograms(lbs):
        """Convert pounds to kilograms."""
        return lbs / 2.20462
    
    def celsius_to_fahrenheit(c):
        """Convert Celsius to Fahrenheit."""
        return (c * 9/5) + 32
    
    def fahrenheit_to_celsius(f):
        """Convert Fahrenheit to Celsius."""
        return (f - 32) * 5/9
    
    print("\nConversion Options:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("0. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (0-6): ")
            
            if choice == '0':
                print("Goodbye!")
                break
            
            if choice == '1':
                meters = float(input("Enter meters: "))
                feet = meters_to_feet(meters)
                print(f"{meters} meters = {feet:.2f} feet")
            
            elif choice == '2':
                feet = float(input("Enter feet: "))
                meters = feet_to_meters(feet)
                print(f"{feet} feet = {meters:.2f} meters")
            
            elif choice == '3':
                kg = float(input("Enter kilograms: "))
                lbs = kilograms_to_pounds(kg)
                print(f"{kg} kg = {lbs:.2f} pounds")
            
            elif choice == '4':
                lbs = float(input("Enter pounds: "))
                kg = pounds_to_kilograms(lbs)
                print(f"{lbs} pounds = {kg:.2f} kg")
            
            elif choice == '5':
                c = float(input("Enter Celsius: "))
                f = celsius_to_fahrenheit(c)
                print(f"{c}°C = {f:.1f}°F")
            
            elif choice == '6':
                f = float(input("Enter Fahrenheit: "))
                c = fahrenheit_to_celsius(f)
                print(f"{f}°F = {c:.1f}°C")
            
            else:
                print("Invalid choice. Please enter 0-6.")
        
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break


def run_all_exercises():
    """Run all Day 8 exercises."""
    print("=" * 60)
    print("Week 2, Day 8: Functions Basics")
    print("=" * 60)

    print("\n--- Exercise 1: Math Functions ---")
    exercise_1_math_functions()

    print("\n--- Exercise 2: String Functions ---")
    exercise_2_string_functions()

    print("\n--- Exercise 3: Temperature Conversion ---")
    exercise_3_temperature_conversion()

    print("\n--- Exercise 4: Function Practice ---")
    exercise_4_function_practice()

    print("\n--- Exercise 5: Function Parameters ---")
    exercise_5_function_parameters()

    print("\n" + "=" * 60)
    print("Mini Project: Unit Converter")
    print("=" * 60)
    mini_project_unit_converter()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 8 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()