# A-Magic-Eight-Ball
A Python Game

# 🔮 Magic Eight Ball - Console Fortune Teller

A simple Python program that simulates the classic Magic Eight Ball toy. Users can ask any yes-or-no question and receive a random, immediate response from a predefined list of fortunes.

This project is great for beginners learning about:
* **Lists** and how to store data.
* The **`random` module** for picking random items.
* **`while` loops** to keep the game running until the user decides to quit.
* The **`time` module** for adding dramatic pauses.

---

## ✨ Features

* **Interactive Input:** Prompt users for questions continuously.
* **Dramatic Pause:** Uses `time.sleep()` to simulate the "shaking" of the ball.
* **Clean Exit:** Users can type `exit` to quit the program gracefully.
* **Nine Classic Responses:** A variety of positive, neutral, and negative fortunes.

---

## 🚀 How to Run the Game

### 1. Prerequisites

You only need **Python 3** installed on your system.

### 2. Setup and Execution

1.  **Save the Code:** Save the Python code into a file named `eight_ball.py`.
2.  **Open Terminal:** Open your command prompt or terminal application.
3.  **Run the Script:** Execute the file using the Python interpreter:

    ```bash
    python magic.py
    ```

### 3. Gameplay

1.  The program will greet you and prompt you to ask a question.
2.  Type any question that can be answered with "Yes" or "No" and press **Enter**.
3.  After a brief pause, the Magic Eight Ball will reveal its fortune!
4.  To end the game, simply type `exit` when prompted for a question.

---

## 🧠 Code Breakdown Highlights

| Code Snippet | Purpose |
| :--- | :--- |
| `responses = [...]` | A Python **list** used to hold all the possible fortune outcomes. |
| `import time` | Brings in the module needed to control time. |
| `while True:` | Creates an **infinite loop**, allowing the user to ask multiple questions without restarting the script. |
| `time.sleep(1.5)` | Pauses the program for 1.5 seconds, simulating the mystery. |
| `random.choice(responses)` | Randomly selects a single string from the `responses` list. |
| `if question.lower() == 'exit': break` | The **exit condition** that gracefully breaks out of the `while True` loop. |

---

## 🔧 Challenges for Practice

If you want to expand this project and practice your Python skills, try these challenges:

1.  **Add More Responses:** Expand the `responses` list to include 5-10 more fortunes.
2.  **Add a Question Limit:** Modify the `while` loop so the user can only ask 5 questions before the game automatically ends.
3.  **Count Questions:** Add a counter to keep track of how many questions the user has asked during the session.

