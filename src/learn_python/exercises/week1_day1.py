import sys

"""
Week 1, Day 1: Getting Started with Python

Exercises to practice basic Python syntax and concepts.
Complete each exercise by writing the code in the function.
"""


def exercise_1_hello_world():
    """
    Print "Hello, World!" to the console.
    Then print your name on a new line.
    """
    # Your code here
    print("Hello, World!")
    print("Bo George")  # Replace with your actual name


def exercise_2_variables():
    """
    Create variables for:
    - Your name (string)
    - Your age (integer)
    - Your height in meters (float)
    - Whether you like Python (boolean)

    Print each variable with a descriptive message.
    """
    # Your code here
    name = "Bo"
    age = 50
    height = 1.75
    likes_python = True

    print(f"My name is {name}")
    print(f"I am {age} years old")
    print(f"My height is {height} meters")
    print(f"Do I like Python? {likes_python}")


def exercise_3_basic_math():
    """
    Create two variables: a = 15, b = 4
    Perform and print the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Integer division
    6. Modulus (remainder)
    7. Exponentiation (a to the power of b)
    """
    # Your code here
    a = 15
    b = 4

    print(f"a = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Integer division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a**b}")


def exercise_4_string_operations():
    """
    Create a variable with your full name.
    Perform and print:
    1. Length of your name
    2. Your name in uppercase
    3. Your name in lowercase
    4. First letter of your name
    5. Last letter of your name
    6. Your name repeated 3 times
    """
    # Your code here
    full_name = "John Doe"

    print(f"My full name: {full_name}")
    print(f"Length: {len(full_name)} characters")
    print(f"Uppercase: {full_name.upper()}")
    print(f"Lowercase: {full_name.lower()}")
    print(f"First letter: {full_name[0]}")
    print(f"Last letter: {full_name[-1]}")
    print(f"Repeated 3 times: {full_name * 3}")


def exercise_5_type_conversion():
    """
    1. Create a string variable: number_str = "123"
    2. Convert it to integer and float
    3. Create an integer: number_int = 456
    4. Convert it to string and float
    5. Create a float: number_float = 78.9
    6. Convert it to string and integer (note what happens with integer conversion)

    Print all conversions with type information.
    """
    # Your code here
    number_str = "123"
    number_int = 456
    number_float = 78.9

    # String to other types
    str_to_int = int(number_str)
    str_to_float = float(number_str)

    # Integer to other types
    int_to_str = str(number_int)
    int_to_float = float(number_int)

    # Float to other types
    float_to_str = str(number_float)
    float_to_int = int(number_float)  # This will truncate to 78

    print(
        f"Original string '{number_str}' -> int: {str_to_int} (type: {type(str_to_int)})"
    )
    print(
        f"Original string '{number_str}' -> float: {str_to_float} (type: {type(str_to_float)})"
    )
    print(
        f"Original int {number_int} -> str: '{int_to_str}' (type: {type(int_to_str)})"
    )
    print(
        f"Original int {number_int} -> float: {int_to_float} (type: {type(int_to_float)})"
    )
    print(
        f"Original float {number_float} -> str: '{float_to_str}' (type: {type(float_to_str)})"
    )
    print(
        f"Original float {number_float} -> int: {float_to_int} (type: {type(float_to_int)}) - Note: decimal part is lost!"
    )


def mini_project_temperature_converter():
    """
    Create a temperature converter that:
    1. Asks the user for a temperature in Celsius
    2. Converts it to Fahrenheit using formula: F = (C × 9/5) + 32
    3. Prints both temperatures with clear labels

    Bonus: Also convert to Kelvin (K = C + 273.15)
    """
    # Your code here
    print("=== Temperature Converter ===")

    # Get input from user
    celsius_input = input("Enter temperature in Celsius: ")

    # Convert to float
    celsius = float(celsius_input)

    # Convert to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32

    # Convert to Kelvin
    kelvin = celsius + 273.15

    # Display results
    print("\nTemperature Conversion Results:")
    print(f"Celsius: {celsius}°C")
    print(f"Fahrenheit: {fahrenheit}°F")
    print(f"Kelvin: {kelvin}K")

    # Add some fun facts
    if celsius < 0:
        print("Brrr! That's below freezing! ❄️")
    elif celsius > 30:
        print("Wow, that's quite warm! ☀️")
    else:
        print("Nice, comfortable temperature! 😊")


def run_all_exercises():
    """
    Run all the exercises in order.
    """
    print("=" * 50)
    print("Running Week 1, Day 1 Exercises")
    print("=" * 50)

    print("\n--- Exercise 1: Hello World ---")
    exercise_1_hello_world()

    print("\n--- Exercise 2: Variables ---")
    exercise_2_variables()

    print("\n--- Exercise 3: Basic Math ---")
    exercise_3_basic_math()

    print("\n--- Exercise 4: String Operations ---")
    exercise_4_string_operations()

    print("\n--- Exercise 5: Type Conversion ---")
    exercise_5_type_conversion()

    print("\n" + "=" * 50)
    print("Mini Project: Temperature Converter")
    print("=" * 50)
    mini_project_temperature_converter()

    print("\n" + "=" * 50)
    print("Congratulations! You've completed Day 1 exercises!")
    print("=" * 50)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Run {func_name}")
        globals()[func_name]()
    else:
        print("Run em all")
        # This runs when you execute the file directly
        run_all_exercises()
