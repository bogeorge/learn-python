import json
import sys

"""
Week 3, Day 20: Review & Project Day

Review of OOP concepts and preparation for the Library Management System project.
"""


def review_exercise_1_classes_objects():
    """Review: Classes and Objects."""
    print("Review: Classes and Objects")
    print("-" * 40)

    class Book:
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn
            self.is_checked_out = False

        def check_out(self):
            if not self.is_checked_out:
                self.is_checked_out = True
                return True
            return False

        def return_book(self):
            if self.is_checked_out:
                self.is_checked_out = False
                return True
            return False

        def __str__(self):
            status = "Checked Out" if self.is_checked_out else "Available"
            return f"'{self.title}' by {self.author} ({status})"

    # Create objects
    book1 = Book("Python Programming", "John Doe", "123-456789")
    book2 = Book("Data Science Basics", "Jane Smith", "987-654321")

    print("Created books:")
    print(f"  1. {book1}")
    print(f"  2. {book2}")

    # Use methods
    print(f"\nChecking out book1: {book1.check_out()}")
    print(f"Checking out book1 again: {book1.check_out()}")
    print("\nCurrent status:")
    print(f"  {book1}")
    print(f"  {book2}")

    print(f"\nReturning book1: {book1.return_book()}")
    print(f"After return: {book1}")


def review_exercise_2_inheritance():
    """Review: Inheritance."""
    print("\n\nReview: Inheritance")
    print("-" * 40)

    class Vehicle:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
            self.speed = 0

        def accelerate(self, amount):
            self.speed += amount
            return f"Accelerated to {self.speed} km/h"

        def brake(self, amount):
            self.speed = max(0, self.speed - amount)
            return f"Slowed to {self.speed} km/h"

    class Car(Vehicle):
        def __init__(self, make, model, year, doors):
            super().__init__(make, model, year)
            self.doors = doors

        def honk(self):
            return "Beep beep!"

    class Truck(Vehicle):
        def __init__(self, make, model, year, cargo_capacity):
            super().__init__(make, model, year)
            self.cargo_capacity = cargo_capacity
            self.cargo = 0

        def load(self, weight):
            if self.cargo + weight <= self.cargo_capacity:
                self.cargo += weight
                return (
                    f"Loaded {weight} tons. Total: {self.cargo}/{self.cargo_capacity}"
                )
            return f"Cannot load {weight} tons. Capacity exceeded."

    # Create vehicles
    car = Car("Toyota", "Camry", 2020, 4)
    truck = Truck("Ford", "F-150", 2019, 2.5)

    print("Created vehicles:")
    print(f"  Car: {car.year} {car.make} {car.model}")
    print(f"  Truck: {truck.year} {truck.make} {truck.model}")

    # Demonstrate inheritance
    print("\nCommon methods (inherited):")
    print(f"  Car: {car.accelerate(50)}")
    print(f"  Truck: {truck.accelerate(40)}")

    print("\nUnique methods:")
    print(f"  Car: {car.honk()}")
    print(f"  Truck: {truck.load(1.5)}")


def review_exercise_3_polymorphism_encapsulation():
    """Review: Polymorphism and Encapsulation."""
    print("\n\nReview: Polymorphism and Encapsulation")
    print("-" * 40)

    class BankAccount:
        def __init__(self, account_number, balance):
            self.account_number = account_number
            self._balance = balance  # Protected
            self.__transactions = []  # Private

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount
                self.__transactions.append(f"Deposit: +${amount}")
                return True
            return False

        def withdraw(self, amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
                self.__transactions.append(f"Withdrawal: -${amount}")
                return True
            return False

        @property
        def balance(self):
            return self._balance

        def get_transactions(self):
            return self.__transactions.copy()

    # Polymorphism example
    class PaymentMethod:
        def process_payment(self, amount):
            raise NotImplementedError

    class CreditCard(PaymentMethod):
        def process_payment(self, amount):
            return f"Processing ${amount} via credit card"

    class PayPal(PaymentMethod):
        def process_payment(self, amount):
            return f"Processing ${amount} via PayPal"

    # Encapsulation
    account = BankAccount("ACC123", 1000)
    print(f"Account created with balance: ${account.balance}")

    account.deposit(500)
    account.withdraw(200)
    print(f"After transactions: ${account.balance}")
    print(f"Transactions: {account.get_transactions()}")

    # Polymorphism
    payments = [CreditCard(), PayPal()]
    for payment in payments:
        print(f"  {payment.process_payment(100)}")


def review_exercise_4_special_methods_error_handling():
    """Review: Special Methods and Error Handling."""
    print("\n\nReview: Special Methods and Error Handling")
    print("-" * 40)

    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __str__(self):
            return f"Vector({self.x}, {self.y})"

        def __len__(self):
            return 2  # Always 2D vector

        def magnitude(self):
            return (self.x**2 + self.y**2) ** 0.5

    # Special methods
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = v1 + v2

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v3}")
    print(f"Magnitude of v1: {v1.magnitude():.2f}")
    print(f"Length of vector (dimensions): {len(v1)}")

    # Error handling
    print("\nError handling example:")

    def safe_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"
        except TypeError:
            return "Invalid input types"

    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print(f"10 / 'a' = {safe_divide(10, 'a')}")


def review_exercise_5_modules_packages():
    """Review: Modules and Packages."""
    print("\n\nReview: Modules and Packages")
    print("-" * 40)

    print("Key concepts:")
    print("  1. Modules are .py files containing Python code")
    print("  2. Packages are directories with __init__.py")
    print("  3. Use import to access modules")
    print("  4. Use from ... import for specific items")
    print("  5. __name__ == '__main__' for executable code")

    # Demonstrate with built-in modules
    import math
    from datetime import date

    print("\nUsing math module:")
    print(f"  math.sqrt(25) = {math.sqrt(25)}")
    print(f"  math.pi = {math.pi:.5f}")

    print("\nUsing datetime module:")
    today = date.today()
    print(f"  Today's date: {today}")
    print(f"  Year: {today.year}, Month: {today.month}, Day: {today.day}")


def project_preparation_library_management():
    """
    Preparation for Library Management System project.

    This exercise walks through the design and planning of the project.
    """
    print("\n" + "=" * 60)
    print("PROJECT PREPARATION: LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)

    print("\nProject Requirements:")
    print("  1. Book and Member classes")
    print("  2. Borrowing/returning system")
    print("  3. Search functionality")
    print("  4. Data persistence")

    print("\nClass Design:")
    print("  class Book:")
    print("    - title, author, isbn, year")
    print("    - is_available, borrowed_by, due_date")
    print("    - check_out(member), return_book()")

    print("\n  class Member:")
    print("    - name, member_id, email")
    print("    - borrowed_books, membership_date")
    print("    - borrow_limit, fines")

    print("\n  class Library:")
    print("    - books: dict[isbn -> Book]")
    print("    - members: dict[member_id -> Member]")
    print("    - add_book(), remove_book()")
    print("    - register_member(), remove_member()")
    print("    - search_books(), search_members()")
    print("    - save_to_file(), load_from_file()")

    print("\nFeatures to implement:")
    print("  1. Add/remove/view books and members")
    print("  2. Check out and return books")
    print("  3. Search by title, author, or ISBN")
    print("  4. Track due dates and calculate fines")
    print("  5. Save data to JSON file")
    print("  6. Generate reports")

    print("\nData Persistence Strategy:")
    print("  Use JSON format for simplicity:")
    print("  - books.json: List of book dictionaries")
    print("  - members.json: List of member dictionaries")
    print("  - transactions.json: Record of all transactions")

    print("\nExample JSON structure:")
    book_example = {
        "title": "Python Programming",
        "author": "John Doe",
        "isbn": "123-456789",
        "year": 2020,
        "is_available": True,
        "borrowed_by": None,
        "due_date": None,
    }

    print(f"  Book: {json.dumps(book_example, indent=2)}")

    print("\nImplementation Steps:")
    print("  1. Create Book class with basic attributes")
    print("  2. Create Member class with borrowing logic")
    print("  3. Create Library class to manage collections")
    print("  4. Add data persistence with JSON")
    print("  5. Implement search functionality")
    print("  6. Add user interface (CLI menu)")
    print("  7. Test thoroughly")

    print("\nTesting Strategy:")
    print("  1. Unit tests for each class method")
    print("  2. Integration tests for borrowing/returning")
    print("  3. Test data persistence (save/load)")
    print("  4. Test edge cases (overdue, limits, etc.)")

    print("\nStretch Goals:")
    print("  1. Add email notifications for due dates")
    print("  2. Implement waitlists for popular books")
    print("  3. Add book recommendations")
    print("  4. Create a web interface")
    print("  5. Add multiple library branches")


def run_all_exercises():
    """Run all Day 20 review exercises."""
    print("=" * 60)
    print("Week 3, Day 20: Review & Project Day")
    print("=" * 60)

    print("\nThis day reviews OOP concepts and prepares for the")
    print("Library Management System project.")
    print("\nRunning review exercises...")

    review_exercise_1_classes_objects()
    review_exercise_2_inheritance()
    review_exercise_3_polymorphism_encapsulation()
    review_exercise_4_special_methods_error_handling()
    review_exercise_5_modules_packages()

    print("\n" + "=" * 60)
    print("Project Preparation")
    print("=" * 60)
    project_preparation_library_management()

    print("\n" + "=" * 60)
    print("Next Steps:")
    print("  1. Review the project preparation above")
    print("  2. Create the library_management.py file")
    print("  3. Implement the Library Management System")
    print("  4. Test all functionality")
    print("  5. Consider adding stretch goals")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
