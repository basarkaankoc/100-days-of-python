# Day 08 - Caesar Cipher 🔐

This is a simple implementation of the classic **Caesar Cipher** encryption algorithm, built with Python as part of my [100 Days of Python](https://github.com/basarkaankoc/100-days-of-python) journey.

The program allows users to encode or decode messages by shifting the letters of the alphabet.

---

## 🧠 Concepts Practiced

- Functions with parameters
- `if` / `else` logic
- Looping through strings
- Modulo operator `%` to wrap alphabet
- User input handling
- Importing from custom modules

---

## 🚀 How It Works

1. The user selects whether to **encode** or **decode**
2. Enters a message
3. Chooses a shift amount
4. The message is transformed based on the Caesar cipher algorithm

---

## 📄 File Structure

| File Name         | Description                          |
|-------------------|--------------------------------------|
| `caesar_cipher.py` | Main program logic                   |
| `art.py`           | Contains the ASCII logo (`art.logo`) |

---

## 💡 Sample Run

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here is the encoded result: mjqqt btwqi

Type 'yes' if you want to go again. Otherwise, type 'no':
no
Goodbye

---

## 📌 Notes

- Non-alphabet characters (e.g., spaces, symbols) are preserved.
- The cipher wraps around the alphabet using modulo (`%`).
- You can keep running the program multiple times in one session.
