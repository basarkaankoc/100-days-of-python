# Day 10 - Calculator Project 🧮

A terminal-based calculator built in Python as part of my [100 Days of Python](https://github.com/basarkaankoc/100-days-of-python) journey.

It supports:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

You can chain operations using the result of the previous calculation, start a new calculation, or exit anytime.

---

## 🧠 Concepts Practiced

- Functions and return values
- Dictionaries with functions as values
- Loops and recursion
- User input and type casting (`float`)
- Input validation and conditional branching

---

## 📁 File Structure

| File Name        | Description                          |
|------------------|--------------------------------------|
| `calculator.py`  | Main program logic                   |
| `art.py`         | Contains ASCII logo (`art.logo`)     |

---
## 💡 Sample Output

```
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

What's the first number?: 10  
Pick an operation: +  
What's the next number?: 5  
10 + 5 = 15.0

Type 'y' to continue calculating with the result, 'n' to start a new calculation, or 'c' to exit: y  
Pick an operation: *  
What's the next number?: 2  
15.0 * 2 = 30.0

Type 'y' to continue calculating with the result, 'n' to start a new calculation, or 'c' to exit: c  
Calculator exited. Goodbye!
```

---

## ✅ Features

- Chained operations using previous result  
- Clean restart option (`n`)  
- Exit command (`c`) without closing terminalS
- Simple and readable code structure
- ASCII art interface for aesthetics

---

## 📌 Notes

- You can add more operations by expanding the `operations` dictionary.
- To clear screen properly, consider using `os.system('cls')` on Windows or `clear` on Unix-based systems.
- Recursion is used to restart the calculator — which works fine here but be cautious of stack overflow in bigger apps.


