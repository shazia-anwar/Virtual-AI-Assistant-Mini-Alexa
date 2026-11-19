import random

def play_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 3
    
    print("Assistant: Guess a number between 1 and 10.")
    print("Assistant: You have 3 attempts.")
    
    for attempt in range(attempts):
        try:
            guess = int(input("Your guess: "))
        
        except ValueError:
            print("Assistant: Please enter a valid number.")
            continue
        
        if guess == secret_number:
            print("Assistant: Congratulations! Correct guess!")
            return
        
        elif guess < secret_number:
            print("Assistant: Try a higher number.")
        
        else:
            print("Assistant: Try a lower number.")
    
    print("Assistant: Game over!")
    print("Assistant: The correct number was", secret_number)
