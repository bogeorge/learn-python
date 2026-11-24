import sys

"""
Week 2, Day 9: Advanced Functions

Exercises to practice default parameters, variable scope, lambda functions, 
and sorting/filtering with lambdas.
"""


def exercise_1_default_parameters():
    """
    Practice with default parameters.

    1. Create a function with default parameter values
    2. Create a function where some parameters have defaults and others don't
    3. Demonstrate calling functions with and without arguments
    """

    def greet(name, greeting="Hello"):
        """Greet someone with optional custom greeting."""
        return f"{greeting}, {name}!"

    def create_profile(name, age, country="USA", occupation="Student"):
        """Create a user profile with optional country and occupation."""
        return {"name": name, "age": age, "country": country, "occupation": occupation}

    def order_food(item, quantity=1, sauce="none", extra_cheese=False):
        """Order food with various optional parameters."""
        order = f"{quantity} x {item}"
        if sauce != "none":
            order += f" with {sauce} sauce"
        if extra_cheese:
            order += " (extra cheese)"
        return order

    print("Default parameters practice:")
    print(f"  greet('Alice'): {greet('Alice')}")
    print(f"  greet('Bob', 'Hi'): {greet('Bob', 'Hi')}")

    print(f"\n  Default profile: {create_profile('Charlie', 25)}")
    print(f"  Custom profile: {create_profile('Diana', 30, 'Canada', 'Engineer')}")

    print(f"\n  Basic order: {order_food('Pizza')}")
    print(f"  Custom order: {order_food('Burger', 2, 'BBQ', True)}")


def exercise_2_variable_scope():
    """
    Demonstrate variable scope (global vs local).

    1. Show how variables behave in different scopes
    2. Demonstrate the `global` keyword
    3. Show nested function scope
    """

    # Global variable
    global_counter = 0

    def increment_local():
        """Create a local variable (doesn't affect global)."""
        local_counter = 0
        local_counter += 1
        return local_counter

    def increment_global():
        """Modify global variable using global keyword."""
        global global_counter
        global_counter += 1
        return global_counter

    def outer_function():
        """Demonstrate nested function scope."""
        outer_var = "I'm in outer function"

        def inner_function():
            """Access outer function's variable."""
            nonlocal outer_var
            outer_var = "Modified by inner function"
            return outer_var

        print(f"  Before inner: {outer_var}")
        result = inner_function()
        print(f"  After inner: {result}")

    print("\nVariable scope demonstration:")

    print("  Local scope:")
    for _ in range(3):
        print(f"    Local counter: {increment_local()}")

    print("\n  Global scope:")
    for _ in range(3):
        print(f"    Global counter: {increment_global()}")

    print("\n  Nested function scope:")
    outer_function()


def exercise_3_lambda_functions():
    """
    Practice with lambda (anonymous) functions.

    1. Create simple lambda functions
    2. Use lambdas with map(), filter(), sorted()
    3. Store lambdas in variables
    """

    # Basic lambda functions
    square = lambda x: x**2
    is_even = lambda x: x % 2 == 0
    get_length = lambda s: len(s)

    print("Basic lambda functions:")
    print(f"  square(5) = {square(5)}")
    print(f"  is_even(7) = {is_even(7)}")
    print(f"  get_length('Python') = {get_length('Python')}")

    # Lambda with multiple parameters
    calculate = lambda a, b, op: {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else "undefined",
    }[op]

    print(f"\n  calculate(10, 5, 'add') = {calculate(10, 5, 'add')}")
    print(f"  calculate(10, 5, 'mul') = {calculate(10, 5, 'mul')}")

    # Lambda in list comprehensions
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squared_numbers = list(map(lambda x: x**2, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(f"\n  Original numbers: {numbers}")
    print(f"  Squared numbers: {squared_numbers}")
    print(f"  Even numbers: {even_numbers}")


def exercise_4_sorting_with_lambdas():
    """
    Sort and filter data using lambda functions.

    1. Sort lists of various data types
    2. Sort by custom criteria
    3. Use lambda with sorted() and list.sort()
    """

    # List of numbers
    numbers = [42, 17, 89, 3, 56, 24, 91, 8]

    print("Sorting with lambdas:")
    print(f"  Original numbers: {numbers}")

    # Sort by last digit
    sorted_by_last_digit = sorted(numbers, key=lambda x: x % 10)
    print(f"  Sorted by last digit: {sorted_by_last_digit}")

    # List of tuples (name, age)
    people = [("Alice", 28), ("Bob", 35), ("Charlie", 22), ("Diana", 30)]

    print(f"\n  Original people: {people}")

    # Sort by age
    sorted_by_age = sorted(people, key=lambda p: p[1])
    print(f"  Sorted by age: {sorted_by_age}")

    # Sort by name length
    sorted_by_name_length = sorted(people, key=lambda p: len(p[0]))
    print(f"  Sorted by name length: {sorted_by_name_length}")

    # List of dictionaries
    products = [
        {"name": "Laptop", "price": 999.99, "stock": 5},
        {"name": "Mouse", "price": 25.50, "stock": 42},
        {"name": "Keyboard", "price": 79.99, "stock": 15},
        {"name": "Monitor", "price": 299.99, "stock": 8},
    ]

    print(f"\n  Original products: {products}")

    # Sort by price
    sorted_by_price = sorted(products, key=lambda p: p["price"])
    print(f"  Sorted by price: {sorted_by_price}")

    # Sort by value (price * stock)
    sorted_by_value = sorted(products, key=lambda p: p["price"] * p["stock"])
    print(f"  Sorted by total value: {sorted_by_value}")


def exercise_5_advanced_lambda_usage():
    """
    More advanced lambda function usage.

    1. Create higher-order functions with lambdas
    2. Use lambdas with reduce()
    3. Create function factories with lambdas
    """
    from functools import reduce

    # Using reduce() with lambda
    numbers = [1, 2, 3, 4, 5]

    sum_result = reduce(lambda x, y: x + y, numbers)
    product_result = reduce(lambda x, y: x * y, numbers)
    max_result = reduce(lambda x, y: x if x > y else y, numbers)

    print("Advanced lambda usage:")
    print(f"  Numbers: {numbers}")
    print(f"  Sum (reduce): {sum_result}")
    print(f"  Product (reduce): {product_result}")
    print(f"  Max (reduce): {max_result}")

    # Function factory using lambda
    def multiplier_factory(n):
        """Return a function that multiplies by n."""
        return lambda x: x * n

    double = multiplier_factory(2)
    triple = multiplier_factory(3)
    times_ten = multiplier_factory(10)

    print(f"\n  Function factory:")
    print(f"    double(5) = {double(5)}")
    print(f"    triple(5) = {triple(5)}")
    print(f"    times_ten(5) = {times_ten(5)}")

    # Currying with lambda
    def curry_add(a):
        """Curry addition function."""
        return lambda b: a + b

    add_five = curry_add(5)
    add_ten = curry_add(10)

    print(f"\n  Curried functions:")
    print(f"    add_five(3) = {add_five(3)}")
    print(f"    add_ten(7) = {add_ten(7)}")


def mini_project_math_operations_library():
    """
    Math Operations Library

    Create a library of mathematical operations using various function techniques.

    Features:
    1. Collection of math functions (factorial, fibonacci, etc.)
    2. Function composition and chaining
    3. Use of lambda functions for operations
    """
    import math

    print("=" * 50)
    print("MATH OPERATIONS LIBRARY")
    print("=" * 50)

    # Basic math operations using lambda
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "undefined",
        "power": lambda x, y: x**y,
        "modulo": lambda x, y: x % y if y != 0 else "undefined",
    }

    # Special math functions
    def factorial(n):
        """Calculate factorial recursively."""
        return 1 if n <= 1 else n * factorial(n - 1)

    def fibonacci(n):
        """Generate first n Fibonacci numbers."""
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]

    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    # Function composition
    def compose(f, g):
        """Compose two functions: f(g(x))."""
        return lambda x: f(g(x))

    # Create some composed functions
    square_then_double = compose(lambda x: x * 2, lambda x: x**2)
    add_five_then_square = compose(lambda x: x**2, lambda x: x + 5)

    print("\nAvailable operations:")
    print("1. Basic arithmetic (+, -, *, /, ^, %)")
    print("2. Factorial")
    print("3. Fibonacci sequence")
    print("4. Prime checking")
    print("5. Function composition")
    print("0. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (0-5): ")

            if choice == "0":
                print("Exiting Math Library. Goodbye!")
                break

            elif choice == "1":
                print("\nBasic Arithmetic Operations:")
                for op_name in operations:
                    print(f"  {op_name}")

                op = input("Choose operation: ")
                if op in operations:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    result = operations[op](x, y)
                    print(f"{x} {op} {y} = {result}")
                else:
                    print(f"Unknown operation: {op}")

            elif choice == "2":
                n = int(input("Enter a number for factorial: "))
                if n < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    result = factorial(n)
                    print(f"{n}! = {result}")

            elif choice == "3":
                n = int(input("How many Fibonacci numbers? "))
                fib_seq = fibonacci(n)
                print(f"First {n} Fibonacci numbers: {fib_seq}")

            elif choice == "4":
                n = int(input("Enter a number to check if prime: "))
                result = "prime" if is_prime(n) else "not prime"
                print(f"{n} is {result}")

            elif choice == "5":
                print("\nFunction Composition Examples:")
                test_value = float(input("Enter a test value: "))

                print(f"\nFor x = {test_value}:")
                print(f"  square_then_double(x) = {square_then_double(test_value)}")
                print(f"  add_five_then_square(x) = {add_five_then_square(test_value)}")

            else:
                print("Invalid choice. Please enter 0-5.")

        except ValueError:
            print("Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break


def run_all_exercises():
    """Run all Day 9 exercises."""
    print("=" * 60)
    print("Week 2, Day 9: Advanced Functions")
    print("=" * 60)

    print("\n--- Exercise 1: Default Parameters ---")
    exercise_1_default_parameters()

    print("\n--- Exercise 2: Variable Scope ---")
    exercise_2_variable_scope()

    print("\n--- Exercise 3: Lambda Functions ---")
    exercise_3_lambda_functions()

    print("\n--- Exercise 4: Sorting with Lambdas ---")
    exercise_4_sorting_with_lambdas()

    print("\n--- Exercise 5: Advanced Lambda Usage ---")
    exercise_5_advanced_lambda_usage()

    print("\n" + "=" * 60)
    print("Mini Project: Math Operations Library")
    print("=" * 60)
    mini_project_math_operations_library()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 9 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
