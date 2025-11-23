# --- 1. FUNCTION DEFINITIONS ---

def items(file_path):
    itemAvailable = {}

    try:
        with open(file_path, "r") as my_file:
            itemsAvailable = my_file.readlines()
    except FileNotFoundError:
        print(f"ERROR: Inventory file not found at {file_path}")
        return itemAvailable

    print("-------------------ITEMS AVAILABLE IN OUR STORE-------------------")
    for item in itemsAvailable:
        item = item.strip()

        if item == "":
            continue

        parts = item.split()

        if len(parts) < 2:
            continue

        try:
            item_price = float(parts[-1])
        except ValueError:
            continue

        item_name = " ".join(parts[:-1])
        itemAvailable[item_name.title()] = item_price
        print(f"{item_name}: {item_price}")
        
    print("*" * 20)
    return itemAvailable


def process(itemAvailable):
    shoppingDict = {}
    stationaryitems = input("Do you want to proceed buying? (yes/no): ")

    while stationaryitems.lower() == "yes":
        item_added = input("Add an item: ").title()

        if item_added in itemAvailable:
            try:
                item_qty = int(input("Add quantity: "))
            except ValueError:
                print(" Invalid quantity. Please enter a whole number.")
                continue
             # Calculate subtotal
            subtotal = itemAvailable[item_added] *item_qty
            if item_added in shoppingDict:
                shoppingDict[item_added]["quantity"] += item_qty
                shoppingDict[item_added]["SubTotal"] += subtotal
            else:
                shoppingDict[item_added] = {
                    "quantity": item_qty,
                    "SubTotal": subtotal
                }

            print(shoppingDict)

        else:
            print(" Item not found! Unable to add item.")

        stationaryitems = input("Do you wish to add more items? (yes/no): ")
        
    return shoppingDict


def generatebill(user_Name, shoppingDict):
    """
    Calculates the final total and prints the formatted bill summary.
    """
    print("CUSTOMER NAME:", user_Name)
    print("\n********* BILL SUMMARY ************\n")
    print("Item            Quantity         SubTotal")

    total = 0
    for key in shoppingDict:
        subtotal = shoppingDict[key]['SubTotal']
        print(f"{key:15} {shoppingDict[key]['quantity']:5}          {subtotal:15.2f}")
        total += subtotal

    print("\n-----------------------------------")
    print(f"TOTAL BILL: {total:.2f}")
    print("*-*-*-*-*-*-*-*-*-*-THANK YOU-*-*-*-*-*-*-*-*-*")
    print("Hope to see you back soon!")
#MAIN PROGRAM EXECUTION
userName = input("Please enter your name: ")
user_Name = userName.upper()
WelcomeMessage = f"WELCOME TO THE STATIONARY STORE {user_Name}"
print("")
print("=" * len(WelcomeMessage))
print(WelcomeMessage)
print("=" * len(WelcomeMessage))
print("")
FILE_PATH = r"C:\Users\HP\Downloads\stationaryitems.txt"#file path
itemAvailable = items(FILE_PATH)#function call to load inventory

if not itemAvailable:
    print("System halted: Inventory is empty or file error occurred.")
else:
    shoppingDict = process(itemAvailable)#function call to process
    generatebill(user_Name, shoppingDict)#function call to generate bill