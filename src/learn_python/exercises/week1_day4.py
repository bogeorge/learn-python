import sys

"""
Week 1, Day 4: Loops Part 1

Exercises to practice while loops and for loops with range().
"""


def exercise_1_while_loop_basics():
    """
    Demonstrate a basic while loop.

    Count from 1 to 10, printing each number.
    Then count down from 10 to 1.
    """
    print("Counting up:")
    count = 1
    while count <= 10:
        print(f"  {count}")
        count += 1

    print("\nCounting down:")
    count = 10
    while count >= 1:
        print(f"  {count}")
        count -= 1
    print("  Blast off! 🚀")


def exercise_2_for_loop_basics():
    """
    Demonstrate for loops with range().

    1. Print numbers 0–9
    2. Print even numbers from 0–20
    3. Print numbers 10 down to 1 using range() with a step
    """
    print("Numbers 0–9:")
    for i in range(10):
        print(f"  {i}", end=" ")
    print()

    print("\nEven numbers 0–20:")
    for i in range(0, 21, 2):
        print(f"  {i}", end=" ")
    print()

    print("\nCountdown 10–1:")
    for i in range(10, 0, -1):
        print(f"  {i}", end=" ")
    print()


def exercise_3_countdown_timer():
    """
    Ask the user for a number and count down from it to zero,
    printing each value. Print "Done!" when finished.
    """
    start = int(input("Enter a number to count down from: "))

    if start < 0:
        print("Please enter a positive number.")
        return

    count = start
    while count >= 0:
        print(f"  {count}")
        count -= 1

    print("Done!")


def exercise_4_multiplication_table():
    """
    Ask the user for a number and print its multiplication table up to 12.

    Example for 5:
        5 x  1 =  5
        5 x  2 = 10
        ...
        5 x 12 = 60
    """
    number = int(input("Enter a number to generate its multiplication table: "))

    print(f"\nMultiplication table for {number}:")
    print("-" * 20)
    for i in range(1, 13):
        print(f"  {number} x {i:2} = {number * i:3}")


def exercise_5_sum_of_range():
    """
    Ask the user for a start and end number, then calculate:
    1. The sum of all integers in that range (inclusive)
    2. The sum of even numbers only
    3. The sum of odd numbers only

    Print all three results.
    """
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))

    if start > end:
        start, end = end, start  # Swap if entered in the wrong order

    total = 0
    even_total = 0
    odd_total = 0

    for i in range(start, end + 1):
        total += i
        if i % 2 == 0:
            even_total += i
        else:
            odd_total += i

    print(f"\nRange: {start} to {end}")
    print(f"  Sum of all numbers : {total}")
    print(f"  Sum of even numbers: {even_total}")
    print(f"  Sum of odd numbers : {odd_total}")


def mini_project_guessing_game():
    """
    A number guessing game (1–100).

    - The computer picks a random number between 1 and 100
    - The user has 10 attempts to guess it
    - After each guess, print "Too high", "Too low", or "Correct!"
    - At the end, print how many attempts were used

    Note: this is a simpler version than the full project in
    projects/beginner/02_number_guessing_game.py — the goal here
    is to practice loops, not build a full game.
    """
    import random

    print("=" * 40)
    print("NUMBER GUESSING GAME (1–100)")
    print("=" * 40)

    secret = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    guessed = False

    print(f"I've picked a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")

        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.\n")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("Please guess between 1 and 100.\n")
            continue

        if guess < secret:
            print("Too low!\n")
        elif guess > secret:
            print("Too high!\n")
        else:
            print(f"\n🎉 Correct! The number was {secret}.")
            print(f"You got it in {attempts} attempt(s).")
            guessed = True
            break

    if not guessed:
        print(f"\n😔 Out of attempts! The number was {secret}.")


def run_all_exercises():
    """Run all Day 4 exercises."""
    print("=" * 60)
    print("Week 1, Day 4: Loops Part 1")
    print("=" * 60)

    print("\n--- Exercise 1: While Loop Basics ---")
    exercise_1_while_loop_basics()

    print("\n--- Exercise 2: For Loop Basics ---")
    exercise_2_for_loop_basics()

    print("\n--- Exercise 3: Countdown Timer ---")
    exercise_3_countdown_timer()

    print("\n--- Exercise 4: Multiplication Table ---")
    exercise_4_multiplication_table()

    print("\n--- Exercise 5: Sum of Range ---")
    exercise_5_sum_of_range()

    print("\n" + "=" * 60)
    print("Mini Project: Guessing Game")
    print("=" * 60)
    mini_project_guessing_game()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 4 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Run {func_name}")
        globals()[func_name]()
    else:
        print("Run em all")
        run_all_exercises()
