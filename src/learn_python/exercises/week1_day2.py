import sys

"""
Week 1, Day 2: Basic Data Types & Operations

Exercises to practice Python data types and operations.
"""


def exercise_1_numeric_operations():
    """
    Create variables for:
    - Two integers
    - Two floats
    - One complex number

    Perform and print various mathematical operations.
    """
    # Your code here
    int1 = 10
    int2 = 3
    float1 = 7.5
    float2 = 2.5
    complex_num = 3 + 4j

    print("Numeric Operations:")
    print(f"Integers: {int1}, {int2}")
    print(f"  Addition: {int1} + {int2} = {int1 + int2}")
    print(f"  Subtraction: {int1} - {int2} = {int1 - int2}")
    print(f"  Multiplication: {int1} * {int2} = {int1 * int2}")
    print(f"  Division: {int1} / {int2} = {int1 / int2}")
    print(f"  Integer division: {int1} // {int2} = {int1 // int2}")
    print(f"  Modulus: {int1} % {int2} = {int1 % int2}")

    print(f"\nFloats: {float1}, {float2}")
    print(f"  Addition: {float1} + {float2} = {float1 + float2}")
    print(f"  Subtraction: {float1} - {float2} = {float1 - float2}")
    print(f"  Multiplication: {float1} * {float2} = {float1 * float2}")
    print(f"  Division: {float1} / {float2} = {float1 / float2}")

    print(f"\nComplex number: {complex_num}")
    print(f"  Real part: {complex_num.real}")
    print(f"  Imaginary part: {complex_num.imag}")
    print(f"  Conjugate: {complex_num.conjugate()}")


def exercise_2_string_formatting():
    """
    Practice different string formatting methods:
    1. f-strings (Python 3.6+)
    2. format() method
    3. % formatting (older style)
    4. Concatenation

    Create a profile with name, age, and profession.
    """
    # Your code here
    name = "Alex"
    age = 28
    profession = "Software Developer"

    print("String Formatting Examples:")

    # 1. f-strings (modern, recommended)
    profile_fstring = (
        f"My name is {name}, I'm {age} years old, and I work as a {profession}."
    )
    print(f"1. f-string: {profile_fstring}")

    # 2. format() method
    profile_format = "My name is {}, I'm {} years old, and I work as a {}.".format(
        name, age, profession
    )
    print(f"2. format(): {profile_format}")

    # 3. % formatting
    profile_percent = "My name is %s, I'm %d years old, and I work as a %s." % (
        name,
        age,
        profession,
    )
    print(f"3. %% formatting: {profile_percent}")

    # 4. Concatenation
    profile_concat = (
        "My name is "
        + name
        + ", I'm "
        + str(age)
        + " years old, and I work as a "
        + profession
        + "."
    )
    print(f"4. Concatenation: {profile_concat}")

    # Additional formatting examples
    print("\nAdditional Formatting:")
    price = 49.99
    quantity = 3
    total = price * quantity

    print(f"Price: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")

    # Padding and alignment
    print(f"\n{'Item':<10} {'Price':>10} {'Quantity':>10} {'Total':>10}")
    print(f"{'Apple':<10} {2.99:>10.2f} {5:>10} {2.99 * 5:>10.2f}")
    print(f"{'Banana':<10} {1.49:>10.2f} {3:>10} {1.49 * 3:>10.2f}")
    print(f"{'Orange':<10} {3.25:>10.2f} {2:>10} {3.25 * 2:>10.2f}")


def exercise_3_boolean_operations():
    """
    Practice boolean operations and comparisons.
    Create variables and test various conditions.
    """
    # Your code here
    a = 10
    b = 20
    c = 10

    print("Boolean Operations:")
    print(f"Variables: a = {a}, b = {b}, c = {c}")

    # Comparison operators
    print("\nComparison Operators:")
    print(f"a == b: {a == b}")  # Equal to
    print(f"a != b: {a != b}")  # Not equal to
    print(f"a < b: {a < b}")  # Less than
    print(f"a > b: {a > b}")  # Greater than
    print(f"a <= c: {a <= c}")  # Less than or equal to
    print(f"a >= c: {a >= c}")  # Greater than or equal to

    # Logical operators
    print("\nLogical Operators:")
    x = True
    y = False

    print(f"x = {x}, y = {y}")
    print(f"x and y: {x and y}")  # AND
    print(f"x or y: {x or y}")  # OR
    print(f"not x: {not x}")  # NOT

    # Combined expressions
    print("\nCombined Expressions:")
    age = 25
    has_license = True
    has_experience = False

    print(f"Age: {age}, Has license: {has_license}, Has experience: {has_experience}")

    can_drive = age >= 16 and has_license
    print(f"Can drive (age >= 16 and has license): {can_drive}")

    needs_training = age >= 18 and not has_experience
    print(f"Needs training (age >= 18 and not has experience): {needs_training}")

    is_eligible = (age >= 21 and has_license) or (age >= 18 and has_experience)
    print(f"Is eligible for advanced training: {is_eligible}")


def exercise_4_type_checking():
    """
    Practice checking and converting data types.
    Create variables of different types and check/convert them.
    """
    # Your code here
    print("Type Checking and Conversion:")

    # Create variables of different types
    var_int = 42
    var_float = 3.14
    var_str = "123"
    var_bool = True
    var_none = None

    # Display original types
    print("Original variables:")
    print(f"  var_int = {var_int} (type: {type(var_int)})")
    print(f"  var_float = {var_float} (type: {type(var_float)})")
    print(f"  var_str = '{var_str}' (type: {type(var_str)})")
    print(f"  var_bool = {var_bool} (type: {type(var_bool)})")
    print(f"  var_none = {var_none} (type: {type(var_none)})")

    # Type checking
    print("\nType checking with isinstance():")
    print(f"  isinstance(var_int, int): {isinstance(var_int, int)}")
    print(f"  isinstance(var_float, float): {isinstance(var_float, float)}")
    print(f"  isinstance(var_str, str): {isinstance(var_str, str)}")
    print(f"  isinstance(var_bool, bool): {isinstance(var_bool, bool)}")

    # Type conversion
    print("\nType conversion:")

    # String to other types
    str_to_int = int(var_str)
    str_to_float = float(var_str)
    str_to_bool = bool(var_str)  # Non-empty string is True

    print(f"  int('{var_str}') = {str_to_int} (type: {type(str_to_int)})")
    print(f"  float('{var_str}') = {str_to_float} (type: {type(str_to_float)})")
    print(f"  bool('{var_str}') = {str_to_bool} (type: {type(str_to_bool)})")

    # Integer to other types
    int_to_str = str(var_int)
    int_to_float = float(var_int)
    int_to_bool = bool(var_int)  # Non-zero is True

    print(f"  str({var_int}) = '{int_to_str}' (type: {type(int_to_str)})")
    print(f"  float({var_int}) = {int_to_float} (type: {type(int_to_float)})")
    print(f"  bool({var_int}) = {int_to_bool} (type: {type(int_to_bool)})")

    # Boolean to other types
    bool_to_int = int(var_bool)  # True = 1, False = 0
    bool_to_str = str(var_bool)
    bool_to_float = float(var_bool)

    print(f"  int({var_bool}) = {bool_to_int} (type: {type(bool_to_int)})")
    print(f"  str({var_bool}) = '{bool_to_str}' (type: {type(bool_to_str)})")
    print(f"  float({var_bool}) = {bool_to_float} (type: {type(bool_to_float)})")

    # Truthy/falsy values
    print("\nTruthy/Falsy values:")
    test_values = [0, 1, 0.0, 1.0, "", "hello", [], [1, 2], {}, {"key": "value"}, None]

    for value in test_values:
        bool_value = bool(value)
        print(f"  bool({repr(value)}) = {bool_value}")


def mini_project_bmi_calculator():
    """
    Create a BMI (Body Mass Index) calculator.

    BMI Formula: weight (kg) / (height (m))²

    BMI Categories:
    - Underweight: < 18.5
    - Normal weight: 18.5 - 24.9
    - Overweight: 25 - 29.9
    - Obesity: ≥ 30

    Features:
    1. Ask for weight and height
    2. Calculate BMI
    3. Display BMI category
    4. Provide health advice
    """
    # Your code here
    print("=" * 50)
    print("BMI CALCULATOR")
    print("=" * 50)
    print("Calculate your Body Mass Index")
    print("=" * 50)

    try:
        # Get user input
        print("\nPlease enter your information:")

        # Choose unit system
        print("\nChoose unit system:")
        print("1. Metric (kg, meters)")
        print("2. Imperial (pounds, inches)")

        unit_choice = input("\nEnter choice (1 or 2): ").strip()

        if unit_choice == "1":
            # Metric system
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))

            # Calculate BMI
            bmi = weight / (height**2)

        elif unit_choice == "2":
            # Imperial system
            weight = float(input("Enter your weight in pounds (lb): "))
            height = float(input("Enter your height in inches (in): "))

            # Convert to metric for calculation
            weight_kg = weight * 0.453592
            height_m = height * 0.0254

            # Calculate BMI
            bmi = weight_kg / (height_m**2)

        else:
            print("Invalid choice. Using metric system by default.")
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
            bmi = weight / (height**2)

        # Display results
        print("\n" + "=" * 50)
        print("RESULTS")
        print("=" * 50)
        print(f"Your BMI: {bmi:.1f}")

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
            advice = (
                "Consider consulting a nutritionist to develop a healthy eating plan."
            )
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
            advice = "Great job! Maintain your healthy lifestyle with balanced diet and regular exercise."
        elif 25 <= bmi < 30:
            category = "Overweight"
            advice = "Consider increasing physical activity and making healthier food choices."
        else:
            category = "Obesity"
            advice = "Please consult with a healthcare provider for guidance on weight management."

        print(f"Category: {category}")
        print(f"\nHealth Advice: {advice}")

        # Additional information
        print("\n" + "=" * 50)
        print("BMI REFERENCE CHART")
        print("=" * 50)
        print("Underweight: < 18.5")
        print("Normal weight: 18.5 - 24.9")
        print("Overweight: 25 - 29.9")
        print("Obesity: ≥ 30")

        # Fun facts
        print("\n" + "=" * 50)
        print("HEALTH TIPS")
        print("=" * 50)
        print("1. Aim for at least 30 minutes of moderate exercise daily")
        print("2. Include fruits and vegetables in every meal")
        print("3. Stay hydrated by drinking plenty of water")
        print("4. Get 7-9 hours of sleep each night")
        print("5. Manage stress through meditation or hobbies")

    except ValueError:
        print("Error: Please enter valid numbers!")
    except ZeroDivisionError:
        print("Error: Height cannot be zero!")
    except Exception as e:
        print(f"An error occurred: {e}")


def run_all_exercises():
    """Run all Day 2 exercises."""
    print("=" * 60)
    print("Week 1, Day 2: Basic Data Types & Operations")
    print("=" * 60)

    print("\n--- Exercise 1: Numeric Operations ---")
    exercise_1_numeric_operations()

    print("\n--- Exercise 2: String Formatting ---")
    exercise_2_string_formatting()

    print("\n--- Exercise 3: Boolean Operations ---")
    exercise_3_boolean_operations()

    print("\n--- Exercise 4: Type Checking ---")
    exercise_4_type_checking()

    print("\n" + "=" * 60)
    print("Mini Project: BMI Calculator")
    print("=" * 60)
    mini_project_bmi_calculator()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 2 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Run {func_name}")
        globals()[func_name]()
    else:
        print("Run em all")
        # This runs when you execute the file directly
        run_all_exercises()
