import sys

"""
Week 1, Day 5: Loops Part 2 & Lists

Exercises to practice nested loops, break/continue, and list basics.
"""


def exercise_1_nested_loops():
    """
    Use nested loops to print a times table grid for 1–5.

    Expected output (partial):
        1   2   3   4   5
        2   4   6   8  10
        3   6   9  12  15
        ...
    """
    print("Times table (1–5):")
    print()

    # Header row
    print("   ", end="")
    for col in range(1, 6):
        print(f"{col:4}", end="")
    print()
    print("   " + "-" * 20)

    # Table body
    for row in range(1, 6):
        print(f"{row:2} |", end="")
        for col in range(1, 6):
            print(f"{row * col:4}", end="")
        print()


def exercise_2_pattern_printing():
    """
    Use nested loops to print two patterns.

    Pattern 1 — right-angled triangle:
        *
        **
        ***
        ****
        *****

    Pattern 2 — inverted triangle:
        *****
        ****
        ***
        **
        *
    """
    rows = 5

    print("Pattern 1 — right-angled triangle:")
    for i in range(1, rows + 1):
        print("  " + "*" * i)

    print("\nPattern 2 — inverted triangle:")
    for i in range(rows, 0, -1):
        print("  " + "*" * i)


def exercise_3_break_and_continue():
    """
    Demonstrate break and continue.

    1. Loop from 1 to 20. Skip multiples of 3 (continue).
       Stop entirely when you hit 15 (break).
    2. Keep asking the user to type a word until they type "quit".
       Skip any input that is blank.
    """
    print("Numbers 1–20, skipping multiples of 3, stopping at 15:")
    for i in range(1, 21):
        if i == 15:
            print(f"  Reached {i}, stopping.")
            break
        if i % 3 == 0:
            continue
        print(f"  {i}", end=" ")
    print()

    print("\nType words (blank input is ignored, 'quit' exits):")
    while True:
        word = input("  Enter a word: ").strip()
        if word == "":
            print("  (blank input ignored)")
            continue
        if word.lower() == "quit":
            print("  Exiting.")
            break
        print(f"  You typed: {word}")


def exercise_4_list_basics():
    """
    Demonstrate creating and working with lists.

    1. Create a list of five fruits
    2. Access the first and last item
    3. Add an item with append()
    4. Remove an item with remove()
    5. Check if an item is in the list
    6. Print the length of the list
    7. Loop over the list and print each item
    """
    fruits = ["apple", "banana", "cherry", "mango", "orange"]

    print(f"Original list : {fruits}")
    print(f"First item    : {fruits[0]}")
    print(f"Last item     : {fruits[-1]}")

    fruits.append("grape")
    print(f"\nAfter append  : {fruits}")

    fruits.remove("banana")
    print(f"After remove  : {fruits}")

    print(f"\n'mango' in list  : {'mango' in fruits}")
    print(f"'banana' in list : {'banana' in fruits}")

    print(f"\nLength: {len(fruits)}")

    print("\nAll fruits:")
    for fruit in fruits:
        print(f"  - {fruit}")


def exercise_5_find_max_min():
    """
    Given a list of numbers, find the maximum and minimum
    without using the built-in max() or min() functions.
    Then verify your result using the built-ins.
    """
    numbers = [34, 7, 23, 32, 5, 62, 18, 45, 11, 29]
    print(f"Numbers: {numbers}")

    # Manual search
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    print(f"\nManual search  → max: {largest}, min: {smallest}")
    print(f"Built-in check → max: {max(numbers)}, min: {min(numbers)}")

    match = largest == max(numbers) and smallest == min(numbers)
    print(f"Results match  : {match}")


def mini_project_shopping_list():
    """
    A simple shopping list manager.

    Commands:
      add <item>    — add an item to the list
      remove <item> — remove an item from the list
      view          — display the current list
      clear         — remove everything
      quit          — exit
    """
    print("=" * 40)
    print("SHOPPING LIST MANAGER")
    print("=" * 40)
    print("Commands: add <item>, remove <item>, view, clear, quit\n")

    shopping_list = []

    while True:
        raw = input("Command: ").strip()

        if not raw:
            continue

        # Split into command and optional argument
        parts = raw.split(maxsplit=1)
        command = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else ""

        if command == "add":
            if not argument:
                print("  Usage: add <item>")
            elif argument.lower() in [item.lower() for item in shopping_list]:
                print(f"  '{argument}' is already on the list.")
            else:
                shopping_list.append(argument)
                print(
                    f"  Added '{argument}'. List now has {len(shopping_list)} item(s)."
                )

        elif command == "remove":
            if not argument:
                print("  Usage: remove <item>")
            else:
                # Case-insensitive removal
                match = next(
                    (i for i in shopping_list if i.lower() == argument.lower()), None
                )
                if match:
                    shopping_list.remove(match)
                    print(f"  Removed '{match}'.")
                else:
                    print(f"  '{argument}' is not on the list.")

        elif command == "view":
            if not shopping_list:
                print("  Your list is empty.")
            else:
                print(f"\n  Shopping list ({len(shopping_list)} item(s)):")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"    {index}. {item}")
                print()

        elif command == "clear":
            shopping_list.clear()
            print("  List cleared.")

        elif command == "quit":
            print("\nFinal list:")
            if shopping_list:
                for index, item in enumerate(shopping_list, start=1):
                    print(f"  {index}. {item}")
            else:
                print("  (empty)")
            print("Goodbye!")
            break

        else:
            print(f"  Unknown command '{command}'. Try: add, remove, view, clear, quit")


def run_all_exercises():
    """Run all Day 5 exercises."""
    print("=" * 60)
    print("Week 1, Day 5: Loops Part 2 & Lists")
    print("=" * 60)

    print("\n--- Exercise 1: Nested Loops ---")
    exercise_1_nested_loops()

    print("\n--- Exercise 2: Pattern Printing ---")
    exercise_2_pattern_printing()

    print("\n--- Exercise 3: Break and Continue ---")
    exercise_3_break_and_continue()

    print("\n--- Exercise 4: List Basics ---")
    exercise_4_list_basics()

    print("\n--- Exercise 5: Find Max and Min ---")
    exercise_5_find_max_min()

    print("\n" + "=" * 60)
    print("Mini Project: Shopping List Manager")
    print("=" * 60)
    mini_project_shopping_list()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 5 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Run {func_name}")
        globals()[func_name]()
    else:
        print("Run em all")
        run_all_exercises()
