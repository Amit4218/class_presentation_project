#! /usr/bin/python3

import requests
import os
import platform

correct_answers = 0
total_attempts = 0


def clear_screen():
    # Clear terminal screen based on OS
    if platform.system() == "windows":
        os.system("cls")
    else:
        os.system("clear")


def get_random_riddle():
    try:
        response = requests.get(
            "https://infiniteamit.pythonanywhere.com/get-random-riddle-cli"
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException as e:
        return None


def quit_riddle():
    print("\nThanks for playing! Goodbye!")
    print(f"Score: {correct_answers} correct answers out of {total_attempts} attempts.")
    print("------------------------------------------------------\n")


def start_riddle():
    global correct_answers, total_attempts

    clear_screen()  # Clear the screen before showing the riddle

    riddle = get_random_riddle()
    if not riddle:
        print("Oops! No riddle available at the moment.")
        return

    riddle_answer = riddle["answer"].lower().strip()

    print("-------------------------------------------------------------------------\n")
    print(f"Riddle: {riddle['riddle']}\n\n")
    print("Type 'exit' or 'q' to quit the game at any time.\n")
    print("-------------------------------------------------------------------------\n")

    answer = input("Your answer: ").lower().strip()

    if answer in ["exit", "q"]:
        quit_riddle()
        return

    total_attempts += 1

    if answer == riddle_answer:
        print("✅ Correct! Well done!\n")
        correct_answers += 1
    else:
        print(f"❌ Wrong! The correct answer was: {riddle_answer}\n")

    choice = input("Do you want to play again? (yes/no): ").lower().strip()
    if choice in ["yes", "y"]:
        start_riddle()
    else:
        quit_riddle()


def main():
    clear_screen()
    print("\n\t############  Welcome to the Riddle CLI! ############\n")
    input("Press Enter to start...\n")
    start_riddle()


if __name__ == "__main__":
    main()
