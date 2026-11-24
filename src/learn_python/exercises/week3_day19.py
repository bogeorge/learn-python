import importlib.util
import os
import sys

"""
Week 3, Day 19: Modules & Packages

Exercises to practice import statements, creating modules, 
__name__ == "__main__" pattern, and virtual environments.
"""

# Note: This file demonstrates module concepts but some exercises
# require creating separate module files. We'll simulate some aspects.


def exercise_1_import_statements():
    """
    Practice different import statement patterns.

    1. Import entire module
    2. Import specific items
    3. Import with aliases
    4. Relative imports
    """

    print("Import statement patterns:")

    # Simulating imports by showing what would happen
    print("\n  1. Import entire module:")
    print("     import math")
    print("     result = math.sqrt(16)  # Returns 4.0")

    print("\n  2. Import specific items:")
    print("     from math import sqrt, pi")
    print("     result = sqrt(16)  # Returns 4.0")
    print("     circle_area = pi * 5**2")

    print("\n  3. Import with alias:")
    print("     import numpy as np")
    print("     import pandas as pd")
    print("     import matplotlib.pyplot as plt")

    print("\n  4. Import everything (not recommended):")
    print("     from math import *")
    print("     result = sqrt(16) + sin(pi/2)")

    print("\n  5. Conditional imports:")
    try:
        # Try to import a module that might not be installed
        import requests

        print("     'requests' module is available")
    except ImportError:
        print("     'requests' module is not installed")

    # Demonstrate actual imports
    import math
    import random as rnd
    from datetime import date

    print("\n  6. Actual import examples:")
    print(f"     math.sqrt(25) = {math.sqrt(25)}")
    print(f"     Current date: {date.today()}")
    print(f"     Random number: {rnd.randint(1, 100)}")


def exercise_2_creating_modules():
    """
    Create and use custom modules.

    1. Create a utility module
    2. Import and use it
    3. Show module attributes
    """

    # First, let's create a simple module file
    module_content = '''
"""
geometry.py - A simple geometry module
"""

import math

PI = math.pi

def circle_area(radius):
    """Calculate area of a circle."""
    return PI * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of a circle."""
    return 2 * PI * radius

def rectangle_area(width, height):
    """Calculate area of a rectangle."""
    return width * height

def rectangle_perimeter(width, height):
    """Calculate perimeter of a rectangle."""
    return 2 * (width + height)

def triangle_area(base, height):
    """Calculate area of a triangle."""
    return 0.5 * base * height

def hypotenuse(a, b):
    """Calculate hypotenuse of a right triangle."""
    return math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    # Test code when run directly
    print("Testing geometry module:")
    print(f"Circle area (r=5): {circle_area(5):.2f}")
    print(f"Rectangle area (4x6): {rectangle_area(4, 6)}")
    print(f"Hypotenuse (3, 4): {hypotenuse(3, 4)}")
'''

    # Write the module file
    module_path = (
        "/tmp/geometry.py" if sys.platform != "win32" else "C:\\temp\\geometry.py"
    )

    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(module_path), exist_ok=True)

        with open(module_path, "w") as f:
            f.write(module_content)

        # Now demonstrate importing it
        print("Creating and using custom modules:")

        # Method 1: Using importlib
        spec = importlib.util.spec_from_file_location("geometry", module_path)
        geometry = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(geometry)

        print("\n  1. Imported geometry module:")
        print(f"     Circle area (radius=3): {geometry.circle_area(3):.2f}")
        print(f"     Rectangle perimeter (4x5): {geometry.rectangle_perimeter(4, 5)}")
        print(f"     Triangle area (base=6, height=4): {geometry.triangle_area(6, 4)}")

        # Method 2: Adding to sys.path and importing
        print("\n  2. Module attributes:")
        print(f"     Module name: {geometry.__name__}")
        print(f"     File location: {geometry.__file__}")
        print(f"     Module documentation: {geometry.__doc__.strip()}")
        print(
            f"     Available functions: {[name for name in dir(geometry) if not name.startswith('_')]}"
        )

        # Clean up
        os.remove(module_path)

    except Exception as e:
        print(f"  Note: Could not create temp module file: {e}")
        print("  Demonstrating module concepts instead...")

        # Fallback demonstration
        print("\n  Module creation concepts:")
        print("  1. Create a .py file with functions and classes")
        print("  2. Save it in your project directory or Python path")
        print("  3. Import it using: import module_name")
        print("  4. Use its functions: module_name.function_name()")


def exercise_3_name_main_pattern():
    """
    Demonstrate __name__ == "__main__" pattern.

    1. Show how it works
    2. Create reusable modules
    3. Demonstrate testing code
    """

    # Create a module that demonstrates the pattern
    module_content = '''
"""
calculator.py - A reusable calculator module
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test code that only runs when module is executed directly
if __name__ == "__main__":
    print("Running calculator tests...")
    
    # Test cases
    test_cases = [
        (add, 5, 3, 8),
        (subtract, 10, 4, 6),
        (multiply, 7, 6, 42),
        (divide, 15, 3, 5),
    ]
    
    all_passed = True
    for func, a, b, expected in test_cases:
        try:
            result = func(a, b)
            if result == expected:
                print(f"  ✓ {func.__name__}({a}, {b}) = {result}")
            else:
                print(f"  ✗ {func.__name__}({a}, {b}) = {result} (expected {expected})")
                all_passed = False
        except Exception as e:
            print(f"  ✗ {func.__name__}({a}, {b}) failed: {e}")
            all_passed = False
    
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")
    
    print("\\nModule can be imported without running tests.")
'''

    print("\n__name__ == '__main__' pattern:")

    # Create and run the module
    module_path = (
        "/tmp/calculator.py" if sys.platform != "win32" else "C:\\temp\\calculator.py"
    )

    try:
        os.makedirs(os.path.dirname(module_path), exist_ok=True)

        with open(module_path, "w") as f:
            f.write(module_content)

        print("\n  1. When run directly:")
        print("     $ python calculator.py")

        # Execute the module
        spec = importlib.util.spec_from_file_location("calculator", module_path)
        calculator_module = importlib.util.module_from_spec(spec)

        # Capture output
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            spec.loader.exec_module(calculator_module)
        output = f.getvalue()

        print("     Output:")
        for line in output.strip().split("\n"):
            print(f"       {line}")

        print("\n  2. When imported:")
        print("     import calculator")
        print("     result = calculator.add(10, 20)")
        print(f"     Result would be: {calculator_module.add(10, 20)}")

        print("\n  3. Checking __name__:")
        print(f"     When run directly: __name__ = '{calculator_module.__name__}'")

        # Clean up
        os.remove(module_path)

    except Exception as e:
        print(f"  Note: Could not create temp module: {e}")
        print("\n  Key concepts:")
        print("  1. __name__ is '__main__' when file is run directly")
        print("  2. __name__ is the module name when imported")
        print("  3. Use if __name__ == '__main__': for test code")
        print("  4. This allows modules to be both imported and run directly")


def exercise_4_packages_structure():
    """
    Demonstrate package structure and organization.

    1. Create package directory structure
    2. Use __init__.py files
    3. Demonstrate subpackage imports
    """

    print("\nPackage structure and organization:")

    # Explain package structure
    print("\n  1. Basic package structure:")
    print("     mypackage/")
    print("     ├── __init__.py")
    print("     ├── module1.py")
    print("     ├── module2.py")
    print("     └── subpackage/")
    print("         ├── __init__.py")
    print("         └── module3.py")

    print("\n  2. __init__.py files:")
    print("     - Make directories Python packages")
    print("     - Can be empty or contain initialization code")
    print("     - Can define what gets imported with 'from package import *'")

    print("\n  3. Import examples:")
    print("     import mypackage.module1")
    print("     from mypackage import module2")
    print("     from mypackage.subpackage import module3")

    print("\n  4. Relative imports (inside packages):")
    print("     from . import module1  # Import from same package")
    print("     from .. import parent_module  # Import from parent package")
    print("     from .subpackage import module3  # Import from subpackage")

    # Create a simple example structure
    print("\n  5. Example: Creating a math utilities package")

    # Create temporary package structure
    temp_dir = "/tmp/mymath" if sys.platform != "win32" else "C:\\temp\\mymath"

    try:
        # Clean up if exists
        import shutil

        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

        # Create directory structure
        os.makedirs(temp_dir)
        os.makedirs(os.path.join(temp_dir, "geometry"))
        os.makedirs(os.path.join(temp_dir, "algebra"))

        # Create __init__.py files
        with open(os.path.join(temp_dir, "__init__.py"), "w") as f:
            f.write('''"""
mymath - A mathematics utilities package.
"""

__version__ = "1.0.0"
__author__ = "Python Learner"

# Expose commonly used functions
from .geometry.circles import circle_area
from .geometry.rectangles import rectangle_area
from .algebra.basic import add, multiply

print(f"Initializing mymath package v{__version__}")
''')

        # Create geometry/__init__.py
        with open(os.path.join(temp_dir, "geometry", "__init__.py"), "w") as f:
            f.write('''"""
Geometry subpackage.
"""
from .circles import *
from .rectangles import *
''')

        # Create geometry/circles.py
        with open(os.path.join(temp_dir, "geometry", "circles.py"), "w") as f:
            f.write('''"""
Circle geometry functions.
"""
import math

def circle_area(radius):
    """Calculate area of a circle."""
    return math.pi * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of a circle."""
    return 2 * math.pi * radius
''')

        # Create geometry/rectangles.py
        with open(os.path.join(temp_dir, "geometry", "rectangles.py"), "w") as f:
            f.write('''"""
Rectangle geometry functions.
"""

def rectangle_area(width, height):
    """Calculate area of a rectangle."""
    return width * height

def rectangle_perimeter(width, height):
    """Calculate perimeter of a rectangle."""
    return 2 * (width + height)
''')

        # Create algebra/__init__.py
        with open(os.path.join(temp_dir, "algebra", "__init__.py"), "w") as f:
            f.write('''"""
Algebra subpackage.
"""
from .basic import *
''')

        # Create algebra/basic.py
        with open(os.path.join(temp_dir, "algebra", "basic.py"), "w") as f:
            f.write('''"""
Basic algebra functions.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def power(base, exponent):
    """Calculate base raised to exponent."""
    return base ** exponent
''')

        # Add to Python path and import
        import sys

        sys.path.insert(0, os.path.dirname(temp_dir))

        print(f"\n    Created package at: {temp_dir}")
        print("    Package structure created successfully.")

        # Import and use the package
        import mymath

        print("\n    Using the package:")
        print(f"      mymath.circle_area(5): {mymath.circle_area(5):.2f}")
        print(f"      mymath.rectangle_area(4, 6): {mymath.rectangle_area(4, 6)}")
        print(f"      mymath.add(10, 20): {mymath.add(10, 20)}")

        # Import submodules directly
        from mymath.algebra import basic
        from mymath.geometry import circles, rectangles

        print("\n    Using submodules:")
        print(
            f"      circles.circle_circumference(3): {circles.circle_circumference(3):.2f}"
        )
        print(
            f"      rectangles.rectangle_perimeter(4, 5): {rectangles.rectangle_perimeter(4, 5)}"
        )
        print(f"      basic.power(2, 8): {basic.power(2, 8)}")

        # Clean up
        shutil.rmtree(temp_dir)
        sys.path.pop(0)  # Remove temp path

    except Exception as e:
        print(f"  Note: Could not create temp package: {e}")
        print("\n  Key package concepts:")
        print("  1. Packages are directories with __init__.py")
        print("  2. Subpackages are subdirectories with their own __init__.py")
        print("  3. Use dot notation for imports: import package.subpackage.module")
        print("  4. __init__.py controls what's exported from the package")


def exercise_5_virtual_environments():
    """
    Demonstrate virtual environment concepts.

    1. Explain virtual environments
    2. Show requirements.txt
    3. Demonstrate dependency management
    """

    print("\nVirtual environments and dependency management:")

    print("\n  1. What are virtual environments?")
    print("     - Isolated Python environments")
    print("     - Separate dependencies for different projects")
    print("     - Avoid version conflicts")

    print("\n  2. Creating virtual environments:")
    print("     python -m venv venv               # Create")
    print("     source venv/bin/activate          # Activate (Linux/Mac)")
    print("     venv\\Scripts\\activate           # Activate (Windows)")
    print("     deactivate                        # Deactivate")

    print("\n  3. Managing dependencies:")
    print("     pip install package_name          # Install")
    print("     pip install -r requirements.txt   # Install from file")
    print("     pip freeze > requirements.txt     # Save dependencies")
    print("     pip list                          # List installed")
    print("     pip uninstall package_name        # Uninstall")

    print("\n  4. Example requirements.txt:")
    requirements_example = """# Project dependencies
# Format: package_name==version

# Web framework
flask==2.3.2

# Database
sqlalchemy==2.0.19
psycopg2-binary==2.9.7

# Data processing
pandas==2.0.3
numpy==1.24.3

# Testing
pytest==7.4.0
pytest-cov==4.1.0

# Development tools
black==23.7.0
flake8==6.0.0
"""

    print("     " + "\n     ".join(requirements_example.split("\n")))

    print("\n  5. Best practices:")
    print("     - Always use virtual environments")
    print("     - Include requirements.txt in version control")
    print("     - Pin versions for production (package==1.2.3)")
    print("     - Use ~= for compatible releases (package~=1.2)")
    print("     - Separate dev and prod requirements")

    print("\n  6. Advanced tools:")
    print("     - pipenv: Combines pip and virtualenv")
    print("     - poetry: Modern dependency management")
    print("     - conda: Package and environment manager")
    print("     - docker: Containerization for reproducibility")


def mini_project_modular_game_application():
    """
    Modular Game Application

    A game application organized into modules and packages.

    Features:
    1. Modular architecture
    2. Separate modules for different game components
    3. Package structure
    4. Main game loop
    """

    print("=" * 60)
    print("MODULAR GAME APPLICATION")
    print("=" * 60)

    # Create a simple modular game structure in memory
    print("\nGame Module Structure:")
    print("  game/")
    print("  ├── __init__.py")
    print("  ├── main.py")
    print("  ├── player.py")
    print("  ├── enemy.py")
    print("  ├── items.py")
    print("  └── combat.py")

    # Simulate the modules
    class Player:
        """Player module."""

        def __init__(self, name, health=100, attack=10):
            self.name = name
            self.health = health
            self.attack = attack
            self.inventory = []
            self.level = 1
            self.experience = 0

        def take_damage(self, damage):
            """Take damage."""
            self.health -= damage
            self.health = max(self.health, 0)
            return self.health > 0

        def heal(self, amount):
            """Heal the player."""
            self.health += amount
            self.health = min(self.health, 100)

        def add_item(self, item):
            """Add item to inventory."""
            self.inventory.append(item)

        def gain_experience(self, xp):
            """Gain experience points."""
            self.experience += xp
            if self.experience >= self.level * 100:
                self.level_up()

        def level_up(self):
            """Level up the player."""
            self.level += 1
            self.experience = 0
            self.health = 100
            self.attack += 5
            return f"{self.name} leveled up to level {self.level}!"

        def __str__(self):
            return (
                f"{self.name} (Lvl {self.level}, HP: {self.health}, ATK: {self.attack})"
            )

    class Enemy:
        """Enemy module."""

        def __init__(self, name, health, attack, xp_reward):
            self.name = name
            self.health = health
            self.attack = attack
            self.xp_reward = xp_reward
            self.is_alive = True

        def take_damage(self, damage):
            """Take damage."""
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.is_alive = False
            return self.is_alive

        def __str__(self):
            status = "Alive" if self.is_alive else "Defeated"
            return (
                f"{self.name} (HP: {self.health}, ATK: {self.attack}, Status: {status})"
            )

    class Item:
        """Items module."""

        def __init__(self, name, item_type, value):
            self.name = name
            self.type = item_type  # 'weapon', 'armor', 'potion', 'key'
            self.value = value

        def use(self, player):
            """Use the item."""
            if self.type == "potion":
                player.heal(self.value)
                return f"{player.name} used {self.name} and healed {self.value} HP."
            elif self.type == "weapon":
                player.attack += self.value
                return f"{player.name} equipped {self.name} (+{self.value} ATK)."
            return f"{self.name} has no use effect."

        def __str__(self):
            return f"{self.name} ({self.type}, Value: {self.value})"

    class Combat:
        """Combat module."""

        @staticmethod
        def attack(attacker, defender):
            """Perform an attack."""
            damage = attacker.attack
            is_alive = defender.take_damage(damage)

            result = f"{attacker.name} attacks {defender.name} for {damage} damage."
            if not is_alive:
                result += f" {defender.name} is defeated!"

            return result, is_alive

        @staticmethod
        def battle(player, enemy):
            """Simulate a battle."""
            print(f"\nBattle: {player.name} vs {enemy.name}")
            print("-" * 30)

            round_num = 1
            while player.health > 0 and enemy.is_alive:
                print(f"\nRound {round_num}:")

                # Player attacks
                result, enemy_alive = Combat.attack(player, enemy)
                print(f"  {result}")

                if not enemy_alive:
                    print(f"\nVictory! {player.name} defeated {enemy.name}")
                    player.gain_experience(enemy.xp_reward)
                    return True

                # Enemy attacks
                result, player_alive = Combat.attack(enemy, player)
                print(f"  {result}")

                if not player_alive:
                    print(f"\nDefeat! {player.name} was defeated by {enemy.name}")
                    return False

                print(
                    f"  Status: {player.name} HP: {player.health}, {enemy.name} HP: {enemy.health}"
                )
                round_num += 1

            return False

    # Main game simulation
    print("\nStarting game simulation...")

    # Create player
    player = Player("Hero")
    print(f"Player created: {player}")

    # Create items
    items = [
        Item("Health Potion", "potion", 30),
        Item("Iron Sword", "weapon", 5),
        Item("Magic Amulet", "armor", 3),
    ]

    # Give player starting items
    player.add_item(items[0])
    player.add_item(items[1])
    print("\nStarting items:")
    for item in player.inventory:
        print(f"  {item}")

    # Use a potion
    print(f"\n{item.use(player)}")
    print(f"Player after potion: {player}")

    # Create enemies
    enemies = [
        Enemy("Goblin", 30, 5, 50),
        Enemy("Orc", 60, 10, 100),
        Enemy("Dragon", 150, 20, 300),
    ]

    # Battle sequence
    print("\n" + "=" * 40)
    print("ADVENTURE BEGINS")
    print("=" * 40)

    game_running = True
    enemy_index = 0

    while game_running and enemy_index < len(enemies):
        enemy = enemies[enemy_index]

        # Offer to use items before battle
        if player.inventory:
            print("\nItems available:")
            for i, item in enumerate(player.inventory, 1):
                print(f"  {i}. {item}")

            use_item = input(f"\nUse an item before battling {enemy.name}? (y/n): ")
            if use_item.lower() == "y":
                try:
                    item_num = int(input("Item number: ")) - 1
                    if 0 <= item_num < len(player.inventory):
                        item = player.inventory.pop(item_num)
                        print(item.use(player))
                except ValueError, IndexError:
                    print("Invalid item selection.")

        # Start battle
        victory = Combat.battle(player, enemy)

        if victory:
            enemy_index += 1
            print(f"\nPlayer status: {player}")

            if enemy_index < len(enemies):
                continue_battle = input("\nContinue to next enemy? (y/n): ")
                if continue_battle.lower() != "y":
                    game_running = False
            else:
                print("\n🎉 CONGRATULATIONS! You defeated all enemies!")
                game_running = False
        else:
            print("\n💀 GAME OVER")
            game_running = False

    print("\n" + "=" * 40)
    print("FINAL STATS")
    print("=" * 40)
    print(player)
    print(f"Inventory: {len(player.inventory)} items")
    print(f"Experience: {player.experience} XP")

    print("\nGame modules demonstrated:")
    print("  1. player.py - Player class with stats and inventory")
    print("  2. enemy.py - Enemy class with combat stats")
    print("  3. items.py - Item system with different types")
    print("  4. combat.py - Battle mechanics")
    print("  5. main.py - Game loop and module integration")


def run_all_exercises():
    """Run all Day 19 exercises."""
    print("=" * 60)
    print("Week 3, Day 19: Modules & Packages")
    print("=" * 60)

    print("\n--- Exercise 1: Import Statements ---")
    exercise_1_import_statements()

    print("\n--- Exercise 2: Creating Modules ---")
    exercise_2_creating_modules()

    print("\n--- Exercise 3: Name-Main Pattern ---")
    exercise_3_name_main_pattern()

    print("\n--- Exercise 4: Packages Structure ---")
    exercise_4_packages_structure()

    print("\n--- Exercise 5: Virtual Environments ---")
    exercise_5_virtual_environments()

    print("\n" + "=" * 60)
    print("Mini Project: Modular Game Application")
    print("=" * 60)
    mini_project_modular_game_application()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 19 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
