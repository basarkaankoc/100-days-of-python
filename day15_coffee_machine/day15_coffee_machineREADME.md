# Day 15 - Coffee Machine ☕

This is a simple console-based **Coffee Machine Simulator** written in Python.  
As part of my [100 Days of Python](https://github.com/basarkaankoc/100-days-of-python) challenge, this project simulates a coffee machine that takes user input, manages resources, and processes coin-based transactions.

---

## 🎯 Features

- ☕ Choose from **espresso**, **latte**, or **cappuccino**
- 💰 Insert coins (quarters, dimes, nickels, pennies)
- 📉 Tracks remaining **resources** (water, milk, coffee)
- 💵 Calculates change and **updates profit**
- 📄 Type `report` to print current machine status
- ⛔ Type `off` to turn off the machine

---

## 🧠 Concepts Used

- Python dictionaries and nested data structures
- Function decomposition and return values
- Global variables
- Conditionals and loops
- Input handling
- Float arithmetic and rounding

---

## 🖥️ Sample Output

What would you like ?(espresso/latte/cappuccino) latte
Please insert coin:
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte. Enjoy ☕

What would you like ?(espresso/latte/cappuccino) report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

What would you like ?(espresso/latte/cappuccino) off

---

## 📁 File

- `coffee_machine.py` – Main Python script

---