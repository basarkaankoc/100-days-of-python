# Day 05 - Password Generator 🔐

This is a Python program that generates strong, random passwords based on the user's input.  
It's part of my [100 Days of Python](https://github.com/basarkaankoc/100-days-of-python) journey.

---

## 💡 What It Does

The program:
- Asks how many **letters**, **symbols**, and **numbers** you want in your password
- Randomly selects characters from each category
- Shuffles them to prevent predictable patterns
- Combines them into a single, strong password

---

## 🎮 Sample Run

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
5
How many symbols would you like?
2
How many numbers would you like?
3
Generated password: f%R9m$5K2a
```

---

## 📚 Concepts Used

- Lists and list methods (`append()`, `shuffle()`)
- `random.choice()` and `random.shuffle()`
- For loops
- String concatenation
- User input handling

---

## 📄 Files

- `password_generator.py`: The main script for generating passwords
