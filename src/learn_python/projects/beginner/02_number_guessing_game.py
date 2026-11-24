"""
Project 2: Number Guessing Game
Week 1, Beginner Level

A game where the computer picks a random number and the player tries to guess it.
This project practices:
- Random number generation
- User input and validation
- While loops
- Conditional statements
- Game logic
"""

import random


def easy_game():
    """
    Easy mode: Guess between 1-50 with unlimited attempts.
    """
    print("\n" + "=" * 50)
    print("EASY MODE: Guess between 1-50")
    print("=" * 50)

    # Generate random number
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = float("inf")  # Unlimited attempts

    print("I'm thinking of a number between 1 and 50.")
    print("Can you guess what it is?")

    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            # Check guess
            if guess < 1 or guess > 50:
                print("Please guess a number between 1 and 50!")
                continue

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The secret number was {secret_number}.")
                return attempts

        except ValueError:
            print("Please enter a valid number!")

    return attempts


def medium_game():
    """
    Medium mode: Guess between 1-100 with limited attempts.
    """
    print("\n" + "=" * 50)
    print("MEDIUM MODE: Guess between 1-100")
    print("=" * 50)

    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("I'll give you hints after each guess!")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\nAttempts remaining: {remaining}")

        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100!")
                continue

            # Check guess with more detailed hints
            difference = abs(secret_number - guess)

            if guess == secret_number:
                print(f"\n🎉 Perfect! You guessed it in {attempts} attempts!")
                print(f"The secret number was {secret_number}.")
                return attempts, True
            elif difference <= 5:
                print("🔥 Very close!")
                if guess < secret_number:
                    print("   (Just a bit higher!)")
                else:
                    print("   (Just a bit lower!)")
            elif difference <= 15:
                print("😊 Getting warmer!")
                if guess < secret_number:
                    print("   (Try a higher number)")
                else:
                    print("   (Try a lower number)")
            else:
                print("🥶 Cold...")
                if guess < secret_number:
                    print("   (Way too low)")
                else:
                    print("   (Way too high)")

        except ValueError:
            print("Please enter a valid number!")

    print(f"\n😔 Game over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")
    return attempts, False


def hard_game():
    """
    Hard mode: Guess between 1-200 with very limited attempts and penalties.
    """
    print("\n" + "=" * 50)
    print("HARD MODE: Guess between 1-200")
    print("=" * 50)

    secret_number = random.randint(1, 200)
    max_attempts = 7
    attempts = 0
    score = 1000  # Starting score

    print("I'm thinking of a number between 1 and 200.")
    print(f"You have only {max_attempts} attempts!")
    print(f"Starting score: {score}")
    print("Each wrong guess costs you points!")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\nAttempts remaining: {remaining}")
        print(f"Current score: {score}")

        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 200:
                print("Invalid guess! You lose 50 points.")
                score -= 50
                continue

            if guess == secret_number:
                bonus = (max_attempts - attempts + 1) * 100
                score += bonus
                print(f"\n🎉 INCREDIBLE! You guessed it in {attempts} attempts!")
                print(f"The secret number was {secret_number}.")
                print(f"Bonus points: {bonus}")
                print(f"Final score: {score}")
                return attempts, True, score
            else:
                # Calculate penalty based on how close/far
                difference = abs(secret_number - guess)
                penalty = min(100, difference * 2)  # Max 100 penalty
                score -= penalty

                if guess < secret_number:
                    if difference <= 10:
                        print(f"↗️  Close! A bit higher. (-{penalty} points)")
                    else:
                        print(f"⬆️  Too low! (-{penalty} points)")
                else:
                    if difference <= 10:
                        print(f"↘️  Close! A bit lower. (-{penalty} points)")
                    else:
                        print(f"⬇️  Too high! (-{penalty} points)")

        except ValueError:
            print("Invalid input! You lose 50 points.")
            score -= 50

    print(f"\n💀 GAME OVER! The secret number was {secret_number}.")
    print(f"Final score: {score}")
    return attempts, False, score


def two_player_game():
    """
    Two player mode: One player sets the number, the other guesses.
    """
    print("\n" + "=" * 50)
    print("TWO PLAYER MODE")
    print("=" * 50)

    print("Player 1: You'll set the secret number.")
    print("Player 2: You'll try to guess it.")

    # Player 1 sets the number
    while True:
        try:
            print("\n" + "-" * 30)
            min_range = int(input("Player 1: Enter minimum number (e.g., 1): "))
            max_range = int(input("Player 1: Enter maximum number (e.g., 100): "))

            if min_range >= max_range:
                print("Maximum must be greater than minimum!")
                continue

            secret_number = int(
                input(
                    f"Player 1: Enter secret number between {min_range} and {max_range}: "
                )
            )

            if secret_number < min_range or secret_number > max_range:
                print(f"Number must be between {min_range} and {max_range}!")
                continue

            break
        except ValueError:
            print("Please enter valid numbers!")

    # Clear screen (conceptually)
    print("\n" * 50)
    print("=" * 50)
    print("Player 2: It's your turn to guess!")
    print("=" * 50)

    max_attempts = 10
    attempts = 0

    print(f"\nGuess the number between {min_range} and {max_range}")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\nAttempts remaining: {remaining}")

        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < min_range or guess > max_range:
                print(f"Please guess between {min_range} and {max_range}!")
                continue

            if guess == secret_number:
                print(f"\n🎉 Player 2 wins! Guessed in {attempts} attempts!")
                print(f"The secret number was {secret_number}.")
                return attempts, True
            else:
                difference = abs(secret_number - guess)
                percentage = (difference / (max_range - min_range)) * 100

                if guess < secret_number:
                    print(f"Too low! ({percentage:.1f}% away from max)")
                else:
                    print(f"Too high! ({percentage:.1f}% away from min)")

        except ValueError:
            print("Please enter a valid number!")

    print(f"\n😔 Player 2 loses! The secret number was {secret_number}.")
    print("Player 1 wins!")
    return attempts, False


def display_stats(stats):
    """
    Display game statistics.
    """
    print("\n" + "=" * 50)
    print("GAME STATISTICS")
    print("=" * 50)

    if not stats:
        print("No games played yet.")
        return

    total_games = len(stats)
    wins = sum(1 for game in stats if game["won"])
    losses = total_games - wins

    print(f"Total games played: {total_games}")
    print(f"Wins: {wins} ({wins / total_games * 100:.1f}%)")
    print(f"Losses: {losses} ({losses / total_games * 100:.1f}%)")

    if wins > 0:
        avg_attempts = sum(game["attempts"] for game in stats if game["won"]) / wins
        print(f"Average attempts to win: {avg_attempts:.1f}")

    # Best score
    if any("score" in game for game in stats):
        scores = [game.get("score", 0) for game in stats]
        best_score = max(scores)
        print(f"Best score: {best_score}")

    # Recent games
    print("\nRecent games:")
    for i, game in enumerate(stats[-5:], 1):
        result = "WON" if game["won"] else "LOST"
        mode = game["mode"]
        attempts = game["attempts"]

        if "score" in game:
            print(
                f"  {i}. {mode}: {result} in {attempts} attempts (Score: {game['score']})"
            )
        else:
            print(f"  {i}. {mode}: {result} in {attempts} attempts")


def number_guessing_game():
    """
    Main game function with menu and game loop.
    """
    print("=" * 60)
    print("NUMBER GUESSING GAME")
    print("=" * 60)

    game_stats = []

    while True:
        print("\n" + "=" * 50)
        print("MAIN MENU")
        print("=" * 50)
        print("1. Easy Mode (1-50, unlimited attempts)")
        print("2. Medium Mode (1-100, 10 attempts)")
        print("3. Hard Mode (1-200, 7 attempts, scoring)")
        print("4. Two Player Mode")
        print("5. View Statistics")
        print("6. How to Play")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            attempts = easy_game()
            game_stats.append({"mode": "Easy", "won": True, "attempts": attempts})

        elif choice == "2":
            attempts, won = medium_game()
            game_stats.append({"mode": "Medium", "won": won, "attempts": attempts})

        elif choice == "3":
            attempts, won, score = hard_game()
            game_stats.append(
                {"mode": "Hard", "won": won, "attempts": attempts, "score": score}
            )

        elif choice == "4":
            attempts, won = two_player_game()
            game_stats.append({"mode": "Two Player", "won": won, "attempts": attempts})

        elif choice == "5":
            display_stats(game_stats)

        elif choice == "6":
            print_instructions()

        elif choice == "7":
            print("\n" + "=" * 50)
            print("Thanks for playing!")
            print("=" * 50)

            if game_stats:
                display_stats(game_stats)

            break

        else:
            print("Invalid choice. Please enter 1-7.")

        # Ask if player wants to play again
        if choice in ["1", "2", "3", "4"]:
            play_again = input("\nPlay another game? (y/n): ").strip().lower()
            if play_again != "y":
                print("\nThanks for playing!")
                if game_stats:
                    display_stats(game_stats)
                break


def print_instructions():
    """
    Print game instructions.
    """
    print("\n" + "=" * 50)
    print("HOW TO PLAY")
    print("=" * 50)
    print("\nIn this game, you try to guess a secret number.")
    print("\nGame Modes:")
    print("1. EASY: Guess between 1-50 with unlimited attempts")
    print("2. MEDIUM: Guess between 1-100 with 10 attempts")
    print("3. HARD: Guess between 1-200 with 7 attempts and scoring")
    print("4. TWO PLAYER: One player sets the number, other guesses")

    print("\nTips:")
    print("• Start with the middle of the range")
    print("• Use the hints to adjust your next guess")
    print("• In Hard mode, minimize wrong guesses to keep score high")
    print("• In Two Player mode, choose a tricky number!")

    print("\nScoring (Hard Mode only):")
    print("• Start with 1000 points")
    print("• Each wrong guess costs points based on how far off you are")
    print("• Bonus points for guessing quickly")

    input("\nPress Enter to return to menu...")


def test_game_logic():
    """
    Test the game logic with automated tests.
    """
    print("\n" + "=" * 50)
    print("GAME LOGIC TESTS")
    print("=" * 50)

    print("\nTesting random number generation...")

    # Test random number range
    test_numbers = []
    for _ in range(1000):
        test_numbers.append(random.randint(1, 50))

    min_num = min(test_numbers)
    max_num = max(test_numbers)

    print("Generated 1000 numbers between 1-50:")
    print(f"  Minimum: {min_num} (Expected: 1)")
    print(f"  Maximum: {max_num} (Expected: 50)")

    if min_num == 1 and max_num == 50:
        print("  ✅ Random generation working correctly")
    else:
        print("  ❌ Random generation issue detected")

    # Test game logic
    print("\nTesting game logic...")

    # Simulate a game
    secret = 42
    guesses = [20, 50, 35, 45, 42]  # Simulated guesses
    attempts = 0

    for guess in guesses:
        attempts += 1
        if guess == secret:
            print(f"  ✅ Correct guess on attempt {attempts}")
            break
        elif guess < secret:
            print(f"  Attempt {attempts}: {guess} -> Too low")
        else:
            print(f"  Attempt {attempts}: {guess} -> Too high")

    print("\nTests completed!")


def main():
    """
    Main function to run the number guessing game.
    """
    print("Welcome to the Number Guessing Game, Bo!")

    while True:
        print("\n" + "=" * 50)
        print("NUMBER GUESSING GAME")
        print("=" * 50)
        print("1. Play Game")
        print("2. Run Tests")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            test_game_logic()
        elif choice == "3":
            print("\nGoodbye! Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1-3.")


if __name__ == "__main__":
    main()
