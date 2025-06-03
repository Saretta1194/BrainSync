import gspread
from google.oauth2.service_account import Credentials
import os
import sys
import time
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("BrainSync")

question_sheet = SHEET.worksheet("questions")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def display_title():
    print(r"""# noqa: W291
______      _             _____                  
| ___ \    (_)           /  ___|                 
| |_/ /_ __ _  __ _ _ __ \ `--. _   _ _ __   ___ 
| ___ \ '__| |/ _` | '_ \ `--. \ | | | '_ \ / __|
| |_/ / |  | | (_| | | | /\__/ / |_| | | | | (__ 
\____/|_|  |_|\__,_|_| |_\____/ \__, |_| |_|\___|
                                 __/ |           
                                |___/            
 """)


# Show rules
def rules():
    print(">> Welcome to BrainSync: The 3-Level Knowledge Challenge!\n")
    time.sleep(0.8)
    print("🎯 OBJECTIVE:")
    print("Answer 5 multiple-choice questions in each level to progress.")
    print("There are 3 levels: Easy → Medium → Hard\n")
    time.sleep(0.8)
    print("🛡️ RULES:")
    print("• Each level has 5 questions.")
    print("• You need at least 4 correct answers to pass a level.")
    print("• You're allowed 1 mistake per level.")
    print("• More than 1 mistake ends the game.\n")
    time.sleep(0.8)
    print("📝 HOW TO PLAY:")
    print("• Answer by typing A, B, or C.")
    print("• Invalid input will prompt a retry.")
    print("• You'll receive feedback after each answer.")
    print("• At the end, you can save your score.\n")
    time.sleep(0.8)
    print("Good luck! 🍀\n")
    time.sleep(1)


def get_username():
    """
    Ask the user for their name and validate it's not empty.
    Returns the username as a string.
    """
    while True:
        name = input("🧑 Please enter your name:\n").strip()
        if name:
            return name
        else:
            print("⚠️ Name cannot be empty. Please enter it again.")


# Main menu
def main_menu(username):
    progress = {}  # Track level scores
    time.sleep(0.8)
    """
    Displays the main menu and handles user navigation.
    """
    while True:
        clear()
        display_title()
        print(f"👋 Welcome, {username}!\n")
        print("Please choose an option:")
        print("1. Start Quiz")
        print("2. View Rules")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3):\n").strip()

        if choice == "1":
            clear()
            print("Starting Level 1: Easy\n")
            time.sleep(1)
            run_level("easy", username, progress)
            break

        elif choice == "2":
            clear()
            rules()
            input("\nPress ENTER to return to the main menu.")

        elif choice == "3":
            print(f"\nThanks for playing BrainSync, {username}! Goodbye 👋")
            time.sleep(1)
            sys.exit()

        else:
            print("\n❌ Invalid input. Please enter 1, 2 or 3.")
            time.sleep(1.5)


def run_level(level, username, progress):
    """
    Runs the quiz for a given level (easy, medium, hard)
    """

    # Load all rows from Google Sheets as dictionary list
    data = question_sheet.get_all_records()

    # Filter only questions with the desired level
    level_questions = [q for q in data if q["level"] == level]

    score = 0
    mistakes = 0

    for question in level_questions[:5]:
        if ask_question(question):
            score += 1
        else:
            mistakes += 1
        if mistakes > 1:
            print("Game over ❌ ")
            save_score(username, level, score, "failed")
            choice = ""
            while choice not in ["Y", "N"]:
                choice = input(
                    "Ready for another round? (Y/N):\n"
                    ).strip().upper()
                if choice not in ["Y", "N"]:
                    print("❌ Invalid input. Please enter Y or N.")
            if choice == "Y":
                run_level(level, username, progress)
                return
            else:
                print(" Thanks for playing  👋")
                save_score(username, level, score, "quit")
                show_final_summary(username, progress)
                return
    progress[level] = score

    if score >= 4:
        if level == "hard":
            print("🎉 You’ve completed all levels!")
            save_score(username, level, score, "passed")
            show_final_summary(username, progress)
            return
        else:
            print("🎉 You passed the level!")
            save_score(username, level, score, "passed")
            choice = ""
            while choice not in ["Y", "N"]:
                choice = (
                    input(
                        "Do you want to continue to the next level? (Y/N):\n"
                        ).strip().upper()
                )
                if choice not in ["Y", "N"]:
                    print("❌ Invalid input. Please enter Y or N.")
            if choice == "Y":
                next_level = "medium" if level == "easy" else "hard"
                run_level(next_level, username, progress)
            else:
                show_final_summary(username, progress)
    else:
        print("❌ You didn’t pass this level.")
        save_score(username, level, score, "failed")
        choice = ""
        while choice not in ["Y", "N"]:
            choice = input("Do you want another chance?(Y/N):\n").strip().upper()
            if choice not in ["Y", "N"]:
                print("❌ Invalid input. Please enter Y or N.")
        if choice == "Y":
            run_level(level, username, progress)
        else:
            show_final_summary(username, progress)
            return


def ask_question(question):
    print("\nHere is your question:")
    print(f"Q: {question['question']}")
    print(f"A: {question['option_a']}")
    print(f"B: {question['option_b']}")
    print(f"C: {question['option_c']}")

    answer = ""
    while answer not in ["A", "B", "C"]:
        answer = input("Enter your answer here:\n").strip().upper()
        if answer not in ["A", "B", "C"]:
            print("Please enter only A,B or C")

    if answer == question["correct"]:
        print("Correct! ")
        return True
    else:
        print("Oops, not correct! Go again")
        return False


def save_score(username, level, score, status):
    """
    Update results worksheet, add new row with the list data provided
    """
    print("Updating score.../n")
    current_date = datetime.now().strftime("%d/%m/%Y")
    result_worksheet = SHEET.worksheet("results")
    result_worksheet.append_row([username, level, score, status, current_date])
    print(" ✅ Score updated successfully.\n")


def show_final_summary(username, progress):
    """
    Shows a final summary of the quiz with the total score and levels passed.
    """
    total_score = sum(progress.values())
    levels_completed = sum(1 for score in progress.values() if score >= 4)

    print("\n📊 FINAL SUMMARY 📊")
    print(f"Player: {username}")
    print(f"Levels Completed: {levels_completed}/3")
    print(f"Total Score: {total_score}/15\n")

    if levels_completed == 3:
        print("🏆 Status: BrainSinc Master! Well done! 🧠")
    elif levels_completed == 2:
        print("💪 Great job! Just one level away from perfection.")
    elif levels_completed == 1:
        print("👍 Nice try! You passed one level. Keep training!")
    else:
        print("📚 You didn't pass any level. Give it another shot!")


clear()
display_title()
username = get_username()
print(f"\n👋 Hello, {username}! Get ready to test your knowledge.\n")
time.sleep(1.2)
main_menu(username)
