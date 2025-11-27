# STATIONARY MANAGEMENT STORE PYTHON


# OVERVIEW OF THE PROJECT 
The Stationary Management System is a console-based retail application developed in Python. The system aims to simulate a fundamental point-of-sale (POS) process for a small stationary store. Its core functions are to load inventory from an external file, facilitate an interactive purchasing session for a customer, calculate all necessary subtotals, and generate a final, formatted sales receipt. The project emphasizes robustness through file error handling and data validation for user inputs.



# Features
Feature                                                   Description                                                                Related Function

Inventory Initialization     Reads item names and prices from a specified external text file (stationaryitems.txt)                      items()
                             at the start of the program.
                             
Error Handling              "Gracefully handles the critical FileNotFoundError if the inventory data file is missing,                   items()
 (File I/O)                   preventing the program from crashing and providing a clear error message."
 
Input Validation            "Ensures that the quantity entered by the user during the shopping process is a valid whole                 process()
(Quantity)                   number (integer). Invalid input is rejected, and the user is prompted to try again.  
                             
Case-Insensitive Matching   "Converts both the inventory item names and the customer's input to Title Case (.title())                   items(), process()
                            to ensure reliable lookups, regardless of how the customer types the item name."
                            
Interactive Shopping Loop    Implements a user-friendly while loop that allows the customer to repeatedly add items                     process()
                             to their cart until they explicitly choose to exit.
                             
Dynamic Cart Management     Uses a nested dictionary (shoppingDict) to act as the shopping cart. It intelligently                       process()
                            updates the total quantity and cumulative subtotal if an item is added more than once.
                            
Financial Calculation      "Calculates the subtotal for each item added and, critically, determines the final grand                     process(), generatebill()
                           total of the entire purchase."
                           
Formatted Receipt          "Produces a clean, structured bill summary, using Python's f-string formatting to ensure                      generatebill()
  Generation                perfect alignment for item names, quantities, and monetary values (2 decimal places)."


# Technologies/Tools Used 

Primary Language: Python 3.x
Rationale: Chosen for its readability, ease of file handling, and excellent dictionary manipulation capabilities, making it ideal for rapid prototyping of management systems.

Data Storage: Plain Text File (.txt)
Rationale: Simple external storage for inventory data, simulating a basic database without requiring complex database management systems (DBMS).

Development Environment: Any standard Python IDE (e.g., PyCharm, VS Code, Thonny) or a basic terminal environment.

#Steps to Install & Run the Project

This project is a standalone Python script, requiring no special libraries beyond the standard installation.

1. Setup the EnvironmentEnsure you have Python 3.x installed on your operating system (Windows, macOS, or Linux).
2. Save the CodeSave the entire Python script provided in the prompt into a file named stationary_app.py.
3. Create the Inventory Data FileThe script is hardcoded to look for the inventory file at a specific location:PythonFILE_PATH = r"C:\Users\HP\Downloads\stationaryitems.txt"
Action A (Recommended): Create a text file named stationaryitems.txt at the exact path: C:\Users\HP\Downloads\.
Action B (Alternative): If you cannot use that path, you must edit the FILE_PATH variable in stationary_app.py to point to a location accessible on your machine (e.g., "inventory.txt" if placed in the same directory as the script).
4. Populate the Inventory FileThe file must contain one item per line, with the item name followed by its price (separated by spaces).Example stationaryitems.txt ContentA4 White Paper
5. Run the ApplicationOpen your command prompt or terminal, navigate to the directory where you saved stationary_app.py, and execute the script:Bash


#Screenshots

<img width="1058" height="885" alt="Screenshot 2025-11-23 200722" src="https://github.com/user-attachments/assets/113e4684-e4c2-4e39-b23a-18fd78a86fb9" />
<img width="1542" height="633" alt="Screenshot 2025-11-23 200916" src="https://github.com/user-attachments/assets/9791185a-566b-4702-aa41-70d3ae2649dd" />

