import gspread
from google.oauth2.service_account import Credentials
import os
import sys
import time


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('BrainSync')

question_sheet = SHEET.worksheet('questions')



# Clear terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display title screen
def display_title():
    print("""
 /$$$$$$$                     /$$            /$$$$$$                               
| $$__  $$                   |__/           /$$__  $$                              
| $$  \ $$  /$$$$$$  /$$$$$$  /$$ /$$$$$$$ | $$  \__/ /$$   /$$ /$$$$$$$   /$$$$$$$
| $$$$$$$  /$$__  $$|____  $$| $$| $$__  $$|  $$$$$$ | $$  | $$| $$__  $$ /$$_____/
| $$__  $$| $$  \__/ /$$$$$$$| $$| $$  \ $$ \____  $$| $$  | $$| $$  \ $$| $$      
| $$  \ $$| $$      /$$__  $$| $$| $$  | $$ /$$  \ $$| $$  | $$| $$  | $$| $$      
| $$$$$$$/| $$     |  $$$$$$$| $$| $$  | $$|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$
|_______/ |__/      \_______/|__/|__/  |__/ \______/  \____  $$|__/  |__/ \_______/
                                                      /$$  | $$                    
                                                     |  $$$$$$/                    
                                                      \______/                     
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

# Main menu
def main_menu():
    time.sleep(0.8)
    """
    Displays the main menu and handles user navigation.
    """   
    while True:
        clear()
        display_title()
        print("Please choose an option:")
        print("1. Start Quiz")
        print("2. View Rules")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            clear()
            print("Starting Level 1: Easy\n")
            time.sleep(1)
            run_level("easy")  
            break

        elif choice == "2":
            clear()
            rules()
            input("\nPress ENTER to return to the main menu.")

        elif choice == "3":
            print("\nThanks for playing BrainSync! Goodbye 👋")
            time.sleep(1)
            sys.exit()

        else:
            print("\n❌ Invalid input. Please enter 1, 2 or 3.")
            time.sleep(1.5)

def run_level(level):
    """
    Runs the quiz for a given level (easy, medium, hard).
    Loads one question for now.
    """
    # Carica tutte le righe dal foglio Google Sheets come lista di dizionari
    data = question_sheet.get_all_records()

    # Filtra solo le domande con il livello desiderato
    level_questions = [q for q in data if q['level'] == level]

    # Per ora selezioniamo la prima domanda del livello
    question = level_questions[0]

    # Mostra la domanda e le opzioni all'utente
    print("\nHere is your question:")
    print(f"Q: {question['question']}")
    print(f"A: {question['option_a']}")
    print(f"B: {question['option_b']}")
    print(f"C: {question['option_c']}")





    


clear()
display_title()
main_menu()
