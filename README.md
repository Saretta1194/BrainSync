# BRIANSYNC 

A terminal-based multiple-choice quiz game connected to Google Sheets for score tracking and progression logging.
<img src="assets/images/responsive.jpg" alt="responsive" width="800">
The deployed project live link is [HERE](https://brainsync-0f71c4bb1b9c.herokuapp.com/)

## 📌 Contents

- [Introduction](#introduction)  
- [Project Goals](#project-goals)  
- [User Goals](#user-goals)  
- [Site Owner Goals](#site-owner-goals)  
- [Pre-Development Planning](#pre-development-planning)  
- [Development](#development)  
- [Features](#features)  
- [Game Flow](#game-flow)  
- [Google Sheets Integration](#google-sheets-integration)  
- [Technologies Used](#technologies-used)   
- [Testing](#testing)  
- [Validation](#validation)  
- [Deployment](#deployment)  
- [Bugs](#bugs)  
- [Credits](#credits)  
- [Acknowledgements](#acknowledgements)  

---

## 🧠 Introduction

**BrainSync** is a fun and engaging quiz program designed to challenge users across 3 levels of difficulty: Easy, Medium, and Hard. It uses a Google Sheet to retrieve and store questions and user scores. The game is designed to run in a terminal environment and provides instant feedback, score tracking, and end-of-game summaries.

---

## 🎯 Project Goals

- Provide a simple but engaging educational quiz game.
- Introduce users to progressively challenging content.
- Encourage learning through fun and competition.
- Log all user performance data for future insights.

---

## 🙋‍♂️ User Goals

- Understand the game rules clearly.
- Play through multiple quiz levels with increasing difficulty.
- Get instant feedback on answers.
- Receive a final performance summary.
- Ensure progress is saved securely.

---
## 💼 Site Owner Goals

- Present an interactive educational tool.
- Collect user performance data via Google Sheets.
- Provide an intuitive, bug-free experience.
- Keep the code modular and scalable for future improvements.

---
## 📝 Pre-Development Planning

- Brainstormed quiz mechanics and win/loss conditions.
Wireframes <img src="assets/images/logic.png" alt="Wireframes of the game" width="800">
- Created question templates for Google Sheets.
- Planned function responsibilities (e.g., user input, score tracking, game flow).
- Outlined a clear UI in terminal format with visual ASCII art and emojis for feedback.

---
## 💻 Development

- Used Python and `gspread` to connect with Google Sheets.
- Structured code for clear function segregation.
- Added terminal UI elements: title screen, menu, rules, and real-time prompts.
- Enabled score persistence using Google Sheets append functionality.

---
## ✨ Features

### 🧾 Terminal UI with ASCII Art  
Displays a welcoming title screen and clear visual feedback.
<img src="assets/images/start.jpg" alt="logo" width="800">

### 📜 Game Rules Display  
Accessible from the main menu at any time.
<img src="assets/images/rules brainsync.jpg" alt="rules" width="800">

### 🔁 Three-Level Structure  
Players must answer 5 questions per level and need at least 4 correct answers to advance.
<img src="assets/images/brainsync game.jpg" alt="game" width="800">

### ❌ Mistake Limiter  
Users are allowed only 1 mistake per level; 2 mistakes ends the game.
<img src="assets/images/game over.jpg" alt="gameover" width="800">

### ✅ Real-time Feedback  
Immediate response after each answer—correct or incorrect.
<img src="assets/images/pass.jpg" alt="correct" width="800">

### 📊 Final Summary  
Reports the number of levels passed and the total score.
<img src="assets/images/finish of the game briansync.jpg" alt="summary" width="800">

---
## 🎮 Game Flow

1. Welcome screen and player name input.
2. Main menu with options to:
   - Start Quiz
   - View Rules
   - Exit
3. Each level contains:
   - 5 multiple-choice questions
   - Feedback after each question
   - Score tracking
4. At the end of each level:
   - Option to continue or quit
   - Score saved to Google Sheets

---
## 🗂️ Google Sheets Integration

BrainSync uses two worksheets:

- **`questions`**: Stores all multiple-choice questions with options and correct answers.
 <img src="assets/images/google sheets.png" alt="google sheets questions" width="800">
- **`results`**: Logs user scores including:
  - Username
  - Level played
  - Score
  - Status (passed/failed/quit)
  - Date of play
 <img src="assets/images/result.png" alt="google sheets results" width="800">
 
 ---

 ## 🛠️ Technologies Used

- Python 3
- Google Sheets API
- GitHub
- CodeAnywhere
- Heroku
- Python Library´s

---
## Testing

The portal has undergone extensive testing, and the results are available for review
[here - TESTING](https://github.com/Saretta1194/BrainSync/blob/main/TESTING.md)

### Validator Testing

- CI Python Linter
  - No errors were returned when passing the final version through the 
  [CI Python Linter](https://pep8ci.herokuapp.com/#)

<img src="assets/" alt="CI Python Linter" width="800">

### Fixed Bugs
- Long lines on Python code:
  - The solution was to create strings with the variable name outside the function.

### Unfixed Bugs
  - none
  
## Deployment
- The deployment was done through heroku. following the steps below:
  - Preparing for deployment:
      - Add a new line character ("\n") at the end of each input request.
      - Create a list of dependancies to go into the requirements.txt file by typing "pip3 freeze > requirements.txt" into the terminal.
  - Deployment:
      - Log into Heroku and in the dashboard, press the "Create new app" button.
      - Click on the "Settings" tab, scroll down to the "Reveal Config Vars" button and click on it to create config vars.
      - Add the first config vars. The key is "CREDS" and value is the contents of the creds.json file.
      - Add the second config vars. The key is "PORT" and value is "8000".
      - Click on the "Add buildpack" button on the same page and add the buildpacks "python" and "node.js" in this order.
      - Click on the "Deploy" tab.
      - Choose the "GitHub" deployment method and then connect to GitHub.
      - Scroll down to the "Automatic deploys" section, select the "main" branch to deploy from and then press the "Enable Automatic Deploys" button to deploy the project.
