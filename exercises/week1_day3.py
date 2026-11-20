import sys

"""
Week 1, Day 3: Input & Conditional Statements

Exercises to practice getting user input and making decisions with if/elif/else.
"""


def exercise_1_user_input():
    """
    Practice getting input from the user.
    
    1. Ask the user for their name
    2. Ask for their age (convert to integer)
    3. Ask for their favourite number (convert to float)
    4. Print a summary using an f-string
    """
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    favourite_number = float(input("What is your favourite number? "))

    print(f"\nHello {name}! You are {age} years old and your favourite number is {favourite_number}.")


def exercise_2_age_verification():
    """
    Ask the user for their age and print a message based on the result.
    
    - Under 13: "You are a child."
    - 13–17: "You are a teenager."
    - 18–64: "You are an adult."
    - 65 and over: "You are a senior."
    """
    age = int(input("Enter your age: "))

    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior.")


def exercise_3_number_comparison():
    """
    Ask the user for two numbers and compare them.
    
    Print which is larger, or whether they are equal.
    Also print whether each number is positive, negative, or zero.
    """
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    # Compare the two numbers
    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} and {b} are equal")

    # Check sign of each number
    for label, number in [("First number", a), ("Second number", b)]:
        if number > 0:
            print(f"{label} ({number}) is positive")
        elif number < 0:
            print(f"{label} ({number}) is negative")
        else:
            print(f"{label} ({number}) is zero")


def exercise_4_grade_calculator():
    """
    Ask the user for a score (0–100) and print the corresponding letter grade.
    
    - 90–100: A
    - 80–89:  B
    - 70–79:  C
    - 60–69:  D
    - Below 60: F
    
    Also print a short message for each grade.
    """
    score = float(input("Enter your score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
        return

    if score >= 90:
        grade = "A"
        message = "Excellent work!"
    elif score >= 80:
        grade = "B"
        message = "Good job!"
    elif score >= 70:
        grade = "C"
        message = "Satisfactory."
    elif score >= 60:
        grade = "D"
        message = "Needs improvement."
    else:
        grade = "F"
        message = "Please see your instructor."

    print(f"\nScore: {score}")
    print(f"Grade: {grade}")
    print(message)


def exercise_5_comparison_operators():
    """
    Demonstrate all comparison and logical operators.
    
    Create two integer variables and print the result of every
    comparison, then combine them with and/or/not.
    """
    a = 15
    b = 10

    print(f"a = {a}, b = {b}")
    print()

    # Comparison operators
    print("Comparison operators:")
    print(f"  a == b  : {a == b}")
    print(f"  a != b  : {a != b}")
    print(f"  a >  b  : {a > b}")
    print(f"  a <  b  : {a < b}")
    print(f"  a >= b  : {a >= b}")
    print(f"  a <= b  : {a <= b}")
    print()

    # Logical operators
    print("Logical operators:")
    print(f"  a > 5 and b > 5   : {a > 5 and b > 5}")
    print(f"  a > 20 or b > 5   : {a > 20 or b > 5}")
    print(f"  not a > 20        : {not a > 20}")
    print()

    # Combined
    print("Combined expressions:")
    is_between = 5 < a < 20
    print(f"  5 < a < 20        : {is_between}")

    either_large = a > 100 or b > 100
    print(f"  a > 100 or b > 100: {either_large}")


def mini_project_login_system():
    """
    A simple login system.
    
    - Store a username and password (hardcoded for practice)
    - Ask the user for their credentials
    - Allow up to 3 attempts before locking them out
    - Print an appropriate message for success or failure
    """
    print("=" * 40)
    print("SIMPLE LOGIN SYSTEM")
    print("=" * 40)

    correct_username = "bo"
    correct_password = "python123"
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}")
        username = input("Username: ")
        password = input("Password: ")

        if username == correct_username and password == correct_password:
            print("\n✅ Login successful! Welcome, Bo.")
            return
        elif username != correct_username:
            print("❌ Unknown username.")
        else:
            print("❌ Incorrect password.")

        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"{remaining} attempt(s) remaining.")

    print("\n🔒 Account locked. Too many failed attempts.")


def run_all_exercises():
    """Run all Day 3 exercises."""
    print("=" * 60)
    print("Week 1, Day 3: Input & Conditional Statements")
    print("=" * 60)

    print("\n--- Exercise 1: User Input ---")
    exercise_1_user_input()

    print("\n--- Exercise 2: Age Verification ---")
    exercise_2_age_verification()

    print("\n--- Exercise 3: Number Comparison ---")
    exercise_3_number_comparison()

    print("\n--- Exercise 4: Grade Calculator ---")
    exercise_4_grade_calculator()

    print("\n--- Exercise 5: Comparison Operators ---")
    exercise_5_comparison_operators()

    print("\n" + "=" * 60)
    print("Mini Project: Login System")
    print("=" * 60)
    mini_project_login_system()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 3 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Run {func_name}")
        globals()[func_name]()
    else:
        print("Run em all")
        run_all_exercises()
