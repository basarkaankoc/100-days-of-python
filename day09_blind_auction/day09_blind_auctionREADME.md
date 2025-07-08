# Day 09 - Blind Auction Project 💰

This is a terminal-based **Blind Auction** program built in Python as part of my [100 Days of Python](https://github.com/basarkaankoc/100-days-of-python) journey.

Multiple bidders can enter their names and secret bid amounts. At the end, the highest bidder is announced.

---

## 🎯 What It Does

- Allows multiple users to enter a name and bid amount
- Clears the screen (simulated with `\n` * 50) between bidders
- Stores all bids in a dictionary
- Determines the highest bidder using a loop
- Handles invalid input if necessary

---

## 🧠 Concepts Practiced

- Dictionaries and key-value pairs
- Loops and conditional logic
- Function creation
- Input handling
- Basic validation

---

## 📄 File Structure

| File Name          | Description                        |
|--------------------|------------------------------------|
| `blind_auction.py` | Main script with auction logic     |
| `art.py`           | ASCII logo displayed at startup    |

---

## 💡 Sample Output

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

What is your name?: Alice
What is your bid?: $200
Are there any other bidders? Type 'yes or no'. 
yes


What is your name?: Bob
What is your bid?: $250
Are there any other bidders? Type 'yes or no'.
no

The winner is Bob with a bid of $250
```

## 📝 Notes

- This program uses `\n * 50` to simulate a screen clear.  
- A more advanced version could use `os.system('cls' or 'clear')`.
- Bids are stored in a dictionary with the name as the key and amount as value.


