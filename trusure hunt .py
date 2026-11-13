
import random
import time

# Global variables
player_name = ""
total_score = 0
games_played = 0
best_score = 0


# Function to display welcome message
def welcome_message():
    print("\n========================================")
    print("       TREASURE NUMBER HUNT GAME")
    print("========================================")
    print("Welcome to the Treasure Hunt Adventure!")
    print("Find the secret treasure number to win.")
    print("----------------------------------------")


# Function to select difficulty level
def select_difficulty():

    print("\nSelect Your Difficulty Level")
    print("1. Easy   (1 to 50) - 10 Attempts")
    print("2. Medium (1 to 100) - 7 Attempts")
    print("3. Hard   (1 to 200) - 5 Attempts")

    while True:
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            return 50, 10

        elif choice == "2":
            return 100, 7

        elif choice == "3":
            return 200, 5

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


# Function to give hints
def give_hint(secret_number, guess):

    difference = abs(secret_number - guess)

    if difference == 0:
        print("Congratulations! You found the treasure!")

    elif difference <= 5:
        print("Very Close! You are almost there!")

    elif difference <= 15:
        print("Getting Closer! Keep trying!")

    elif guess < secret_number:
        print("Too Low! Try a Higher Number.")

    else:
        print("Too High! Try a Lower Number.")


# Function to calculate score
def calculate_score(attempts_left, max_attempts):

    score = attempts_left * 10

    if attempts_left == max_attempts:
        score += 50

    return score


# Function to play the game
def play_game():

    global total_score, games_played, best_score

    max_number, max_attempts = select_difficulty()

    secret_number = random.randint(1, max_number)

    attempts_left = max_attempts
    attempts_used = 0

    print("\n========================================")
    print("A treasure is hidden between 1 and",
          max_number)
    print("You have", max_attempts, "attempts.")
    print("========================================")

    # Main game loop
    while attempts_left > 0:

        print("\nAttempts Remaining:", attempts_left)

        try:
            guess = int(input("Enter your treasure number: "))

        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > max_number:
            print("Number is outside the allowed range!")
            continue

        attempts_used += 1
        attempts_left -= 1

        if guess == secret_number:

            print("\n********************************")
            print("        TREASURE FOUND!")
            print("********************************")
            print("Excellent work,", player_name)
            print("Secret Number:", secret_number)
            print("Attempts Used:", attempts_used)

            points = calculate_score(
                attempts_left, max_attempts
            )

            print("Your Score:", points)

            total_score += points
            games_played += 1

            if points > best_score:
                best_score = points

            break

        else:
            give_hint(secret_number, guess)

            # Give an additional clue
            if attempts_left > 0:
                if secret_number % 2 == 0:
                    print("Hint: The treasure number is EVEN.")
                else:
                    print("Hint: The treasure number is ODD.")

    else:
        print("\nSorry! You have used all your attempts.")
        print("The treasure number was:", secret_number)
        print("Better luck next time!")

        games_played += 1


# Function to display scoreboard
def display_scoreboard():

    print("\n========================================")
    print("             SCOREBOARD")
    print("========================================")

    print("Player Name :", player_name)
    print("Games Played:", games_played)
    print("Total Score :", total_score)
    print("Best Score  :", best_score)

    if games_played > 0:
        average = total_score / games_played
        print("Average Score:", round(average, 2))

    print("========================================")


# Function to display game instructions
def instructions():

    print("\n******** GAME INSTRUCTIONS ********")
    print("1. Select your preferred difficulty.")
    print("2. Guess the hidden treasure number.")
    print("3. Follow the hints provided.")
    print("4. Find the number before attempts end.")
    print("5. Earn more points with fewer attempts.")
    print("6. Try different levels to improve your score.")
    print("***********************************")


# Main function
def main():

    global player_name

    welcome_message()

    player_name = input("\nEnter your name: ")

    print("\nHello", player_name, "! Ready for the adventure?")

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Start New Game")
        print("2. View Instructions")
        print("3. View Scoreboard")
        print("4. Exit Game")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":

            play_game()

        elif choice == "2":

            instructions()

        elif choice == "3":

            display_scoreboard()

        elif choice == "4":

            print("\nThank you for playing,", player_name)
            print("Your Final Score:", total_score)
            print("See you again in the next adventure!")
            print("\nGAME OVER!")
            break

        else:

            print("Invalid choice! Please select 1 to 4.")


# Program execution
if __name__ == "__main__":
    main()
