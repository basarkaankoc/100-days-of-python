# Day 06 - Reeborg's World Challenges 🤖

As part of the **100 Days of Python** challenge, I completed several algorithmic puzzles on [Reeborg's World](https://reeborg.ca/reeborg.html).

These challenges helped reinforce:
- `while` loops and conditional logic
- environmental sensing (`front_is_clear()`, `right_is_clear()`, etc.)
- defining reusable functions like `turn_right()`

---

## ✅ Challenges Completed

| Challenge   | Description                      | File Name     |
|------------|----------------------------------|---------------|
| Hurdle 1   | Basic jumping over fixed wall    | `hurdle_1.py` |
| Hurdle 2   | Jump with unknown number of hurdles | `hurdle_2.py` |
| Hurdle 3   | Jump with random spacing         | `hurdle_3.py` |
| Hurdle 4   | Complex hurdles with gaps        | `hurdle_4.py` |
| Maze       | Navigate a complex maze          | `maze.py`     |

---

## 🧠 Concepts Practiced

- Loops with `while not at_goal()`
- Conditional movement: `if`, `elif`, `else`
- Defining helper functions like `turn_right()`
- Environment checks: `front_is_clear()`, `right_is_clear()`, etc.
- Recursive or loop-based maze solving

---

## 💡 Example Snippet (Maze Logic)

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
