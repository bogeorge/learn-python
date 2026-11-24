import sys

"""
Week 3, Day 15: Classes & Objects

Exercises to practice class definition, objects, methods, attributes,
and basic object-oriented programming concepts.
"""


def exercise_1_basic_class():
    """
    Create a basic Person class.
    
    1. Define a Person class with name and age attributes
    2. Add methods to get and set attributes
    3. Create multiple Person objects
    """
    
    class Person:
        """A simple Person class."""
        
        def __init__(self, name, age):
            """Initialize a Person with name and age."""
            self.name = name
            self.age = age
        
        def greet(self):
            """Return a greeting message."""
            return f"Hello, my name is {self.name} and I'm {self.age} years old."
        
        def have_birthday(self):
            """Increase age by 1."""
            self.age += 1
            return f"Happy birthday {self.name}! You are now {self.age}."
        
        def __str__(self):
            """Return string representation of the Person."""
            return f"Person(name='{self.name}', age={self.age})"
    
    print("Basic Person class:")
    
    # Create Person objects
    alice = Person("Alice", 30)
    bob = Person("Bob", 25)
    
    print(f"  Alice: {alice}")
    print(f"  Bob: {bob}")
    
    # Call methods
    print(f"  Alice.greet(): {alice.greet()}")
    print(f"  Bob.have_birthday(): {bob.have_birthday()}")
    
    # Access attributes
    print(f"  Alice's name: {alice.name}")
    print(f"  Bob's age: {bob.age}")
    
    # Modify attributes
    alice.age = 31
    print(f"  After modification: {alice}")


def exercise_2_car_class():
    """
    Create a Car class with methods and attributes.
    
    1. Define a Car class with make, model, year, and mileage
    2. Add methods to drive the car and get info
    3. Track fuel level and consumption
    """
    
    class Car:
        """A Car class representing a vehicle."""
        
        def __init__(self, make, model, year, fuel_capacity=50):
            """Initialize a Car with basic attributes."""
            self.make = make
            self.model = model
            self.year = year
            self.mileage = 0
            self.fuel_capacity = fuel_capacity
            self.fuel_level = fuel_capacity
            self.is_running = False
        
        def start(self):
            """Start the car."""
            if self.fuel_level > 0:
                self.is_running = True
                return f"{self.make} {self.model} started."
            return "Cannot start - out of fuel!"
        
        def stop(self):
            """Stop the car."""
            self.is_running = False
            return f"{self.make} {self.model} stopped."
        
        def drive(self, distance):
            """Drive the car a certain distance."""
            if not self.is_running:
                return "Cannot drive - car is not running!"
            
            # Calculate fuel needed (assuming 10 km per liter)
            fuel_needed = distance / 10
            
            if fuel_needed > self.fuel_level:
                actual_distance = self.fuel_level * 10
                self.mileage += actual_distance
                self.fuel_level = 0
                self.is_running = False
                return (f"Drove {actual_distance:.1f} km before running out of fuel. "
                       f"Total mileage: {self.mileage:.1f} km")
            else:
                self.mileage += distance
                self.fuel_level -= fuel_needed
                return (f"Drove {distance} km. "
                       f"Fuel remaining: {self.fuel_level:.1f}L/{self.fuel_capacity}L")
        
        def refuel(self, amount):
            """Refuel the car."""
            if amount <= 0:
                return "Invalid fuel amount."
            
            space_available = self.fuel_capacity - self.fuel_level
            if amount > space_available:
                self.fuel_level = self.fuel_capacity
                return f"Added {space_available:.1f}L (tank is now full)."
            else:
                self.fuel_level += amount
                return f"Added {amount:.1f}L. Fuel level: {self.fuel_level:.1f}L"
        
        def get_info(self):
            """Get car information."""
            status = "running" if self.is_running else "stopped"
            return (f"{self.year} {self.make} {self.model} - "
                   f"Mileage: {self.mileage:.1f} km, "
                   f"Fuel: {self.fuel_level:.1f}L/{self.fuel_capacity}L, "
                   f"Status: {status}")
        
        def __str__(self):
            """Return string representation."""
            return self.get_info()
    
    print("\nCar class example:")
    
    # Create a car
    my_car = Car("Toyota", "Camry", 2020, 60)
    print(f"  Created: {my_car}")
    
    # Test methods
    print(f"  {my_car.start()}")
    print(f"  {my_car.drive(100)}")
    print(f"  {my_car.drive(400)}")  # Should run out of fuel
    print(f"  {my_car.refuel(30)}")
    print(f"  {my_car.start()}")
    print(f"  {my_car.drive(200)}")
    print(f"  {my_car.stop()}")
    
    print(f"\n  Final car info: {my_car}")


def exercise_3_book_class():
    """
    Create a Book class for a library system.
    
    1. Define a Book class with title, author, ISBN, and availability
    2. Add methods to check out and return books
    3. Track due dates and late fees
    """
    
    class Book:
        """A Book class for library management."""
        
        def __init__(self, title, author, isbn, pages):
            """Initialize a Book."""
            self.title = title
            self.author = author
            self.isbn = isbn
            self.pages = pages
            self.is_available = True
            self.borrower = None
            self.due_date = None
            self.times_borrowed = 0
        
        def checkout(self, borrower, due_date):
            """Check out the book to a borrower."""
            if not self.is_available:
                return f"Sorry, '{self.title}' is already checked out to {self.borrower}."
            
            self.is_available = False
            self.borrower = borrower
            self.due_date = due_date
            self.times_borrowed += 1
            
            return f"'{self.title}' checked out to {borrower}. Due: {due_date}"
        
        def return_book(self):
            """Return a checked out book."""
            if self.is_available:
                return f"'{self.title}' was not checked out."
            
            borrower = self.borrower
            self.is_available = True
            self.borrower = None
            self.due_date = None
            
            return f"'{self.title}' returned by {borrower}."
        
        def is_overdue(self, current_date):
            """Check if book is overdue."""
            if self.is_available or not self.due_date:
                return False
            
            # Simple string comparison for dates (YYYY-MM-DD format)
            return current_date > self.due_date
        
        def get_status(self):
            """Get current status of the book."""
            if self.is_available:
                return f"'{self.title}' is available for checkout."
            else:
                status = f"Checked out to {self.borrower}, due {self.due_date}"
                if self.times_borrowed > 0:
                    status += f" (borrowed {self.times_borrowed} times)"
                return status
        
        def __str__(self):
            """Return string representation."""
            return f"'{self.title}' by {self.author} ({self.pages} pages, ISBN: {self.isbn})"
    
    print("\nBook class example:")
    
    # Create some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 180)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 281)
    book3 = Book("1984", "George Orwell", "978-0451524935", 328)
    
    print(f"  Books created:")
    print(f"    1. {book1}")
    print(f"    2. {book2}")
    print(f"    3. {book3}")
    
    # Test checkout and return
    print(f"\n  Checkout tests:")
    print(f"    {book1.checkout('Alice', '2024-12-25')}")
    print(f"    {book2.checkout('Bob', '2024-12-20')}")
    print(f"    {book1.checkout('Charlie', '2024-12-30')}")  # Should fail
    
    print(f"\n  Status:")
    print(f"    Book1: {book1.get_status()}")
    print(f"    Book2: {book2.get_status()}")
    print(f"    Book3: {book3.get_status()}")
    
    print(f"\n  Overdue check (current date: 2024-12-26):")
    print(f"    Book1 overdue? {book1.is_overdue('2024-12-26')}")
    print(f"    Book2 overdue? {book2.is_overdue('2024-12-26')}")
    
    print(f"\n  Return tests:")
    print(f"    {book1.return_book()}")
    print(f"    {book1.return_book()}")  # Should say not checked out
    
    print(f"\n  Final status:")
    print(f"    Book1: {book1.get_status()}")


def exercise_4_rectangle_class():
    """
    Create a Rectangle class with geometric calculations.
    
    1. Define a Rectangle class with width and height
    2. Add methods for area, perimeter, and diagonal
    3. Add comparison methods
    """
    
    class Rectangle:
        """A Rectangle class for geometric calculations."""
        
        def __init__(self, width, height):
            """Initialize a Rectangle with width and height."""
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive numbers")
            self.width = width
            self.height = height
        
        def area(self):
            """Calculate area of the rectangle."""
            return self.width * self.height
        
        def perimeter(self):
            """Calculate perimeter of the rectangle."""
            return 2 * (self.width + self.height)
        
        def diagonal(self):
            """Calculate diagonal length of the rectangle."""
            return (self.width**2 + self.height**2) ** 0.5
        
        def is_square(self):
            """Check if the rectangle is a square."""
            return self.width == self.height
        
        def scale(self, factor):
            """Scale the rectangle by a factor."""
            if factor <= 0:
                raise ValueError("Scale factor must be positive")
            self.width *= factor
            self.height *= factor
        
        def rotate(self):
            """Rotate the rectangle (swap width and height)."""
            self.width, self.height = self.height, self.width
        
        def __eq__(self, other):
            """Check if two rectangles have same dimensions."""
            if not isinstance(other, Rectangle):
                return False
            return self.width == other.width and self.height == other.height
        
        def __lt__(self, other):
            """Compare rectangles by area."""
            if not isinstance(other, Rectangle):
                raise TypeError("Can only compare with other Rectangle objects")
            return self.area() < other.area()
        
        def __str__(self):
            """Return string representation."""
            shape = "Square" if self.is_square() else "Rectangle"
            return f"{shape}(width={self.width}, height={self.height})"
    
    print("\nRectangle class example:")
    
    # Create rectangles
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(4, 4)
    rect3 = Rectangle(6, 2)
    
    print(f"  Created rectangles:")
    print(f"    1. {rect1}")
    print(f"    2. {rect2} (square)")
    print(f"    3. {rect3}")
    
    # Test calculations
    print(f"\n  Calculations for rect1:")
    print(f"    Area: {rect1.area()}")
    print(f"    Perimeter: {rect1.perimeter()}")
    print(f"    Diagonal: {rect1.diagonal():.2f}")
    print(f"    Is square? {rect1.is_square()}")
    
    print(f"\n  Calculations for rect2:")
    print(f"    Area: {rect2.area()}")
    print(f"    Is square? {rect2.is_square()}")
    
    # Test operations
    print(f"\n  Operations:")
    rect1_copy = Rectangle(5, 3)
    print(f"    rect1 == rect1_copy? {rect1 == rect1_copy}")
    print(f"    rect1 < rect2? {rect1 < rect2}")
    print(f"    rect2 < rect3? {rect2 < rect3}")
    
    # Test scaling and rotating
    print(f"\n  Transformations:")
    rect1.scale(2)
    print(f"    After scaling by 2: {rect1}")
    print(f"    New area: {rect1.area()}")
    
    rect1.rotate()
    print(f"    After rotating: {rect1}")


def exercise_5_bank_account_class():
    """
    Create a BankAccount class for the mini-project.
    
    1. Define a BankAccount class with account number, owner, and balance
    2. Add methods for deposit, withdrawal, and transfer
    3. Implement interest calculation
    4. Add transaction history
    """
    
    class BankAccount:
        """A BankAccount class representing a bank account."""
        
        def __init__(self, account_number, owner_name, initial_balance=0):
            """Initialize a BankAccount."""
            self.account_number = account_number
            self.owner_name = owner_name
            self.balance = initial_balance
            self.transaction_history = []
            self._record_transaction("Account opened", initial_balance)
        
        def deposit(self, amount):
            """Deposit money into the account."""
            if amount <= 0:
                return "Deposit amount must be positive."
            
            self.balance += amount
            self._record_transaction("Deposit", amount)
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        
        def withdraw(self, amount):
            """Withdraw money from the account."""
            if amount <= 0:
                return "Withdrawal amount must be positive."
            
            if amount > self.balance:
                return f"Insufficient funds. Balance: ${self.balance:.2f}"
            
            self.balance -= amount
            self._record_transaction("Withdrawal", -amount)
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        
        def transfer(self, amount, target_account):
            """Transfer money to another BankAccount."""
            if not isinstance(target_account, BankAccount):
                return "Target must be a BankAccount object."
            
            if amount <= 0:
                return "Transfer amount must be positive."
            
            if amount > self.balance:
                return f"Insufficient funds. Balance: ${self.balance:.2f}"
            
            # Withdraw from this account
            self.balance -= amount
            self._record_transaction(f"Transfer to {target_account.owner_name}", -amount)
            
            # Deposit to target account
            target_account.balance += amount
            target_account._record_transaction(f"Transfer from {self.owner_name}", amount)
            
            return (f"Transferred ${amount:.2f} to {target_account.owner_name}. "
                   f"New balance: ${self.balance:.2f}")
        
        def add_interest(self, rate_percent):
            """Add interest to the account balance."""
            if rate_percent <= 0:
                return "Interest rate must be positive."
            
            interest = self.balance * (rate_percent / 100)
            self.balance += interest
            self._record_transaction(f"Interest ({rate_percent}%)", interest)
            return f"Added ${interest:.2f} interest. New balance: ${self.balance:.2f}"
        
        def get_statement(self, num_transactions=5):
            """Get recent transaction statement."""
            if not self.transaction_history:
                return "No transactions yet."
            
            statement = f"Statement for {self.owner_name} (Account: {self.account_number})\n"
            statement += f"Current balance: ${self.balance:.2f}\n\n"
            statement += "Recent transactions:\n"
            
            recent = self.transaction_history[-num_transactions:]
            for transaction in recent:
                amount = transaction["amount"]
                sign = "+" if amount >= 0 else ""
                statement += f"  {transaction['description']}: {sign}${abs(amount):.2f}\n"
            
            return statement
        
        def _record_transaction(self, description, amount):
            """Record a transaction in history (private method)."""
            self.transaction_history.append({
                "description": description,
                "amount": amount,
                "balance": self.balance
            })
        
        def __str__(self):
            """Return string representation."""
            return (f"BankAccount(owner='{self.owner_name}', "
                   f"account='{self.account_number}', balance=${self.balance:.2f})")
    
    print("\nBankAccount class example:")
    
    # Create bank accounts
    account1 = BankAccount("ACC001", "Alice Johnson", 1000.00)
    account2 = BankAccount("ACC002", "Bob Smith", 500.00)
    
    print(f"  Created accounts:")
    print(f"    1. {account1}")
    print(f"    2. {account2}")
    
    # Test operations
    print(f"\n  Account operations:")
    print(f"    {account1.deposit(250.50)}")
    print(f"    {account1.withdraw(100.00)}")
    print(f"    {account1.withdraw(2000.00)}")  # Should fail
    
    print(f"    {account1.transfer(300.00, account2)}")
    
    print(f"    {account1.add_interest(2.5)}")
    
    # Get statements
    print(f"\n  Account1 statement:")
    print(account1.get_statement())
    
    print(f"\n  Account2 statement (first 3 transactions):")
    print(account2.get_statement(3))


def mini_project_bank_account_system():
    """
    Bank Account System
    
    A complete bank account management system using OOP principles.
    
    Features:
    1. Create multiple bank accounts
    2. Perform deposits, withdrawals, transfers
    3. Calculate interest
    4. View transaction history
    """
    
    # Use the BankAccount class from exercise 5
    class BankAccount:
        """A BankAccount class representing a bank account."""
        
        def __init__(self, account_number, owner_name, initial_balance=0):
            """Initialize a BankAccount."""
            self.account_number = account_number
            self.owner_name = owner_name
            self.balance = initial_balance
            self.transaction_history = []
            self._record_transaction("Account opened", initial_balance)
        
        def deposit(self, amount):
            """Deposit money into the account."""
            if amount <= 0:
                return "Deposit amount must be positive."
            
            self.balance += amount
            self._record_transaction("Deposit", amount)
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        
        def withdraw(self, amount):
            """Withdraw money from the account."""
            if amount <= 0:
                return "Withdrawal amount must be positive."
            
            if amount > self.balance:
                return f"Insufficient funds. Balance: ${self.balance:.2f}"
            
            self.balance -= amount
            self._record_transaction("Withdrawal", -amount)
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        
        def transfer(self, amount, target_account):
            """Transfer money to another BankAccount."""
            if not isinstance(target_account, BankAccount):
                return "Target must be a BankAccount object."
            
            if amount <= 0:
                return "Transfer amount must be positive."
            
            if amount > self.balance:
                return f"Insufficient funds. Balance: ${self.balance:.2f}"
            
            # Withdraw from this account
            self.balance -= amount
            self._record_transaction(f"Transfer to {target_account.owner_name}", -amount)
            
            # Deposit to target account
            target_account.balance += amount
            target_account._record_transaction(f"Transfer from {self.owner_name}", amount)
            
            return (f"Transferred ${amount:.2f} to {target_account.owner_name}. "
                   f"New balance: ${self.balance:.2f}")
        
        def add_interest(self, rate_percent):
            """Add interest to the account balance."""
            if rate_percent <= 0:
                return "Interest rate must be positive."
            
            interest = self.balance * (rate_percent / 100)
            self.balance += interest
            self._record_transaction(f"Interest ({rate_percent}%)", interest)
            return f"Added ${interest:.2f} interest. New balance: ${self.balance:.2f}"
        
        def get_statement(self, num_transactions=5):
            """Get recent transaction statement."""
            if not self.transaction_history:
                return "No transactions yet."
            
            statement = f"Statement for {self.owner_name} (Account: {self.account_number})\n"
            statement += f"Current balance: ${self.balance:.2f}\n\n"
            statement += "Recent transactions:\n"
            
            recent = self.transaction_history[-num_transactions:]
            for transaction in recent:
                amount = transaction["amount"]
                sign = "+" if amount >= 0 else ""
                statement += f"  {transaction['description']}: {sign}${abs(amount):.2f}\n"
            
            return statement
        
        def _record_transaction(self, description, amount):
            """Record a transaction in history (private method)."""
            self.transaction_history.append({
                "description": description,
                "amount": amount,
                "balance": self.balance
            })
        
        def __str__(self):
            """Return string representation."""
            return (f"BankAccount(owner='{self.owner_name}', "
                   f"account='{self.account_number}', balance=${self.balance:.2f})")
    
    print("=" * 60)
    print("BANK ACCOUNT SYSTEM")
    print("=" * 60)
    
    # Create some initial accounts
    accounts = {
        "ACC001": BankAccount("ACC001", "Alice Johnson", 1000.00),
        "ACC002": BankAccount("ACC002", "Bob Smith", 500.00),
        "ACC003": BankAccount("ACC003", "Charlie Brown", 750.00)
    }
    
    def find_account(account_number):
        """Find an account by number."""
        return accounts.get(account_number)
    
    def display_accounts():
        """Display all accounts."""
        if not accounts:
            print("No accounts found.")
            return
        
        print("\nAll Accounts:")
        print("-" * 50)
        for acc_num, account in accounts.items():
            print(f"{acc_num}: {account.owner_name} - ${account.balance:.2f}")
    
    def create_account():
        """Create a new bank account."""
        print("\nCreate New Account:")
        
        # Generate account number
        account_number = f"ACC{len(accounts) + 1:03d}"
        print(f"Generated account number: {account_number}")
        
        owner_name = input("Owner name: ").strip()
        if not owner_name:
            print("Owner name cannot be empty.")
            return
        
        try:
            initial_balance = float(input("Initial deposit amount: $"))
            if initial_balance < 0:
                print("Initial balance cannot be negative.")
                return
        except ValueError:
            print("Invalid amount. Using $0.00 as initial balance.")
            initial_balance = 0.0
        
        new_account = BankAccount(account_number, owner_name, initial_balance)
        accounts[account_number] = new_account
        
        print(f"Account created successfully!")
        print(f"{new_account}")
    
    print(f"Loaded {len(accounts)} account(s).")
    
    while True:
        print("\nMain Menu:")
        print("1. View all accounts")
        print("2. Create new account")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Transfer money")
        print("6. Add interest")
        print("7. View account statement")
        print("8. Delete account")
        print("0. Exit")
        
        try:
            choice = input("\nEnter your choice (0-8): ")
            
            if choice == '0':
                print("Exiting Bank Account System. Goodbye!")
                break
            
            elif choice == '1':
                display_accounts()
            
            elif choice == '2':
                create_account()
            
            elif choice in ['3', '4', '5', '6', '7', '8']:
                # All these operations require an account
                account_number = input("Enter account number: ").upper()
                account = find_account(account_number)
                
                if not account:
                    print(f"Account {account_number} not found.")
                    continue
                
                if choice == '3':  # Deposit
                    try:
                        amount = float(input("Deposit amount: $"))
                        print(account.deposit(amount))
                    except ValueError:
                        print("Invalid amount.")
                
                elif choice == '4':  # Withdraw
                    try:
                        amount = float(input("Withdrawal amount: $"))
                        print(account.withdraw(amount))
                    except ValueError:
                        print("Invalid amount.")
                
                elif choice == '5':  # Transfer
                    target_number = input("Enter target account number: ").upper()
                    target_account = find_account(target_number)
                    
                    if not target_account:
                        print(f"Target account {target_number} not found.")
                        continue
                    
                    if target_account == account:
                        print("Cannot transfer to the same account.")
                        continue
                    
                    try:
                        amount = float(input("Transfer amount: $"))
                        print(account.transfer(amount, target_account))
                    except ValueError:
                        print("Invalid amount.")
                
                elif choice == '6':  # Add interest
                    try:
                        rate = float(input("Interest rate (%): "))
                        print(account.add_interest(rate))
                    except ValueError:
                        print("Invalid rate.")
                
                elif choice == '7':  # View statement
                    try:
                        num = input("Number of transactions to show (default 5): ")
                        num_transactions = int(num) if num.strip() else 5
                        print(account.get_statement(num_transactions))
                    except ValueError:
                        print("Invalid number. Showing 5 transactions.")
                        print(account.get_statement())
                
                elif choice == '8':  # Delete account
                    if account.balance != 0:
                        print(f"Cannot delete account with balance ${account.balance:.2f}")
                        continue
                    
                    confirm = input(f"Delete account {account_number}? (y/n): ")
                    if confirm.lower() == 'y':
                        del accounts[account_number]
                        print(f"Account {account_number} deleted.")
            
            else:
                print("Invalid choice. Please enter 0-8.")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def run_all_exercises():
    """Run all Day 15 exercises."""
    print("=" * 60)
    print("Week 3, Day 15: Classes & Objects")
    print("=" * 60)

    print("\n--- Exercise 1: Basic Class ---")
    exercise_1_basic_class()

    print("\n--- Exercise 2: Car Class ---")
    exercise_2_car_class()

    print("\n--- Exercise 3: Book Class ---")
    exercise_3_book_class()

    print("\n--- Exercise 4: Rectangle Class ---")
    exercise_4_rectangle_class()

    print("\n--- Exercise 5: Bank Account Class ---")
    exercise_5_bank_account_class()

    print("\n" + "=" * 60)
    print("Mini Project: Bank Account System")
    print("=" * 60)
    mini_project_bank_account_system()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 15 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()