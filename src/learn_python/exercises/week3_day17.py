import sys

"""
Week 3, Day 17: Polymorphism & Encapsulation

Exercises to practice polymorphism (multiple forms of a method),
private attributes, getters/setters, and property decorators.
"""


def exercise_1_polymorphism():
    """
    Demonstrate polymorphism with different payment methods.

    1. Create base Payment class with pay() method
    2. Create derived classes with different implementations
    3. Show polymorphic behavior
    """

    class Payment:
        """Base class for all payment methods."""

        def pay(self, amount):
            """Process payment - to be implemented by subclasses."""
            raise NotImplementedError("Subclasses must implement pay()")

        def get_receipt(self):
            """Get payment receipt."""
            return "Payment receipt"

    class CreditCardPayment(Payment):
        """Credit card payment implementation."""

        def __init__(self, card_number, expiry_date, cvv):
            self.card_number = card_number
            self.expiry_date = expiry_date
            self.cvv = cvv

        def pay(self, amount):
            """Process credit card payment."""
            # Mask card number for security
            masked_card = f"****-****-****-{self.card_number[-4:]}"
            return (
                f"Processing credit card payment of ${amount:.2f} "
                f"using card {masked_card}"
            )

    class PayPalPayment(Payment):
        """PayPal payment implementation."""

        def __init__(self, email):
            self.email = email

        def pay(self, amount):
            """Process PayPal payment."""
            return (
                f"Processing PayPal payment of ${amount:.2f} for account {self.email}"
            )

    class BankTransferPayment(Payment):
        """Bank transfer payment implementation."""

        def __init__(self, account_number, routing_number):
            self.account_number = account_number
            self.routing_number = routing_number

        def pay(self, amount):
            """Process bank transfer."""
            return (
                f"Processing bank transfer of ${amount:.2f} "
                f"from account ending in {self.account_number[-4:]}"
            )

    print("Polymorphism example - Payment methods:")

    # Create different payment methods
    payments = [
        CreditCardPayment("1234567812345678", "12/25", "123"),
        PayPalPayment("user@example.com"),
        BankTransferPayment("9876543210", "021000021"),
    ]

    # Demonstrate polymorphism - same interface, different implementations
    for payment in payments:
        print(f"\n  Using {payment.__class__.__name__}:")
        print(f"    {payment.pay(100.00)}")
        print(f"    Receipt: {payment.get_receipt()}")


def exercise_2_encapsulation():
    """
    Demonstrate encapsulation with private attributes.

    1. Use underscore convention for private attributes
    2. Create getter and setter methods
    3. Show data protection
    """

    class BankAccount:
        """Bank account with encapsulated attributes."""

        def __init__(self, account_number, owner_name, initial_balance):
            self.account_number = account_number  # Public
            self.owner_name = owner_name  # Public
            self._balance = initial_balance  # Protected (by convention)
            self.__transactions = []  # Private (name mangling)
            self.__pin = "0000"  # Private

        # Getter methods
        def get_balance(self):
            """Get current balance."""
            return self._balance

        def get_transaction_count(self):
            """Get number of transactions."""
            return len(self.__transactions)

        # Setter methods with validation
        def set_pin(self, old_pin, new_pin):
            """Change PIN with validation."""
            if old_pin != self.__pin:
                return "Incorrect old PIN"

            if len(new_pin) != 4 or not new_pin.isdigit():
                return "PIN must be 4 digits"

            self.__pin = new_pin
            return "PIN changed successfully"

        def deposit(self, amount, pin):
            """Deposit money with PIN verification."""
            if pin != self.__pin:
                return "Incorrect PIN"

            if amount <= 0:
                return "Deposit amount must be positive"

            self._balance += amount
            self.__transactions.append(f"Deposit: +${amount:.2f}")
            return f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"

        def withdraw(self, amount, pin):
            """Withdraw money with PIN verification."""
            if pin != self.__pin:
                return "Incorrect PIN"

            if amount <= 0:
                return "Withdrawal amount must be positive"

            if amount > self._balance:
                return "Insufficient funds"

            self._balance -= amount
            self.__transactions.append(f"Withdrawal: -${amount:.2f}")
            return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"

        def get_statement(self, pin):
            """Get account statement with PIN verification."""
            if pin != self.__pin:
                return "Incorrect PIN"

            statement = f"Account: {self.account_number}\n"
            statement += f"Owner: {self.owner_name}\n"
            statement += f"Balance: ${self._balance:.2f}\n"
            statement += f"Transactions ({self.get_transaction_count()}):\n"

            for i, transaction in enumerate(self.__transactions[-5:], 1):
                statement += f"  {i}. {transaction}\n"

            return statement

        # Attempt to access private attribute (will fail)
        def try_access_private(self):
            """Demonstrate that private attributes are not easily accessible."""
            try:
                # This will work from inside the class
                print(f"  Inside class: __pin = {self.__pin}")
            except AttributeError:
                print("  Cannot access __pin directly")

    print("\nEncapsulation example - Bank Account:")

    # Create account
    account = BankAccount("ACC123", "Alice Smith", 1000.00)

    print(f"  Account created: {account.owner_name}")
    print(f"  Initial balance: ${account.get_balance():.2f}")

    # Test operations with wrong PIN
    print("\n  Test with wrong PIN:")
    print(f"    Deposit: {account.deposit(100, '1111')}")

    # Test with correct PIN
    print("\n  Test with correct PIN:")
    print(f"    {account.set_pin('0000', '1234')}")
    print(f"    {account.deposit(500, '1234')}")
    print(f"    {account.withdraw(200, '1234')}")

    # Get statement
    print("\n  Account statement:")
    print(account.get_statement("1234"))

    # Demonstrate access restrictions
    print("\n  Access demonstration:")
    print(f"    Public attribute (account_number): {account.account_number}")
    print(
        f"    Protected attribute (_balance): ${account._balance:.2f} (accessible but shouldn't be)"
    )
    print(f"    Transaction count via getter: {account.get_transaction_count()}")

    # Try to access private attribute from outside
    print("\n  Attempting to access private attributes from outside:")
    try:
        # This will fail due to name mangling
        print(f"    account.__pin: {account.__pin}")
    except AttributeError as e:
        print(f"    Error accessing __pin: {e}")

    # But we can still access it with name mangling (not recommended!)
    print(f"    account._BankAccount__pin: {account._BankAccount__pin}")


def exercise_3_property_decorators():
    """
    Demonstrate property decorators.

    1. Use @property for getters
    2. Use @attribute.setter for setters
    3. Create computed properties
    """

    class Temperature:
        """Temperature class with property decorators."""

        def __init__(self, celsius=0):
            self._celsius = celsius

        @property
        def celsius(self):
            """Get temperature in Celsius."""
            return self._celsius

        @celsius.setter
        def celsius(self, value):
            """Set temperature in Celsius with validation."""
            if value < -273.15:  # Absolute zero
                raise ValueError(
                    "Temperature cannot be below absolute zero (-273.15°C)"
                )
            self._celsius = value

        @property
        def fahrenheit(self):
            """Get temperature in Fahrenheit (computed property)."""
            return (self._celsius * 9 / 5) + 32

        @fahrenheit.setter
        def fahrenheit(self, value):
            """Set temperature via Fahrenheit."""
            self._celsius = (value - 32) * 5 / 9

        @property
        def kelvin(self):
            """Get temperature in Kelvin (computed property)."""
            return self._celsius + 273.15

        @kelvin.setter
        def kelvin(self, value):
            """Set temperature via Kelvin."""
            if value < 0:
                raise ValueError("Kelvin cannot be negative")
            self._celsius = value - 273.15

        def __str__(self):
            return (
                f"{self._celsius:.1f}°C = {self.fahrenheit:.1f}°F = {self.kelvin:.1f}K"
            )

    class Rectangle:
        """Rectangle with property decorators."""

        def __init__(self, width, height):
            self._width = width
            self._height = height

        @property
        def width(self):
            """Get width."""
            return self._width

        @width.setter
        def width(self, value):
            """Set width with validation."""
            if value <= 0:
                raise ValueError("Width must be positive")
            self._width = value

        @property
        def height(self):
            """Get height."""
            return self._height

        @height.setter
        def height(self, value):
            """Set height with validation."""
            if value <= 0:
                raise ValueError("Height must be positive")
            self._height = value

        @property
        def area(self):
            """Compute area (read-only property)."""
            return self._width * self._height

        @property
        def perimeter(self):
            """Compute perimeter (read-only property)."""
            return 2 * (self._width + self._height)

        @property
        def is_square(self):
            """Check if rectangle is square (read-only property)."""
            return self._width == self._height

        def __str__(self):
            shape = "Square" if self.is_square else "Rectangle"
            return f"{shape}({self._width}x{self._height}), Area: {self.area}, Perimeter: {self.perimeter}"

    print("\nProperty decorators example:")

    # Temperature example
    print("\n  Temperature class:")
    temp = Temperature(25)
    print(f"    Initial: {temp}")

    # Using property setters
    temp.celsius = 30
    print(f"    After setting celsius=30: {temp}")

    temp.fahrenheit = 86  # Should be 30°C
    print(f"    After setting fahrenheit=86: {temp}")

    temp.kelvin = 300  # Should be 26.85°C
    print(f"    After setting kelvin=300: {temp}")

    # Rectangle example
    print("\n  Rectangle class:")
    rect = Rectangle(5, 3)
    print(f"    Initial: {rect}")

    # Using property setters
    rect.width = 6
    rect.height = 4
    print(f"    After setting width=6, height=4: {rect}")

    # Try to set read-only property
    print("\n    Trying to set area (read-only):")
    try:
        rect.area = 100  # This will fail
    except AttributeError as e:
        print(f"      Error: {e}")

    # Validation example
    print("\n    Testing validation:")
    try:
        rect.width = -5
    except ValueError as e:
        print(f"      Error setting width=-5: {e}")


def exercise_4_employee_management():
    """
    Employee management system with encapsulation.

    1. Create Employee class with private attributes
    2. Use property decorators for access control
    3. Implement salary management with validation
    """

    class Employee:
        """Employee class with encapsulated data."""

        def __init__(self, name, employee_id, department, base_salary):
            self._name = name
            self._employee_id = employee_id
            self._department = department
            self._base_salary = base_salary
            self._bonus = 0
            self._years_of_service = 0
            self.__performance_rating = 3.0  # 1-5 scale, private

        # Property decorators for basic attributes
        @property
        def name(self):
            return self._name

        @property
        def employee_id(self):
            return self._employee_id

        @property
        def department(self):
            return self._department

        @department.setter
        def department(self, new_department):
            self._department = new_department

        # Salary properties with validation
        @property
        def base_salary(self):
            return self._base_salary

        @base_salary.setter
        def base_salary(self, new_salary):
            if new_salary < 0:
                raise ValueError("Salary cannot be negative")
            self._base_salary = new_salary

        @property
        def bonus(self):
            return self._bonus

        @bonus.setter
        def bonus(self, amount):
            if amount < 0:
                raise ValueError("Bonus cannot be negative")
            self._bonus = amount

        # Years of service with auto-increment
        @property
        def years_of_service(self):
            return self._years_of_service

        def add_year_of_service(self):
            """Add one year of service."""
            self._years_of_service += 1

        # Performance rating with getter/setter
        @property
        def performance_rating(self):
            """Get performance rating."""
            return self.__performance_rating

        @performance_rating.setter
        def performance_rating(self, rating):
            """Set performance rating with validation."""
            if not 1.0 <= rating <= 5.0:
                raise ValueError("Performance rating must be between 1.0 and 5.0")
            self.__performance_rating = rating

        # Computed properties
        @property
        def total_salary(self):
            """Calculate total salary (base + bonus)."""
            return self._base_salary + self._bonus

        @property
        def salary_with_seniority_bonus(self):
            """Calculate salary with seniority bonus."""
            seniority_bonus = self._years_of_service * 1000
            return self.total_salary + seniority_bonus

        @property
        def performance_bonus(self):
            """Calculate performance-based bonus."""
            if self.__performance_rating >= 4.5:
                return self._base_salary * 0.20
            elif self.__performance_rating >= 4.0:
                return self._base_salary * 0.15
            elif self.__performance_rating >= 3.5:
                return self._base_salary * 0.10
            elif self.__performance_rating >= 3.0:
                return self._base_salary * 0.05
            else:
                return 0

        # Methods
        def promote(self, new_department, salary_increase):
            """Promote employee to new department with salary increase."""
            old_dept = self._department
            old_salary = self._base_salary

            self._department = new_department
            self._base_salary += salary_increase

            return (
                f"Promoted from {old_dept} to {new_department}. "
                f"Salary increased from ${old_salary:,.2f} to ${self._base_salary:,.2f}"
            )

        def get_employee_summary(self):
            """Get employee summary."""
            return (
                f"Employee: {self._name} (ID: {self._employee_id})\n"
                f"Department: {self._department}\n"
                f"Years of service: {self._years_of_service}\n"
                f"Base salary: ${self._base_salary:,.2f}\n"
                f"Bonus: ${self._bonus:,.2f}\n"
                f"Performance rating: {self.__performance_rating:.1f}/5.0\n"
                f"Total salary: ${self.total_salary:,.2f}\n"
                f"Performance bonus: ${self.performance_bonus:,.2f}\n"
                f"Salary with seniority: ${self.salary_with_seniority_bonus:,.2f}"
            )

    print("\nEmployee management system:")

    # Create employees
    emp1 = Employee("Alice Johnson", "E001", "Engineering", 80000)
    emp2 = Employee("Bob Smith", "E002", "Sales", 60000)

    # Set up employees
    emp1.years_of_service = 3  # Actually need to use the method
    for _ in range(3):
        emp1.add_year_of_service()
    emp1.performance_rating = 4.7
    emp1.bonus = 5000

    emp2.years_of_service = 1
    for _ in range(1):
        emp2.add_year_of_service()
    emp2.performance_rating = 3.8
    emp2.bonus = 3000

    # Display employee information
    employees = [emp1, emp2]
    for emp in employees:
        print(f"\n  {emp.name}:")
        print(f"    Department: {emp.department}")
        print(f"    Base salary: ${emp.base_salary:,.2f}")
        print(f"    Bonus: ${emp.bonus:,.2f}")
        print(f"    Total salary: ${emp.total_salary:,.2f}")
        print(f"    Performance bonus: ${emp.performance_bonus:,.2f}")
        print(f"    Salary with seniority: ${emp.salary_with_seniority_bonus:,.2f}")

    # Demonstrate promotion
    print(f"\n  Promoting {emp1.name}:")
    print(f"    {emp1.promote('Senior Engineering', 15000)}")

    # Demonstrate validation
    print(f"\n  Testing validation for {emp2.name}:")
    try:
        emp2.base_salary = -1000
    except ValueError as e:
        print(f"    Error: {e}")

    try:
        emp2.performance_rating = 6.0
    except ValueError as e:
        print(f"    Error: {e}")

    # Show complete summary
    print(f"\n  Complete summary for {emp1.name}:")
    print(emp1.get_employee_summary())


def exercise_5_readonly_properties():
    """
    Demonstrate read-only properties.

    1. Create properties without setters
    2. Show computed read-only properties
    3. Demonstrate immutability
    """

    class Circle:
        """Circle with read-only properties."""

        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self):
            """Get radius (read-only after initialization)."""
            return self._radius

        @property
        def diameter(self):
            """Compute diameter (read-only)."""
            return 2 * self._radius

        @property
        def circumference(self):
            """Compute circumference (read-only)."""
            return 2 * 3.14159 * self._radius

        @property
        def area(self):
            """Compute area (read-only)."""
            return 3.14159 * self._radius**2

        def __str__(self):
            return (
                f"Circle(r={self._radius}), "
                f"d={self.diameter:.2f}, "
                f"c={self.circumference:.2f}, "
                f"a={self.area:.2f}"
            )

    class ImmutablePoint:
        """Immutable point with read-only properties."""

        def __init__(self, x, y):
            self._x = x
            self._y = y

        @property
        def x(self):
            """Get x coordinate (read-only)."""
            return self._x

        @property
        def y(self):
            """Get y coordinate (read-only)."""
            return self._y

        @property
        def distance_from_origin(self):
            """Compute distance from origin (read-only)."""
            return (self._x**2 + self._y**2) ** 0.5

        @property
        def quadrant(self):
            """Determine quadrant (read-only)."""
            if self._x > 0 and self._y > 0:
                return "Quadrant I"
            elif self._x < 0 and self._y > 0:
                return "Quadrant II"
            elif self._x < 0 and self._y < 0:
                return "Quadrant III"
            elif self._x > 0 and self._y < 0:
                return "Quadrant IV"
            elif self._x == 0 and self._y != 0:
                return "Y-axis"
            elif self._y == 0 and self._x != 0:
                return "X-axis"
            else:
                return "Origin"

        def translate(self, dx, dy):
            """Create a new translated point (immutable)."""
            return ImmutablePoint(self._x + dx, self._y + dy)

        def __str__(self):
            return f"Point({self._x}, {self._y})"

    print("\nRead-only properties example:")

    # Circle example
    print("\n  Circle class:")
    circle = Circle(5)
    print(f"    Created: {circle}")

    print("\n    Trying to modify read-only properties:")
    try:
        circle.radius = 10  # This will fail
    except AttributeError as e:
        print(f"      Error setting radius: {e}")

    try:
        circle.diameter = 20  # This will fail
    except AttributeError as e:
        print(f"      Error setting diameter: {e}")

    # ImmutablePoint example
    print("\n  ImmutablePoint class:")
    point = ImmutablePoint(3, 4)
    print(f"    Created: {point}")
    print(f"    Distance from origin: {point.distance_from_origin:.2f}")
    print(f"    Quadrant: {point.quadrant}")

    # Create new point (immutability)
    new_point = point.translate(2, -1)
    print("\n    After translate(2, -1):")
    print(f"      Original: {point}")
    print(f"      New point: {new_point}")
    print(f"      New quadrant: {new_point.quadrant}")

    print("\n    Trying to modify immutable point:")
    try:
        point.x = 10  # This will fail
    except AttributeError as e:
        print(f"      Error setting x: {e}")


def mini_project_employee_management_system():
    """
    Employee Management System

    A complete employee management system using encapsulation and properties.

    Features:
    1. Employee data encapsulation
    2. Property decorators for validation
    3. Salary and performance management
    """

    # Use the Employee class from exercise 4
    class Employee:
        """Employee class with encapsulated data."""

        def __init__(self, name, employee_id, department, base_salary):
            self._name = name
            self._employee_id = employee_id
            self._department = department
            self._base_salary = base_salary
            self._bonus = 0
            self._years_of_service = 0
            self.__performance_rating = 3.0

        @property
        def name(self):
            return self._name

        @property
        def employee_id(self):
            return self._employee_id

        @property
        def department(self):
            return self._department

        @department.setter
        def department(self, new_department):
            self._department = new_department

        @property
        def base_salary(self):
            return self._base_salary

        @base_salary.setter
        def base_salary(self, new_salary):
            if new_salary < 0:
                raise ValueError("Salary cannot be negative")
            self._base_salary = new_salary

        @property
        def bonus(self):
            return self._bonus

        @bonus.setter
        def bonus(self, amount):
            if amount < 0:
                raise ValueError("Bonus cannot be negative")
            self._bonus = amount

        @property
        def years_of_service(self):
            return self._years_of_service

        def add_year_of_service(self):
            self._years_of_service += 1

        @property
        def performance_rating(self):
            return self.__performance_rating

        @performance_rating.setter
        def performance_rating(self, rating):
            if not 1.0 <= rating <= 5.0:
                raise ValueError("Performance rating must be between 1.0 and 5.0")
            self.__performance_rating = rating

        @property
        def total_salary(self):
            return self._base_salary + self._bonus

        @property
        def salary_with_seniority_bonus(self):
            seniority_bonus = self._years_of_service * 1000
            return self.total_salary + seniority_bonus

        @property
        def performance_bonus(self):
            if self.__performance_rating >= 4.5:
                return self._base_salary * 0.20
            elif self.__performance_rating >= 4.0:
                return self._base_salary * 0.15
            elif self.__performance_rating >= 3.5:
                return self._base_salary * 0.10
            elif self.__performance_rating >= 3.0:
                return self._base_salary * 0.05
            else:
                return 0

        def promote(self, new_department, salary_increase):
            old_dept = self._department
            old_salary = self._base_salary

            self._department = new_department
            self._base_salary += salary_increase

            return (
                f"Promoted from {old_dept} to {new_department}. "
                f"Salary increased from ${old_salary:,.2f} to ${self._base_salary:,.2f}"
            )

        def get_summary(self):
            return (
                f"Employee: {self._name} (ID: {self._employee_id})\n"
                f"Department: {self._department}\n"
                f"Years of service: {self._years_of_service}\n"
                f"Base salary: ${self._base_salary:,.2f}\n"
                f"Bonus: ${self._bonus:,.2f}\n"
                f"Performance rating: {self.__performance_rating:.1f}/5.0\n"
                f"Total salary: ${self.total_salary:,.2f}"
            )

    print("=" * 60)
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 60)

    # Create initial employees
    employees = {
        "E001": Employee("Alice Johnson", "E001", "Engineering", 80000),
        "E002": Employee("Bob Smith", "E002", "Sales", 60000),
        "E003": Employee("Charlie Brown", "E003", "Marketing", 55000),
    }

    # Set up initial data
    employees["E001"].years_of_service = 3
    for _ in range(3):
        employees["E001"].add_year_of_service()
    employees["E001"].performance_rating = 4.7
    employees["E001"].bonus = 5000

    employees["E002"].years_of_service = 1
    for _ in range(1):
        employees["E002"].add_year_of_service()
    employees["E002"].performance_rating = 3.8
    employees["E002"].bonus = 3000

    employees["E003"].years_of_service = 5
    for _ in range(5):
        employees["E003"].add_year_of_service()
    employees["E003"].performance_rating = 4.2
    employees["E003"].bonus = 4000

    def display_employees():
        """Display all employees."""
        if not employees:
            print("No employees found.")
            return

        print("\nAll Employees:")
        print("-" * 60)
        for emp_id, employee in employees.items():
            print(
                f"{emp_id}: {employee.name} - {employee.department} "
                f"(Salary: ${employee.total_salary:,.2f})"
            )

    def create_employee():
        """Create a new employee."""
        print("\nCreate New Employee:")

        # Generate employee ID
        emp_id = f"E{len(employees) + 1:03d}"
        print(f"Generated employee ID: {emp_id}")

        name = input("Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        department = input("Department: ").strip() or "General"

        try:
            base_salary = float(input("Base salary: $"))
            if base_salary < 0:
                print("Salary cannot be negative.")
                return
        except ValueError:
            print("Invalid salary. Using $0.00.")
            base_salary = 0.0

        new_employee = Employee(name, emp_id, department, base_salary)
        employees[emp_id] = new_employee

        print("Employee created successfully!")
        print(f"{new_employee.get_summary()}")

    print(f"Loaded {len(employees)} employee(s).")

    while True:
        print("\nMain Menu:")
        print("1. View all employees")
        print("2. Create new employee")
        print("3. View employee details")
        print("4. Update employee")
        print("5. Add year of service")
        print("6. Calculate bonuses")
        print("0. Exit")

        try:
            choice = input("\nEnter your choice (0-6): ")

            if choice == "0":
                print("Exiting Employee Management System. Goodbye!")
                break

            elif choice == "1":
                display_employees()

            elif choice == "2":
                create_employee()

            elif choice in ["3", "4", "5", "6"]:
                # Need to select an employee
                emp_id = input("Enter employee ID: ").upper()
                employee = employees.get(emp_id)

                if not employee:
                    print(f"Employee {emp_id} not found.")
                    continue

                if choice == "3":  # View details
                    print(f"\nEmployee Details for {employee.name}:")
                    print(employee.get_summary())

                elif choice == "4":  # Update employee
                    print(f"\nUpdate Employee {employee.name}:")
                    print("1. Update department")
                    print("2. Update base salary")
                    print("3. Update bonus")
                    print("4. Update performance rating")
                    print("5. Promote employee")

                    update_choice = input("Enter update option (1-5): ")

                    if update_choice == "1":
                        new_dept = input("New department: ").strip()
                        if new_dept:
                            employee.department = new_dept
                            print(f"Department updated to {new_dept}")

                    elif update_choice == "2":
                        try:
                            new_salary = float(input("New base salary: $"))
                            employee.base_salary = new_salary
                            print(f"Base salary updated to ${new_salary:,.2f}")
                        except ValueError as e:
                            print(f"Error: {e}")

                    elif update_choice == "3":
                        try:
                            new_bonus = float(input("New bonus amount: $"))
                            employee.bonus = new_bonus
                            print(f"Bonus updated to ${new_bonus:,.2f}")
                        except ValueError as e:
                            print(f"Error: {e}")

                    elif update_choice == "4":
                        try:
                            new_rating = float(
                                input("New performance rating (1.0-5.0): ")
                            )
                            employee.performance_rating = new_rating
                            print(f"Performance rating updated to {new_rating:.1f}")
                        except ValueError as e:
                            print(f"Error: {e}")

                    elif update_choice == "5":
                        new_dept = input("New department: ").strip()
                        try:
                            increase = float(input("Salary increase: $"))
                            print(employee.promote(new_dept, increase))
                        except ValueError:
                            print("Invalid salary increase.")

                    else:
                        print("Invalid choice.")

                elif choice == "5":  # Add year of service
                    employee.add_year_of_service()
                    print(
                        f"Added year of service for {employee.name}. "
                        f"Total years: {employee.years_of_service}"
                    )

                elif choice == "6":  # Calculate bonuses
                    print(f"\nBonus Calculation for {employee.name}:")
                    print(
                        f"  Performance rating: {employee.performance_rating:.1f}/5.0"
                    )
                    print(f"  Performance bonus: ${employee.performance_bonus:,.2f}")
                    print(f"  Current bonus: ${employee.bonus:,.2f}")
                    print(
                        f"  Total salary with bonuses: ${employee.total_salary + employee.performance_bonus:,.2f}"
                    )

            else:
                print("Invalid choice. Please enter 0-6.")

        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def run_all_exercises():
    """Run all Day 17 exercises."""
    print("=" * 60)
    print("Week 3, Day 17: Polymorphism & Encapsulation")
    print("=" * 60)

    print("\n--- Exercise 1: Polymorphism ---")
    exercise_1_polymorphism()

    print("\n--- Exercise 2: Encapsulation ---")
    exercise_2_encapsulation()

    print("\n--- Exercise 3: Property Decorators ---")
    exercise_3_property_decorators()

    print("\n--- Exercise 4: Employee Management ---")
    exercise_4_employee_management()

    print("\n--- Exercise 5: Read-only Properties ---")
    exercise_5_readonly_properties()

    print("\n" + "=" * 60)
    print("Mini Project: Employee Management System")
    print("=" * 60)
    mini_project_employee_management_system()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 17 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
