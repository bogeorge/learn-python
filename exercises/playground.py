import random

def thing():
    low = 1
    high = 10
    lucky = random.randint(low, high)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}, Pick a number between {low} and {high}: "))
            attempts += 1

            if guess < 1 or guess > 10:  
                print(f"Please enter a number between {low} and {high}!")
                continue
            
            for counter in range(0, guess):
                print(f"counter={counter}")

            if guess < lucky:
                print("Too low!")
            elif guess > lucky:
                print(f"Too high!")
            else:
                print(f"Congrats! {lucky} is correct!")
        except ValueError:
            print("Please enter a valid number")

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
                print(f"  Added '{argument}'. List now has {len(shopping_list)} item(s).")

        elif command == "remove":
            if not argument:
                print("  Usage: remove <item>")
            else:
                # Case-insensitive removal
                match = next((i for i in shopping_list if i.lower() == argument.lower()), None)
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

mini_project_shopping_list()