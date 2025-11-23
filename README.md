# STATIONARY MANAGEMENT STORE PYTHON
It utilizes dictionaries to store ITEM prices, user input for purchasing (item and quantity), calculates subtotal, and generates bill summary."
This project is a command-line application designed to simulate the core functions of a small retail stationary store: loading item inventory, allowing a user to select items and quantities, and generating a final bill.
This little app keeps it simple and powerful:
Primary Language: Python (That's it! No heavy frameworks needed.)
Data Storage: Just the basic Python Dictionary (keys for item names, values for prices/cart details).
Inventory Source: A plain Text File (.txt). Easy to read, easy to edit.
FEATURES
Reads Your Stock List: It quickly grabs all the item names and prices from your stationaryitems.txt file, so it knows exactly what you're selling and for how much!
Keeps Order: If you try to run the app without the inventory file, it politely yells "ERROR: Inventory file not found!" instead of just crashing.
Simple Shopping: You tell it what you want (e.g., "Black Pen") and how many (e.g., "2"), and it puts it in the digital shopping basket.
No Crash Guarantee: You can't accidentally break it by typing "a lot" instead of "5" for the quantity. It checks if you entered a real number and asks you nicely to try again if you didn't.
Smart Cart Aggregation: If you add the same item twice, it doesn't create two line items; it simply adds up the quantities and recalculates the total for that item.
Item Checker: It won't let you add an item (like "Flying Car") that isn't actually in your stock list.
Final Receipt Creator: After shopping, it prints out a clear, tidy, and organized bill summary—just like a real store!
The Bottom Line: It calculates the Grand Total automatically, so you know exactly how much to charge!
