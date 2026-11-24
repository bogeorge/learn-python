import sys
import json
from datetime import datetime

"""
Week 3, Day 18: Special Methods & Error Handling

Exercises to practice special methods (__init__, __str__, __repr__, etc.),
try/except/finally blocks, raising exceptions, and creating custom exceptions.
"""


def exercise_1_special_methods():
    """
    Practice special methods (dunder methods).

    1. Implement __str__, __repr__, __len__, __add__, __eq__
    2. Create a class that behaves like a built-in type
    """

    class ShoppingCart:
        """Shopping cart with special methods."""

        def __init__(self):
            self.items = []
            self.prices = []

        def add_item(self, name, price):
            """Add item to cart."""
            self.items.append(name)
            self.prices.append(price)

        def remove_item(self, name):
            """Remove item from cart."""
            if name in self.items:
                index = self.items.index(name)
                self.items.pop(index)
                price = self.prices.pop(index)
                return price
            return 0

        def __len__(self):
            """Return number of items in cart."""
            return len(self.items)

        def __str__(self):
            """User-friendly string representation."""
            if not self.items:
                return "Shopping cart is empty"

            cart_str = "Shopping Cart:\n"
            for i, (item, price) in enumerate(zip(self.items, self.prices), 1):
                cart_str += f"  {i}. {item}: ${price:.2f}\n"
            cart_str += f"Total: ${sum(self.prices):.2f}"
            return cart_str

        def __repr__(self):
            """Developer-friendly string representation."""
            return f"ShoppingCart(items={self.items}, prices={self.prices})"

        def __add__(self, other):
            """Combine two shopping carts."""
            if not isinstance(other, ShoppingCart):
                raise TypeError("Can only add ShoppingCart objects")

            new_cart = ShoppingCart()
            new_cart.items = self.items + other.items
            new_cart.prices = self.prices + other.prices
            return new_cart

        def __eq__(self, other):
            """Check if two carts have same items and prices."""
            if not isinstance(other, ShoppingCart):
                return False
            return self.items == other.items and self.prices == other.prices

        def __getitem__(self, index):
            """Get item by index."""
            if isinstance(index, slice):
                return list(zip(self.items[index], self.prices[index]))
            return (self.items[index], self.prices[index])

        def __iter__(self):
            """Make cart iterable."""
            return iter(zip(self.items, self.prices))

    print("Special methods example - Shopping Cart:")

    # Create carts
    cart1 = ShoppingCart()
    cart1.add_item("Apple", 1.99)
    cart1.add_item("Banana", 0.99)
    cart1.add_item("Milk", 3.49)

    cart2 = ShoppingCart()
    cart2.add_item("Bread", 2.49)
    cart2.add_item("Eggs", 3.99)

    print(f"\n  cart1:\n{str(cart1)}")
    print(f"\n  cart2:\n{str(cart2)}")

    # Test special methods
    print(f"\n  Special methods demonstration:")
    print(f"    len(cart1): {len(cart1)}")
    print(f"    cart1[1]: {cart1[1]}")
    print(f"    cart1[0:2]: {cart1[0:2]}")

    # Test addition
    combined = cart1 + cart2
    print(f"\n  cart1 + cart2:")
    print(f"    Items: {len(combined)}")
    print(f"    Total: ${sum(combined.prices):.2f}")

    # Test iteration
    print(f"\n  Iterating through cart1:")
    for item, price in cart1:
        print(f"    {item}: ${price:.2f}")

    # Test equality
    cart3 = ShoppingCart()
    cart3.add_item("Apple", 1.99)
    cart3.add_item("Banana", 0.99)
    cart3.add_item("Milk", 3.49)

    print(f"\n  Equality test:")
    print(f"    cart1 == cart2: {cart1 == cart2}")
    print(f"    cart1 == cart3: {cart1 == cart3}")


def exercise_2_basic_error_handling():
    """
    Practice basic error handling with try/except/finally.

    1. Handle different types of exceptions
    2. Use try/except/else/finally blocks
    3. Handle multiple exceptions
    """

    def safe_divide(a, b):
        """Divide two numbers with error handling."""
        try:
            result = a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
        except TypeError:
            return "Error: Both arguments must be numbers"
        else:
            return f"{a} / {b} = {result}"
        finally:
            print("  Division operation attempted")

    def get_list_element(lst, index):
        """Get element from list with error handling."""
        try:
            value = lst[index]
        except IndexError:
            return f"Error: Index {index} out of range (list has {len(lst)} elements)"
        except TypeError:
            return "Error: Index must be an integer"
        else:
            return f"Element at index {index}: {value}"

    def convert_to_int(value):
        """Convert value to integer with error handling."""
        try:
            result = int(value)
        except ValueError:
            return f"Error: Cannot convert '{value}' to integer"
        except TypeError:
            return f"Error: Cannot convert type {type(value).__name__} to integer"
        else:
            return f"Successfully converted to integer: {result}"

    print("\nBasic error handling:")

    # Division examples
    print("\n  Division examples:")
    print(f"    {safe_divide(10, 2)}")
    print(f"    {safe_divide(10, 0)}")
    print(f"    {safe_divide(10, 'a')}")

    # List examples
    print("\n  List examples:")
    my_list = [10, 20, 30, 40, 50]
    print(f"    {get_list_element(my_list, 2)}")
    print(f"    {get_list_element(my_list, 10)}")
    print(f"    {get_list_element(my_list, 'two')}")

    # Conversion examples
    print("\n  Conversion examples:")
    print(f"    {convert_to_int('123')}")
    print(f"    {convert_to_int('abc')}")
    print(f"    {convert_to_int([1, 2, 3])}")

    # Multiple exceptions in one block
    print("\n  Multiple exceptions:")

    def process_value(value):
        try:
            result = int(value)
            reciprocal = 1 / result
        except ValueError, TypeError:
            return "Error: Invalid value for conversion"
        except ZeroDivisionError:
            return "Error: Cannot calculate reciprocal of zero"
        else:
            return f"Value: {result}, Reciprocal: {reciprocal}"

    print(f"    {process_value('100')}")
    print(f"    {process_value('0')}")
    print(f"    {process_value('abc')}")


def exercise_3_raising_exceptions():
    """
    Practice raising exceptions.

    1. Raise built-in exceptions
    2. Raise exceptions with custom messages
    3. Use assert statements
    """

    def validate_age(age):
        """Validate age, raising exceptions for invalid values."""
        if not isinstance(age, (int, float)):
            raise TypeError("Age must be a number")

        if age < 0:
            raise ValueError("Age cannot be negative")

        if age > 150:
            raise ValueError("Age is unrealistically high")

        return f"Valid age: {age}"

    def validate_password(password):
        """Validate password strength."""
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not any(c.isupper() for c in password):
            raise ValueError("Password must contain at least one uppercase letter")

        if not any(c.isdigit() for c in password):
            raise ValueError("Password must contain at least one digit")

        return "Password is strong"

    def calculate_bmi(weight_kg, height_m):
        """Calculate BMI with validation."""
        # Using assert for development checks
        assert weight_kg > 0, "Weight must be positive"
        assert height_m > 0, "Height must be positive"

        bmi = weight_kg / (height_m**2)

        if bmi < 15:
            raise ValueError("BMI indicates very severely underweight")
        elif bmi > 40:
            raise ValueError("BMI indicates very severely obese")

        return f"BMI: {bmi:.1f}"

    print("\nRaising exceptions:")

    # Age validation
    print("\n  Age validation:")
    test_ages = [25, -5, 200, "twenty"]

    for age in test_ages:
        try:
            result = validate_age(age)
            print(f"    {age}: {result}")
        except (TypeError, ValueError) as e:
            print(f"    {age}: Error - {e}")

    # Password validation
    print("\n  Password validation:")
    passwords = ["short", "nouppercase1", "NoDigits", "StrongPass123"]

    for pwd in passwords:
        try:
            result = validate_password(pwd)
            print(f"    '{pwd}': {result}")
        except ValueError as e:
            print(f"    '{pwd}': Error - {e}")

    # BMI calculation
    print("\n  BMI calculation:")
    test_cases = [
        (70, 1.75),  # Normal
        (50, 1.75),  # Underweight
        (120, 1.75),  # Obese
        (-10, 1.75),  # Invalid weight
        (70, 0),  # Invalid height
    ]

    for weight, height in test_cases:
        try:
            result = calculate_bmi(weight, height)
            print(f"    Weight={weight}kg, Height={height}m: {result}")
        except (AssertionError, ValueError) as e:
            print(f"    Weight={weight}kg, Height={height}m: Error - {e}")


def exercise_4_custom_exceptions():
    """
    Create and use custom exceptions.

    1. Define custom exception classes
    2. Use inheritance for exception hierarchy
    3. Add custom attributes to exceptions
    """

    # Custom exception hierarchy
    class BankError(Exception):
        """Base class for all bank-related errors."""

        pass

    class InsufficientFundsError(BankError):
        """Raised when account has insufficient funds."""

        def __init__(self, balance, amount):
            self.balance = balance
            self.amount = amount
            message = (
                f"Insufficient funds: "
                f"Balance ${balance:.2f}, "
                f"Attempted to withdraw ${amount:.2f}"
            )
            super().__init__(message)

    class InvalidAccountError(BankError):
        """Raised when account is invalid."""

        pass

    class TransactionLimitError(BankError):
        """Raised when transaction limit is exceeded."""

        def __init__(self, limit, attempted):
            self.limit = limit
            self.attempted = attempted
            message = (
                f"Transaction limit exceeded: "
                f"Limit ${limit:.2f}, "
                f"Attempted ${attempted:.2f}"
            )
            super().__init__(message)

    # Custom exceptions for inventory system
    class InventoryError(Exception):
        """Base class for inventory errors."""

        pass

    class OutOfStockError(InventoryError):
        """Raised when item is out of stock."""

        def __init__(self, item_name, requested, available):
            self.item_name = item_name
            self.requested = requested
            self.available = available
            message = (
                f"Out of stock: {item_name} - "
                f"Requested {requested}, "
                f"Available {available}"
            )
            super().__init__(message)

    class InvalidItemError(InventoryError):
        """Raised when item is not found in inventory."""

        pass

    class NegativeQuantityError(InventoryError):
        """Raised when quantity is negative."""

        pass

    # Bank system using custom exceptions
    class BankAccount:
        """Bank account with custom exception handling."""

        def __init__(self, account_number, balance, daily_limit=1000):
            self.account_number = account_number
            self.balance = balance
            self.daily_limit = daily_limit
            self.daily_withdrawn = 0

        def withdraw(self, amount):
            """Withdraw money with custom exception handling."""
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")

            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)

            if self.daily_withdrawn + amount > self.daily_limit:
                raise TransactionLimitError(
                    self.daily_limit, self.daily_withdrawn + amount
                )

            self.balance -= amount
            self.daily_withdrawn += amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

        def reset_daily_limit(self):
            """Reset daily withdrawal counter."""
            self.daily_withdrawn = 0

    # Inventory system using custom exceptions
    class Inventory:
        """Inventory system with custom exception handling."""

        def __init__(self):
            self.items = {}

        def add_item(self, name, quantity):
            """Add item to inventory."""
            if quantity < 0:
                raise NegativeQuantityError(f"Cannot add negative quantity: {quantity}")

            if name in self.items:
                self.items[name] += quantity
            else:
                self.items[name] = quantity

        def remove_item(self, name, quantity):
            """Remove item from inventory."""
            if quantity < 0:
                raise NegativeQuantityError(
                    f"Cannot remove negative quantity: {quantity}"
                )

            if name not in self.items:
                raise InvalidItemError(f"Item not found: {name}")

            if self.items[name] < quantity:
                raise OutOfStockError(name, quantity, self.items[name])

            self.items[name] -= quantity
            return f"Removed {quantity} of {name}. Remaining: {self.items[name]}"

        def get_stock(self, name):
            """Get stock level for item."""
            if name not in self.items:
                raise InvalidItemError(f"Item not found: {name}")
            return self.items[name]

    print("\nCustom exceptions:")

    # Bank account examples
    print("\n  Bank account with custom exceptions:")
    account = BankAccount("ACC123", 500.00, daily_limit=300)

    test_withdrawals = [100, 250, 100, 200]

    for amount in test_withdrawals:
        try:
            result = account.withdraw(amount)
            print(f"    Withdraw ${amount:.2f}: {result}")
        except BankError as e:
            print(f"    Withdraw ${amount:.2f}: {e.__class__.__name__} - {e}")
        except ValueError as e:
            print(f"    Withdraw ${amount:.2f}: ValueError - {e}")

    # Inventory examples
    print("\n  Inventory system with custom exceptions:")
    inventory = Inventory()
    inventory.add_item("Widget", 10)
    inventory.add_item("Gadget", 5)

    operations = [
        ("remove", "Widget", 3),
        ("remove", "Widget", 10),
        ("remove", "Nonexistent", 1),
        ("remove", "Gadget", -2),
        ("add", "Gadget", -5),
    ]

    for action, item, quantity in operations:
        try:
            if action == "remove":
                result = inventory.remove_item(item, quantity)
                print(f"    Remove {quantity} {item}: {result}")
            elif action == "add":
                result = inventory.add_item(item, quantity)
                print(f"    Add {quantity} {item}: Success")
        except InventoryError as e:
            print(
                f"    {action.capitalize()} {quantity} {item}: {e.__class__.__name__} - {e}"
            )


def exercise_5_context_managers():
    """
    Practice with context managers (with statement).

    1. Use built-in context managers
    2. Create custom context managers using classes
    3. Create custom context managers using @contextmanager
    """
    from contextlib import contextmanager

    # Custom context manager class
    class Timer:
        """Context manager for timing code execution."""

        def __init__(self, name="Operation"):
            self.name = name

        def __enter__(self):
            import time

            self.start_time = time.time()
            print(f"Starting {self.name}...")
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            import time

            elapsed = time.time() - self.start_time
            print(f"{self.name} completed in {elapsed:.3f} seconds")
            if exc_type:
                print(f"{self.name} failed with {exc_type.__name__}: {exc_val}")
            return False  # Don't suppress exceptions

    class FileHandler:
        """Custom context manager for file operations."""

        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None

        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
            if exc_type:
                print(f"Error occurred while handling {self.filename}: {exc_val}")
            return False  # Don't suppress exceptions

    # Context manager using @contextmanager decorator
    @contextmanager
    def temporary_change(obj, attr, new_value):
        """Temporarily change an attribute, then restore it."""
        original_value = getattr(obj, attr)
        setattr(obj, attr, new_value)
        try:
            yield
        finally:
            setattr(obj, attr, original_value)

    @contextmanager
    def suppress_exception(exception_type):
        """Suppress specified exception types."""
        try:
            yield
        except exception_type:
            pass  # Suppress the exception

    print("\nContext managers:")

    # Using Timer context manager
    print("\n  Timer context manager:")
    with Timer("List comprehension"):
        squares = [x**2 for x in range(10000)]

    # Using FileHandler context manager
    print("\n  FileHandler context manager:")
    try:
        with FileHandler("test_output.txt", "w") as f:
            f.write("Hello, world!\n")
            f.write("This is a test file.\n")
        print("    File written successfully")
    except Exception as e:
        print(f"    Error: {e}")

    # Read back the file
    try:
        with FileHandler("test_output.txt", "r") as f:
            content = f.read()
        print(f"    File content:\n{content}")
    except FileNotFoundError:
        print("    File not found")

    # Using temporary_change context manager
    print("\n  temporary_change context manager:")

    class Config:
        debug_mode = False

    config = Config()
    print(f"    Original debug_mode: {config.debug_mode}")

    with temporary_change(config, "debug_mode", True):
        print(f"    Inside context: debug_mode = {config.debug_mode}")

    print(f"    After context: debug_mode = {config.debug_mode}")

    # Using suppress_exception context manager
    print("\n  suppress_exception context manager:")

    # This will be suppressed
    with suppress_exception(ZeroDivisionError):
        result = 10 / 0
        print("    This won't print")
    print("    ZeroDivisionError was suppressed")

    # This will NOT be suppressed (different exception type)
    try:
        with suppress_exception(ValueError):
            result = int("not a number")
    except ValueError:
        print("    ValueError was NOT suppressed (wrong exception type)")


def mini_project_calculator_with_error_handling():
    """
    Calculator with Error Handling

    A robust calculator application with comprehensive error handling.

    Features:
    1. Basic arithmetic operations with error handling
    2. Custom exceptions for calculator errors
    3. Input validation and sanitization
    4. Operation history with error tracking
    """

    # Custom exceptions for calculator
    class CalculatorError(Exception):
        """Base class for all calculator errors."""

        pass

    class DivisionByZeroError(CalculatorError):
        """Raised when attempting division by zero."""

        pass

    class InvalidInputError(CalculatorError):
        """Raised when input cannot be converted to number."""

        pass

    class OperationError(CalculatorError):
        """Raised for operation-specific errors."""

        pass

    class Calculator:
        """Calculator with comprehensive error handling."""

        def __init__(self):
            self.history = []
            self.memory = 0

        def _validate_number(self, value):
            """Validate and convert input to number."""
            try:
                return float(value)
            except ValueError, TypeError:
                raise InvalidInputError(f"Invalid number: {value}")

        def add(self, a, b):
            """Add two numbers."""
            try:
                num1 = self._validate_number(a)
                num2 = self._validate_number(b)
                result = num1 + num2
                self.history.append(f"{num1} + {num2} = {result}")
                return result
            except CalculatorError as e:
                self.history.append(f"Error: {a} + {b} -> {e}")
                raise

        def subtract(self, a, b):
            """Subtract b from a."""
            try:
                num1 = self._validate_number(a)
                num2 = self._validate_number(b)
                result = num1 - num2
                self.history.append(f"{num1} - {num2} = {result}")
                return result
            except CalculatorError as e:
                self.history.append(f"Error: {a} - {b} -> {e}")
                raise

        def multiply(self, a, b):
            """Multiply two numbers."""
            try:
                num1 = self._validate_number(a)
                num2 = self._validate_number(b)
                result = num1 * num2
                self.history.append(f"{num1} × {num2} = {result}")
                return result
            except CalculatorError as e:
                self.history.append(f"Error: {a} × {b} -> {e}")
                raise

        def divide(self, a, b):
            """Divide a by b."""
            try:
                num1 = self._validate_number(a)
                num2 = self._validate_number(b)

                if num2 == 0:
                    raise DivisionByZeroError("Cannot divide by zero")

                result = num1 / num2
                self.history.append(f"{num1} ÷ {num2} = {result}")
                return result
            except CalculatorError as e:
                self.history.append(f"Error: {a} ÷ {b} -> {e}")
                raise

        def power(self, a, b):
            """Raise a to the power of b."""
            try:
                num1 = self._validate_number(a)
                num2 = self._validate_number(b)

                # Check for potential overflow
                if abs(num1) > 1000 and abs(num2) > 100:
                    raise OperationError("Operation may cause overflow")

                result = num1**num2
                self.history.append(f"{num1}^{num2} = {result}")
                return result
            except CalculatorError as e:
                self.history.append(f"Error: {a}^{b} -> {e}")
                raise

        def sqrt(self, a):
            """Calculate square root."""
            try:
                num = self._validate_number(a)

                if num < 0:
                    raise OperationError(
                        "Cannot calculate square root of negative number"
                    )

                result = num**0.5
                self.history.append(f"√{num} = {result}")
                return result
            except CalculatorError as e:
                self.history.append(f"Error: √{a} -> {e}")
                raise

        def memory_store(self, value):
            """Store value in memory."""
            try:
                self.memory = self._validate_number(value)
                return f"Memory stored: {self.memory}"
            except CalculatorError as e:
                raise

        def memory_recall(self):
            """Recall value from memory."""
            return self.memory

        def memory_add(self, value):
            """Add value to memory."""
            try:
                num = self._validate_number(value)
                self.memory += num
                return f"Memory updated: {self.memory}"
            except CalculatorError as e:
                raise

        def get_history(self, limit=10):
            """Get calculation history."""
            if not self.history:
                return "No history yet."

            history_str = "Calculation History:\n"
            recent = self.history[-limit:]
            for i, entry in enumerate(recent, 1):
                history_str += f"  {i}. {entry}\n"
            return history_str

        def clear_history(self):
            """Clear calculation history."""
            self.history.clear()
            return "History cleared."

    print("=" * 60)
    print("CALCULATOR WITH ERROR HANDLING")
    print("=" * 60)

    calculator = Calculator()

    def display_menu():
        print("\nOperations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (×)")
        print("4. Divide (÷)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Memory Operations")
        print("8. View History")
        print("9. Clear History")
        print("0. Exit")

    def get_number(prompt):
        """Get validated number from user."""
        while True:
            value = input(prompt)
            if value.lower() == "m":
                return calculator.memory_recall()
            try:
                return float(value)
            except ValueError:
                print("Invalid number. Enter a number or 'm' for memory.")

    print(f"Calculator initialized. Type 'm' to use memory value.")

    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice (0-9): ")

            if choice == "0":
                print("Exiting Calculator. Goodbye!")
                break

            elif choice == "1":  # Add
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calculator.add(a, b)
                print(f"Result: {a} + {b} = {result}")

            elif choice == "2":  # Subtract
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calculator.subtract(a, b)
                print(f"Result: {a} - {b} = {result}")

            elif choice == "3":  # Multiply
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calculator.multiply(a, b)
                print(f"Result: {a} × {b} = {result}")

            elif choice == "4":  # Divide
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calculator.divide(a, b)
                print(f"Result: {a} ÷ {b} = {result}")

            elif choice == "5":  # Power
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                result = calculator.power(a, b)
                print(f"Result: {a}^{b} = {result}")

            elif choice == "6":  # Square Root
                a = get_number("Enter number: ")
                result = calculator.sqrt(a)
                print(f"Result: √{a} = {result}")

            elif choice == "7":  # Memory Operations
                print("\nMemory Operations:")
                print("  1. Store in memory")
                print("  2. Recall from memory")
                print("  3. Add to memory")

                mem_choice = input("Enter memory operation (1-3): ")

                if mem_choice == "1":
                    value = get_number("Enter value to store: ")
                    print(calculator.memory_store(value))
                elif mem_choice == "2":
                    print(f"Memory value: {calculator.memory_recall()}")
                elif mem_choice == "3":
                    value = get_number("Enter value to add: ")
                    print(calculator.memory_add(value))
                else:
                    print("Invalid memory operation.")

            elif choice == "8":  # View History
                limit = input("Number of history entries to show (default 10): ")
                try:
                    limit = int(limit) if limit.strip() else 10
                    print(calculator.get_history(limit))
                except ValueError:
                    print("Invalid number. Showing 10 entries.")
                    print(calculator.get_history())

            elif choice == "9":  # Clear History
                print(calculator.clear_history())

            else:
                print("Invalid choice. Please enter 0-9.")

        except CalculatorError as e:
            print(f"Calculator Error: {e}")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


def run_all_exercises():
    """Run all Day 18 exercises."""
    print("=" * 60)
    print("Week 3, Day 18: Special Methods & Error Handling")
    print("=" * 60)

    print("\n--- Exercise 1: Special Methods ---")
    exercise_1_special_methods()

    print("\n--- Exercise 2: Basic Error Handling ---")
    exercise_2_basic_error_handling()

    print("\n--- Exercise 3: Raising Exceptions ---")
    exercise_3_raising_exceptions()

    print("\n--- Exercise 4: Custom Exceptions ---")
    exercise_4_custom_exceptions()

    print("\n--- Exercise 5: Context Managers ---")
    exercise_5_context_managers()

    print("\n" + "=" * 60)
    print("Mini Project: Calculator with Error Handling")
    print("=" * 60)
    mini_project_calculator_with_error_handling()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 18 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
