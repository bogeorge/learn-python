import math
import sys

"""
Week 3, Day 16: Inheritance

Exercises to practice parent/child classes, method overriding, 
the super() function, and inheritance hierarchies.
"""


def exercise_1_basic_inheritance():
    """
    Basic inheritance example with Animal hierarchy.

    1. Create a base Animal class
    2. Create derived classes that inherit from Animal
    3. Demonstrate method overriding
    """

    class Animal:
        """Base class for all animals."""

        def __init__(self, name, species, age):
            self.name = name
            self.species = species
            self.age = age

        def make_sound(self):
            """Make a generic animal sound."""
            return "Some generic animal sound"

        def eat(self, food):
            """Eat some food."""
            return f"{self.name} is eating {food}"

        def sleep(self):
            """Sleep."""
            return f"{self.name} is sleeping"

        def get_info(self):
            """Get animal information."""
            return f"{self.name} the {self.species}, {self.age} years old"

    class Dog(Animal):
        """Dog class that inherits from Animal."""

        def __init__(self, name, age, breed):
            # Call parent class constructor
            super().__init__(name, "Dog", age)
            self.breed = breed

        def make_sound(self):
            """Override make_sound method."""
            return "Woof! Woof!"

        def fetch(self, item):
            """Dog-specific method."""
            return f"{self.name} is fetching the {item}"

    class Cat(Animal):
        """Cat class that inherits from Animal."""

        def __init__(self, name, age, color):
            super().__init__(name, "Cat", age)
            self.color = color

        def make_sound(self):
            """Override make_sound method."""
            return "Meow!"

        def climb_tree(self):
            """Cat-specific method."""
            return f"{self.name} is climbing a tree"

    class Bird(Animal):
        """Bird class that inherits from Animal."""

        def __init__(self, name, age, wingspan):
            super().__init__(name, "Bird", age)
            self.wingspan = wingspan

        def make_sound(self):
            """Override make_sound method."""
            return "Chirp! Chirp!"

        def fly(self, distance):
            """Bird-specific method."""
            return f"{self.name} is flying {distance} meters"

    print("Basic inheritance example:")

    # Create animals
    generic_animal = Animal("Generic", "Unknown", 2)
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 5, "Orange")
    bird = Bird("Tweety", 1, 0.25)

    animals = [generic_animal, dog, cat, bird]

    # Demonstrate inheritance
    for animal in animals:
        print(f"\n  {animal.get_info()}")
        print(f"    Sound: {animal.make_sound()}")
        print(f"    Eat: {animal.eat('food')}")
        print(f"    Sleep: {animal.sleep()}")

        # Type-specific behaviors
        if isinstance(animal, Dog):
            print(f"    Fetch: {animal.fetch('ball')}")
        elif isinstance(animal, Cat):
            print(f"    Climb: {animal.climb_tree()}")
        elif isinstance(animal, Bird):
            print(f"    Fly: {animal.fly(10)}")


def exercise_2_vehicle_hierarchy():
    """
    Create a vehicle class hierarchy.

    1. Create base Vehicle class
    2. Create derived classes for different vehicle types
    3. Demonstrate method overriding and super() usage
    """

    class Vehicle:
        """Base class for all vehicles."""

        def __init__(self, make, model, year, fuel_type):
            self.make = make
            self.model = model
            self.year = year
            self.fuel_type = fuel_type
            self.speed = 0
            self.is_running = False

        def start(self):
            """Start the vehicle."""
            self.is_running = True
            return f"{self.make} {self.model} started."

        def stop(self):
            """Stop the vehicle."""
            self.is_running = False
            self.speed = 0
            return f"{self.make} {self.model} stopped."

        def accelerate(self, increment):
            """Increase speed."""
            if not self.is_running:
                return "Cannot accelerate - vehicle is not running!"

            self.speed += increment
            return f"Accelerated to {self.speed} km/h"

        def brake(self, decrement):
            """Decrease speed."""
            self.speed = max(0, self.speed - decrement)
            return f"Slowed down to {self.speed} km/h"

        def get_info(self):
            """Get vehicle information."""
            status = "running" if self.is_running else "stopped"
            return (
                f"{self.year} {self.make} {self.model} - "
                f"Fuel: {self.fuel_type}, Speed: {self.speed} km/h, Status: {status}"
            )

    class Car(Vehicle):
        """Car class that inherits from Vehicle."""

        def __init__(self, make, model, year, fuel_type, doors, transmission):
            super().__init__(make, model, year, fuel_type)
            self.doors = doors
            self.transmission = transmission
            self.radio_on = False

        def start(self):
            """Override start method for car-specific behavior."""
            result = super().start()
            return f"{result} Car ready to drive."

        def toggle_radio(self):
            """Car-specific method."""
            self.radio_on = not self.radio_on
            status = "on" if self.radio_on else "off"
            return f"Radio turned {status}"

        def get_info(self):
            """Override get_info to include car details."""
            base_info = super().get_info()
            return (
                f"{base_info}, Doors: {self.doors}, Transmission: {self.transmission}"
            )

    class Motorcycle(Vehicle):
        """Motorcycle class that inherits from Vehicle."""

        def __init__(self, make, model, year, fuel_type, engine_size, has_sidecar):
            super().__init__(make, model, year, fuel_type)
            self.engine_size = engine_size
            self.has_sidecar = has_sidecar
            self.kickstand_up = False

        def start(self):
            """Override start method for motorcycle-specific behavior."""
            if not self.kickstand_up:
                return "Cannot start - kickstand is down!"

            result = super().start()
            return f"{result} Motorcycle ready to ride."

        def toggle_kickstand(self):
            """Motorcycle-specific method."""
            self.kickstand_up = not self.kickstand_up
            status = "up" if self.kickstand_up else "down"
            return f"Kickstand is now {status}"

        def wheelie(self):
            """Motorcycle-specific method."""
            if self.speed < 30:
                return "Need more speed for a wheelie!"
            return "Doing a wheelie!"

    class Truck(Vehicle):
        """Truck class that inherits from Vehicle."""

        def __init__(self, make, model, year, fuel_type, cargo_capacity, axles):
            super().__init__(make, model, year, fuel_type)
            self.cargo_capacity = cargo_capacity  # in tons
            self.axles = axles
            self.cargo_weight = 0

        def load_cargo(self, weight):
            """Truck-specific method."""
            if weight < 0:
                return "Cargo weight cannot be negative."

            available = self.cargo_capacity - self.cargo_weight
            if weight > available:
                return (
                    f"Cannot load {weight} tons. Only {available:.1f} tons available."
                )

            self.cargo_weight += weight
            return f"Loaded {weight} tons. Total cargo: {self.cargo_weight:.1f}/{self.cargo_capacity} tons"

        def unload_cargo(self, weight):
            """Truck-specific method."""
            if weight < 0:
                return "Unload weight cannot be negative."

            if weight > self.cargo_weight:
                return f"Cannot unload {weight} tons. Only {self.cargo_weight:.1f} tons loaded."

            self.cargo_weight -= weight
            return f"Unloaded {weight} tons. Remaining cargo: {self.cargo_weight:.1f}/{self.cargo_capacity} tons"

    print("\nVehicle hierarchy example:")

    # Create vehicles
    car = Car("Toyota", "Camry", 2020, "Gasoline", 4, "Automatic")
    motorcycle = Motorcycle(
        "Harley-Davidson", "Sportster", 2019, "Gasoline", 1200, False
    )
    truck = Truck("Ford", "F-150", 2021, "Diesel", 2.5, 2)

    vehicles = [car, motorcycle, truck]

    # Demonstrate vehicle behaviors
    for vehicle in vehicles:
        print(f"\n  {vehicle.get_info()}")

        # Vehicle-specific setup
        if isinstance(vehicle, Motorcycle):
            print(f"    {vehicle.toggle_kickstand()}")

        # Common behaviors
        print(f"    {vehicle.start()}")
        print(f"    {vehicle.accelerate(40)}")

        # Type-specific behaviors
        if isinstance(vehicle, Car):
            print(f"    {vehicle.toggle_radio()}")
        elif isinstance(vehicle, Motorcycle):
            print(f"    {vehicle.wheelie()}")
        elif isinstance(vehicle, Truck):
            print(f"    {vehicle.load_cargo(1.5)}")

        print(f"    {vehicle.brake(20)}")
        print(f"    {vehicle.stop()}")


def exercise_3_multilevel_inheritance():
    """
    Demonstrate multilevel inheritance.

    1. Create a multi-level inheritance hierarchy
    2. Show method resolution order
    3. Demonstrate super() at multiple levels
    """

    class Employee:
        """Base class for all employees."""

        def __init__(self, name, employee_id, salary):
            self.name = name
            self.employee_id = employee_id
            self.salary = salary

        def work(self):
            """Generic work method."""
            return f"{self.name} is working"

        def get_paid(self):
            """Get paid."""
            return f"{self.name} received ${self.salary:.2f}"

        def get_info(self):
            """Get employee information."""
            return f"Employee: {self.name} (ID: {self.employee_id})"

    class Manager(Employee):
        """Manager class that inherits from Employee."""

        def __init__(self, name, employee_id, salary, department, team_size):
            super().__init__(name, employee_id, salary)
            self.department = department
            self.team_size = team_size

        def work(self):
            """Override work method for managers."""
            base_work = super().work()
            return (
                f"{base_work} - managing {self.team_size} people in {self.department}"
            )

        def conduct_meeting(self):
            """Manager-specific method."""
            return f"{self.name} is conducting a team meeting"

        def get_info(self):
            """Override get_info for managers."""
            base_info = super().get_info()
            return f"{base_info}, Manager of {self.department} (Team: {self.team_size})"

    class SeniorManager(Manager):
        """Senior Manager class that inherits from Manager."""

        def __init__(self, name, employee_id, salary, department, team_size, budget):
            super().__init__(name, employee_id, salary, department, team_size)
            self.budget = budget
            self.projects = []

        def work(self):
            """Override work method for senior managers."""
            base_work = super().work()
            return f"{base_work} - overseeing budget of ${self.budget:,.2f}"

        def approve_budget(self, amount):
            """Senior manager-specific method."""
            if amount > self.budget:
                return f"Cannot approve ${amount:,.2f} - exceeds budget of ${self.budget:,.2f}"
            return f"Budget of ${amount:,.2f} approved"

        def add_project(self, project_name):
            """Senior manager-specific method."""
            self.projects.append(project_name)
            return (
                f"Added project: {project_name}. Total projects: {len(self.projects)}"
            )

        def get_info(self):
            """Override get_info for senior managers."""
            base_info = super().get_info()
            return f"{base_info}, Budget: ${self.budget:,.2f}, Projects: {len(self.projects)}"

    class Executive(SeniorManager):
        """Executive class that inherits from SeniorManager."""

        def __init__(
            self,
            name,
            employee_id,
            salary,
            department,
            team_size,
            budget,
            stock_options,
        ):
            super().__init__(name, employee_id, salary, department, team_size, budget)
            self.stock_options = stock_options

        def work(self):
            """Override work method for executives."""
            base_work = super().work()
            return f"{base_work} - making strategic decisions"

        def make_decision(self, decision):
            """Executive-specific method."""
            return f"{self.name} made executive decision: {decision}"

        def get_info(self):
            """Override get_info for executives."""
            base_info = super().get_info()
            return f"{base_info}, Stock options: {self.stock_options}"

    print("\nMultilevel inheritance example:")

    # Create employees at different levels
    employees = [
        Employee("John Doe", "E001", 50000),
        Manager("Jane Smith", "M001", 80000, "Engineering", 10),
        SeniorManager("Bob Johnson", "SM001", 120000, "Product", 25, 1000000),
        Executive("Alice Brown", "EX001", 200000, "Corporate", 100, 5000000, 10000),
    ]

    for employee in employees:
        print(f"\n  {employee.get_info()}")
        print(f"    Work: {employee.work()}")
        print(f"    Pay: {employee.get_paid()}")

        # Type-specific behaviors
        if isinstance(employee, Manager):
            print(f"    Meeting: {employee.conduct_meeting()}")

        if isinstance(employee, SeniorManager):
            print(f"    Budget: {employee.approve_budget(50000)}")
            print(f"    Project: {employee.add_project('New Initiative')}")

        if isinstance(employee, Executive):
            print(f"    Decision: {employee.make_decision('Expand to new markets')}")


def exercise_4_shapes_hierarchy():
    """
    Create a geometric shapes hierarchy.

    1. Create base Shape class
    2. Create derived classes for different shapes
    3. Demonstrate polymorphism with area and perimeter calculations
    """

    class Shape:
        """Base class for all geometric shapes."""

        def __init__(self, name, color="black"):
            self.name = name
            self.color = color

        def area(self):
            """Calculate area - to be implemented by subclasses."""
            raise NotImplementedError("Subclasses must implement area()")

        def perimeter(self):
            """Calculate perimeter - to be implemented by subclasses."""
            raise NotImplementedError("Subclasses must implement perimeter()")

        def describe(self):
            """Describe the shape."""
            return f"A {self.color} {self.name}"

        def scale(self, factor):
            """Scale the shape - to be implemented by subclasses."""
            raise NotImplementedError("Subclasses must implement scale()")

    class Circle(Shape):
        """Circle class that inherits from Shape."""

        def __init__(self, radius, color="red"):
            super().__init__("Circle", color)
            self.radius = radius

        def area(self):
            """Calculate area of circle."""
            return math.pi * self.radius**2

        def perimeter(self):
            """Calculate circumference of circle."""
            return 2 * math.pi * self.radius

        def scale(self, factor):
            """Scale the circle."""
            if factor <= 0:
                raise ValueError("Scale factor must be positive")
            self.radius *= factor

        def describe(self):
            """Override describe for circles."""
            base_desc = super().describe()
            return f"{base_desc} with radius {self.radius}"

    class Rectangle(Shape):
        """Rectangle class that inherits from Shape."""

        def __init__(self, width, height, color="blue"):
            super().__init__("Rectangle", color)
            self.width = width
            self.height = height

        def area(self):
            """Calculate area of rectangle."""
            return self.width * self.height

        def perimeter(self):
            """Calculate perimeter of rectangle."""
            return 2 * (self.width + self.height)

        def scale(self, factor):
            """Scale the rectangle."""
            if factor <= 0:
                raise ValueError("Scale factor must be positive")
            self.width *= factor
            self.height *= factor

        def is_square(self):
            """Check if rectangle is a square."""
            return self.width == self.height

        def describe(self):
            """Override describe for rectangles."""
            base_desc = super().describe()
            shape = "Square" if self.is_square() else "Rectangle"
            return f"A {self.color} {shape} ({self.width}x{self.height})"

    class Triangle(Shape):
        """Triangle class that inherits from Shape."""

        def __init__(self, side1, side2, side3, color="green"):
            super().__init__("Triangle", color)
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3

        def perimeter(self):
            """Calculate perimeter of triangle."""
            return self.side1 + self.side2 + self.side3

        def area(self):
            """Calculate area of triangle using Heron's formula."""
            s = self.perimeter() / 2
            return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

        def scale(self, factor):
            """Scale the triangle."""
            if factor <= 0:
                raise ValueError("Scale factor must be positive")
            self.side1 *= factor
            self.side2 *= factor
            self.side3 *= factor

        def describe(self):
            """Override describe for triangles."""
            base_desc = super().describe()
            return f"{base_desc} with sides {self.side1}, {self.side2}, {self.side3}"

    print("\nShapes hierarchy example:")

    # Create shapes
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Rectangle(3, 3),  # This is a square
        Triangle(3, 4, 5),
    ]

    # Demonstrate polymorphism
    for shape in shapes:
        print(f"\n  {shape.describe()}")
        print(f"    Area: {shape.area():.2f}")
        print(f"    Perimeter: {shape.perimeter():.2f}")

        # Scale and show new calculations
        shape.scale(2)
        print("    After scaling by 2:")
        print(f"      New area: {shape.area():.2f}")
        print(f"      New perimeter: {shape.perimeter():.2f}")


def exercise_5_multiple_inheritance():
    """
    Demonstrate multiple inheritance.

    1. Create classes with multiple parent classes
    2. Show method resolution order (MRO)
    3. Handle diamond problem
    """

    class Printable:
        """Mixin class for printing functionality."""

        def print_info(self):
            """Print object information."""
            return f"Printing: {self}"

        def __str__(self):
            return "Printable object"

    class Savable:
        """Mixin class for saving functionality."""

        def save(self, filename):
            """Save object to file."""
            return f"Saving to {filename}"

        def load(self, filename):
            """Load object from file."""
            return f"Loading from {filename}"

    class Drawable:
        """Mixin class for drawing functionality."""

        def draw(self):
            """Draw the object."""
            return "Drawing object"

    class Document(Printable, Savable):
        """Document class that inherits from Printable and Savable."""

        def __init__(self, title, content):
            self.title = title
            self.content = content

        def __str__(self):
            return f"Document: {self.title}"

        def get_content(self):
            """Get document content."""
            return self.content

    class Image(Drawable, Savable):
        """Image class that inherits from Drawable and Savable."""

        def __init__(self, filename, width, height):
            self.filename = filename
            self.width = width
            self.height = height

        def __str__(self):
            return f"Image: {self.filename} ({self.width}x{self.height})"

        def draw(self):
            """Override draw for images."""
            base_draw = super().draw()
            return f"{base_draw} - displaying {self.filename}"

    class Report(Document, Drawable):
        """Report class that inherits from Document and Drawable."""

        def __init__(self, title, content, charts):
            super().__init__(title, content)
            self.charts = charts

        def __str__(self):
            return f"Report: {self.title} with {len(self.charts)} charts"

        def draw(self):
            """Override draw for reports."""
            base_draw = super().draw()
            return f"{base_draw} - including {len(self.charts)} charts"

    print("\nMultiple inheritance example:")

    # Create objects
    doc = Document("My Document", "This is some content.")
    img = Image("photo.jpg", 1920, 1080)
    report = Report(
        "Annual Report", "Financial analysis...", ["Chart1", "Chart2", "Chart3"]
    )

    objects = [doc, img, report]

    for obj in objects:
        print(f"\n  {obj}")

        # Check available methods
        if hasattr(obj, "print_info"):
            print(f"    Printable: {obj.print_info()}")

        if hasattr(obj, "save"):
            print(f"    Savable: {obj.save('backup.txt')}")

        if hasattr(obj, "draw"):
            print(f"    Drawable: {obj.draw()}")

        if hasattr(obj, "get_content"):
            print(f"    Content: {obj.get_content()[:30]}...")

        # Show MRO
        print(f"    MRO: {[cls.__name__ for cls in type(obj).__mro__]}")


def mini_project_vehicle_hierarchy_system():
    """
    Vehicle Hierarchy System

    A complete vehicle management system using inheritance.

    Features:
    1. Hierarchical vehicle classes
    2. Polymorphic behaviors
    3. Type-specific functionalities
    """

    # Use the Vehicle hierarchy from exercise 2
    class Vehicle:
        """Base class for all vehicles."""

        def __init__(self, make, model, year, fuel_type):
            self.make = make
            self.model = model
            self.year = year
            self.fuel_type = fuel_type
            self.speed = 0
            self.is_running = False
            self.mileage = 0

        def start(self):
            """Start the vehicle."""
            self.is_running = True
            return f"{self.make} {self.model} started."

        def stop(self):
            """Stop the vehicle."""
            self.is_running = False
            self.speed = 0
            return f"{self.make} {self.model} stopped."

        def drive(self, distance):
            """Drive the vehicle."""
            if not self.is_running:
                return "Cannot drive - vehicle is not running!"

            self.mileage += distance
            return f"Drove {distance} km. Total mileage: {self.mileage} km"

        def get_info(self):
            """Get vehicle information."""
            status = "running" if self.is_running else "stopped"
            return (
                f"{self.year} {self.make} {self.model} - "
                f"Fuel: {self.fuel_type}, Mileage: {self.mileage} km, Status: {status}"
            )

    class Car(Vehicle):
        """Car class that inherits from Vehicle."""

        def __init__(self, make, model, year, fuel_type, doors, transmission):
            super().__init__(make, model, year, fuel_type)
            self.doors = doors
            self.transmission = transmission
            self.passengers = 0

        def add_passenger(self):
            """Add a passenger to the car."""
            if self.passengers >= 4:  # Assuming 4 seats
                return "Car is full!"
            self.passengers += 1
            return f"Passenger added. Total passengers: {self.passengers}"

        def remove_passenger(self):
            """Remove a passenger from the car."""
            if self.passengers <= 0:
                return "No passengers to remove!"
            self.passengers -= 1
            return f"Passenger removed. Total passengers: {self.passengers}"

    class ElectricCar(Car):
        """Electric car class that inherits from Car."""

        def __init__(self, make, model, year, doors, transmission, battery_capacity):
            super().__init__(make, model, year, "Electric", doors, transmission)
            self.battery_capacity = battery_capacity  # in kWh
            self.battery_level = 100  # percentage

        def charge(self, amount):
            """Charge the electric car."""
            if amount <= 0:
                return "Charge amount must be positive."

            self.battery_level = min(100, self.battery_level + amount)
            return f"Charged to {self.battery_level}%"

        def get_range(self):
            """Calculate remaining range."""
            # Assuming 6 km per kWh
            remaining_kwh = self.battery_capacity * (self.battery_level / 100)
            return remaining_kwh * 6

        def drive(self, distance):
            """Override drive to account for battery usage."""
            range_km = self.get_range()

            if distance > range_km:
                return f"Cannot drive {distance} km. Only {range_km:.1f} km range available."

            # Use battery
            kwh_used = distance / 6
            self.battery_level -= (kwh_used / self.battery_capacity) * 100

            result = super().drive(distance)
            return f"{result}. Battery: {self.battery_level:.1f}%"

    class Truck(Vehicle):
        """Truck class that inherits from Vehicle."""

        def __init__(self, make, model, year, fuel_type, cargo_capacity):
            super().__init__(make, model, year, fuel_type)
            self.cargo_capacity = cargo_capacity  # in tons
            self.cargo = 0

        def load(self, weight):
            """Load cargo onto the truck."""
            available = self.cargo_capacity - self.cargo
            if weight > available:
                return f"Cannot load {weight} tons. Only {available:.1f} tons capacity available."

            self.cargo += weight
            return f"Loaded {weight} tons. Total cargo: {self.cargo:.1f}/{self.cargo_capacity} tons"

        def unload(self, weight):
            """Unload cargo from the truck."""
            if weight > self.cargo:
                return (
                    f"Cannot unload {weight} tons. Only {self.cargo:.1f} tons loaded."
                )

            self.cargo -= weight
            return f"Unloaded {weight} tons. Remaining cargo: {self.cargo:.1f}/{self.cargo_capacity} tons"

    print("=" * 60)
    print("VEHICLE HIERARCHY SYSTEM")
    print("=" * 60)

    # Create some vehicles
    vehicles = {
        "car1": Car("Toyota", "Camry", 2020, "Gasoline", 4, "Automatic"),
        "electric1": ElectricCar("Tesla", "Model 3", 2021, 4, "Automatic", 75),
        "truck1": Truck("Ford", "F-150", 2019, "Diesel", 2.5),
    }

    def display_vehicles():
        """Display all vehicles."""
        if not vehicles:
            print("No vehicles found.")
            return

        print("\nAll Vehicles:")
        print("-" * 50)
        for vehicle_id, vehicle in vehicles.items():
            print(f"{vehicle_id}: {vehicle.get_info()}")

    def create_vehicle():
        """Create a new vehicle."""
        print("\nCreate New Vehicle:")
        print("1. Car")
        print("2. Electric Car")
        print("3. Truck")

        try:
            choice = input("Enter vehicle type (1-3): ")

            vehicle_id = f"vehicle{len(vehicles) + 1:03d}"
            print(f"Generated vehicle ID: {vehicle_id}")

            make = input("Make: ").strip()
            model = input("Model: ").strip()
            year = int(input("Year: "))

            if choice == "1":  # Car
                fuel_type = input("Fuel type: ").strip()
                doors = int(input("Number of doors: "))
                transmission = input("Transmission: ").strip()

                vehicle = Car(make, model, year, fuel_type, doors, transmission)

            elif choice == "2":  # Electric Car
                doors = int(input("Number of doors: "))
                transmission = input("Transmission: ").strip()
                battery_capacity = float(input("Battery capacity (kWh): "))

                vehicle = ElectricCar(
                    make, model, year, doors, transmission, battery_capacity
                )

            elif choice == "3":  # Truck
                fuel_type = input("Fuel type: ").strip()
                cargo_capacity = float(input("Cargo capacity (tons): "))

                vehicle = Truck(make, model, year, fuel_type, cargo_capacity)

            else:
                print("Invalid choice.")
                return

            vehicles[vehicle_id] = vehicle
            print("Vehicle created successfully!")
            print(f"{vehicle.get_info()}")

        except ValueError:
            print("Invalid input.")

    print(f"Loaded {len(vehicles)} vehicle(s).")

    while True:
        print("\nMain Menu:")
        print("1. View all vehicles")
        print("2. Create new vehicle")
        print("3. Operate vehicle")
        print("4. Vehicle-specific actions")
        print("0. Exit")

        try:
            choice = input("\nEnter your choice (0-4): ")

            if choice == "0":
                print("Exiting Vehicle System. Goodbye!")
                break

            elif choice == "1":
                display_vehicles()

            elif choice == "2":
                create_vehicle()

            elif choice in ["3", "4"]:
                # Need to select a vehicle
                vehicle_id = input("Enter vehicle ID: ")
                vehicle = vehicles.get(vehicle_id)

                if not vehicle:
                    print(f"Vehicle {vehicle_id} not found.")
                    continue

                if choice == "3":  # Operate vehicle
                    print(f"\nOperating {vehicle.make} {vehicle.model}:")
                    print("  1. Start")
                    print("  2. Stop")
                    print("  3. Drive")

                    op_choice = input("Enter operation (1-3): ")

                    if op_choice == "1":
                        print(f"  {vehicle.start()}")
                    elif op_choice == "2":
                        print(f"  {vehicle.stop()}")
                    elif op_choice == "3":
                        try:
                            distance = float(input("Distance to drive (km): "))
                            print(f"  {vehicle.drive(distance)}")
                        except ValueError:
                            print("Invalid distance.")
                    else:
                        print("Invalid operation.")

                elif choice == "4":  # Vehicle-specific actions
                    print(
                        f"\nVehicle-specific actions for {vehicle.make} {vehicle.model}:"
                    )

                    if isinstance(vehicle, Car):
                        print("  1. Add passenger")
                        print("  2. Remove passenger")

                        action = input("Enter action (1-2): ")

                        if action == "1":
                            print(f"  {vehicle.add_passenger()}")
                        elif action == "2":
                            print(f"  {vehicle.remove_passenger()}")
                        else:
                            print("Invalid action.")

                    elif isinstance(vehicle, ElectricCar):
                        print("  1. Charge battery")
                        print("  2. Check range")

                        action = input("Enter action (1-2): ")

                        if action == "1":
                            try:
                                amount = float(input("Charge amount (%): "))
                                print(f"  {vehicle.charge(amount)}")
                            except ValueError:
                                print("Invalid amount.")
                        elif action == "2":
                            range_km = vehicle.get_range()
                            print(f"  Remaining range: {range_km:.1f} km")
                        else:
                            print("Invalid action.")

                    elif isinstance(vehicle, Truck):
                        print("  1. Load cargo")
                        print("  2. Unload cargo")

                        action = input("Enter action (1-2): ")

                        if action == "1":
                            try:
                                weight = float(input("Weight to load (tons): "))
                                print(f"  {vehicle.load(weight)}")
                            except ValueError:
                                print("Invalid weight.")
                        elif action == "2":
                            try:
                                weight = float(input("Weight to unload (tons): "))
                                print(f"  {vehicle.unload(weight)}")
                            except ValueError:
                                print("Invalid weight.")
                        else:
                            print("Invalid action.")

            else:
                print("Invalid choice. Please enter 0-4.")

        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def run_all_exercises():
    """Run all Day 16 exercises."""
    print("=" * 60)
    print("Week 3, Day 16: Inheritance")
    print("=" * 60)

    print("\n--- Exercise 1: Basic Inheritance ---")
    exercise_1_basic_inheritance()

    print("\n--- Exercise 2: Vehicle Hierarchy ---")
    exercise_2_vehicle_hierarchy()

    print("\n--- Exercise 3: Multilevel Inheritance ---")
    exercise_3_multilevel_inheritance()

    print("\n--- Exercise 4: Shapes Hierarchy ---")
    exercise_4_shapes_hierarchy()

    print("\n--- Exercise 5: Multiple Inheritance ---")
    exercise_5_multiple_inheritance()

    print("\n" + "=" * 60)
    print("Mini Project: Vehicle Hierarchy System")
    print("=" * 60)
    mini_project_vehicle_hierarchy_system()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 16 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
