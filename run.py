import gspread
from google.oauth2.service_account import Credentials
import os


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('BrainSync')

question = SHEET.worksheet('question')

# Function to clean the console screen when the next atempt
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
"""
          )
    print(">> Welcome to BrainSync: The 3-Level Knowledge Challenge!")
    print("Your goal: Answer 5 questions correctly to move to the next level.")
    print("Levels: Easy → Medium → Hard")
    print("Answer by typing A, B, or C.\n")

display_title()