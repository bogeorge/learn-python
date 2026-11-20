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
            
            if guess < lucky:
                print("Too low!")
            elif guess > lucky:
                print(f"Too high!")
            else:
                print(f"Congrats! {lucky} is correct!")
        except ValueError:
            print("Please enter a valid number")

thing()