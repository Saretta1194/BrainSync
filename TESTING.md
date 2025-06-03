## 🧪 Testing

Once the BrainSync quiz application was complete, thorough testing was performed to ensure the game works as expected under all typical user scenarios and that any possible input errors are properly handled.

### 👥 User Testing & Feedback

The application was tested in a controlled environment by several users to simulate real interactions. Feedback focused on ease of use, clarity of instructions, and game progression. Based on this feedback:

- Validation was added to prevent players from submitting empty names.
- Invalid answers outside of A, B, or C now prompt clear error messages.
- When users input an invalid choice in menus or confirmation prompts (e.g., "x" instead of "y/n"), they are shown an appropriate message and asked to try again.

### ✅ Functional Tests

| Feature            | Action     | Expected Result                      |Actual Result         |

| Title Screen       | Load game  | ASCII title and welcome message shown| ✅ Works as expected  |
| Name Input (valid) | Enter name | Name accepted and stored             | ✅ Works as expected  |
| Name Input (empty) | Empty name | Prompt for retry                     | ✅ Works as expected  |
| Menu Navigation    |Option1,2or3| Correct section loaded               | ✅ Works as expected  |
| Rules Section      |Select "View Rules"| Rules displayed clearly       | ✅ Works as expected  |
|Questions valid     |Answer A/B/C| Correctness feedback provided        | ✅ Works as expected  |
| Question (invalid) |invalid character  |Error message shown            | ✅ Works as expected  |
| Pass Level         | Answer 4 or more correctly | Advance to next level| ✅ Works as expected  |
| Fail Level         | Make 2 mistakes     | Game over screen appears    | ✅ Works as expected  |
| Score Tracking     | Complete a level    | Score added to summary      | ✅ Works as expected  |
| Save Score         | Finish game         | Score saved to Google Sheets| ✅ Works as expected  |

---

## 🌐 Browser and Terminal Testing

- Browser tested:
  - Chrome
  - Firefox
  - Safari

- Operating systems:
  - Android
  - iOS

Since BrainSync runs in the terminal, it was tested in the following environments:

- macOS Terminal
- VS Code Terminal (cross-platform)

No compatibility issues were encountered across these platforms.

---

## 📊 Google Sheets Integration

The game connects to Google Sheets using the `gspread` and `google-auth` libraries. Multiple test users were simulated, and their scores were correctly saved to the **results** worksheet.

- All expected fields (name, level, score, status, date) are recorded accurately.
- Formatting was tested, and date/time values are correctly displayed.
- No data overwrite issues were found—each play session creates a new row.

---

## 🧾 Input Validation

Extra care was taken to validate all user input:

- Menu and confirmation prompts accept only valid values (1/2/3, Y/N, A/B/C).
- Player name cannot be blank.
- Case-insensitive inputs are accepted (e.g., "a", "A").

These checks ensure that the game does not crash due to unexpected input and provides clear guidance when needed.

### [BACK TO README](https://github.com/Saretta1194/BrainSync/blob/main/README.md)

