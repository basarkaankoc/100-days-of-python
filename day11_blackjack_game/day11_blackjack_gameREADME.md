# Day 11 - Blackjack Game 🃏🖥️

This is a terminal-based simulation of the classic card game **Blackjack (21)**.  
It's part of my [100 Days of Python](https://github.com/basarkaankoc/100-days-of-python) learning journey.

---

## 🎯 Game Rules

- Both the user and the computer are dealt 2 cards initially.
- The user may draw more cards (`'y'`) or hold (`'n'`).
- If a hand reaches 21 with the first 2 cards, it's a Blackjack.
- Aces (`11`) are converted to `1` if the score exceeds 21.
- The computer keeps drawing cards until reaching at least 17.
- The highest score wins, without exceeding 21.

---

## 🧠 Concepts Practiced

- Functions and return values
- Lists and random selection
- Blackjack logic (Ace flexibility, win conditions)
- While loops, game loop structure
- User input handling
- ASCII art integration

---

## 📁 File Structure

| File Name       | Description                      |
|------------------|----------------------------------|
| `blackjack.py`   | Main Blackjack game logic        |
| `art.py`         | ASCII logo for game title        |

---
## 💡 Sample Output

```
Do you want to play a game of Blackjack? Type 'y' or 'n': y

.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      `------'                           |__/

Your cards: [10, 9], current score: 19  
Computer's first card: 8  
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 9], final score: 19  
Computer's final hand: [8, 5, 7], final score: 20  
You lose 😤
```

---

## ✅ Features

- Dynamic scoring system with Blackjack rules  
- Ace logic: 11 becomes 1 if over 21  
- Computer plays like a dealer  
- Game loops until user exits  
- Clean output and ASCII title

---

## 📌 Notes

- Runs fully in the terminal  
- Easy to expand (e.g. betting system, multi-round tracking)  
- Great for mastering conditionals and game logic
