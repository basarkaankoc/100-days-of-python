# Day 07 - Hangman Game 🎯

This is a Python implementation of the classic **Hangman** game as part of my [100 Days of Python](https://github.com/basarkaankoc/100-days-of-python) challenge.

---

## 🎮 Game Overview

- A random word is selected from a predefined list.
- The player has 6 lives and must guess the word letter by letter.
- Incorrect guesses reduce lives and show hangman stages.
- Repeated guesses are handled with feedback.
- The game ends when the word is guessed or all lives are lost.

---

## 🧠 Concepts Practiced

- Modular code with external Python files (`hangman_words`, `hangman_art`)
- Lists and strings
- For loops
- Conditionals and input validation
- Game loop with `while not game_over`
- ASCII art rendering

---

## 📄 File Structure

| File Name        | Description                          |
|------------------|--------------------------------------|
| `hangman_game.py` | Main game loop                      |
| `hangman_words.py`| Word list used in the game          |
| `hangman_art.py`  | Hangman logo and stages (ASCII art) |

---

## 💡 Sample Output

Welcome to...

Guess a letter: a
You guessed a, that's not in the word. You lose a life.
LIVES LEFT: 5

Guess a letter: e
Correct guess!

_ _ e _ _ _

...

YOU WIN!


---

## 📌 Note

This game is entirely terminal-based. All visuals are text-based using ASCII art.
