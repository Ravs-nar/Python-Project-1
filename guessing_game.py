# Import the random and statistics modules.
import random
import statistics

# Create the start_game function.
# Write your code inside this function.
def start_game():
    print("Welcome to the Number Guessing Game")  # 1. Display an intro/welcome message to the player.
    attempt_list = []  # List to store the number of attempts for each game

    while True:
        # Initialize for each game
        winning_number = random.randint(1, 10)  # 2. Store a random number as the answer/solution.
        guess_count = 0

        while True:
            try:
                guess = int(input("Enter your guess: "))  # 3. Continuously prompt the player for a guess.
                guess_count += 1

                if guess > winning_number:
                    print("It's lower")  # a. If the guess is greater than the solution, display to the player "It's lower".
                elif guess < winning_number:
                    print("It's higher")  # b. If the guess is less than the solution, display to the player "It's higher".
                else:
                    # 4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses.
                    print(f"Congratulations! You guessed the correct number {winning_number}.")
                    print(f"It took you {guess_count} attempts to get the correct answer.")
                    print(attempt_list)

                    # Store the number of attempts in the attempt list
                    attempt_list.append(guess_count)
                    
                    # Calculate and display statistics
                    average = statistics.mean(attempt_list)
                    median_attempts = statistics.median(attempt_list)
                    mode_attempts = statistics.mode(attempt_list)
                    print(f"The mean of your attempts list is: {average}")
                    print(f"The median of your attempts list is: {median_attempts}")
                    print(f"The mode of your attempts list is: {mode_attempts}")
                    break  # Break out of the guessing loop when the correct number is guessed

            except ValueError:
                print("Please enter a valid integer.")

        # Prompt the player to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        
        # Check if the player wants to continue
        if play_again == "no":
            print("Thank you for playing!")
            break  # Exit the game loop
        elif play_again != "yes":
            print("Invalid response. Exiting the game.")
            break

# Kick off the program by calling the start_game function.
start_game()