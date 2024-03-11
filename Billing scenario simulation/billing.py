stock = {"Ketchup":10,"Cheese":15,"Tomato":5,"Onion":8,"Chilli":6}
price = {"Ketchup":80,"Cheese":150,"Tomato":70,"Onion":100,"Chilli":50}
purchased = {"Ketchup":0,"Cheese":0,"Tomato":0,"Onion":0,"Chilli":0}

items_list = list(stock.keys())

def disp():
    print("\n\nItems in the store: ",end = "\n")
    i = 0
    for items in stock:
        i += 1
        if stock[items] > 0:
            print(i,".",items,stock[items],end = "\n")

def isempty(item):
    if stock[item] > 0:
        return False
    else:
        return True

def decrementer(item,num):
    if (num > stock[item]):
        print("Available quantity : ",stock[item]," \nbuying the entire stock..\n")
        purchased[item] = purchased[item] + stock[item]
        stock[item] = 0
    else:
        stock[item] = stock[item] - num
        purchased[item] = purchased[item] + num
def bill():
    Total_amt = 0
    print("\n\nPURCHASED ITEMS\tQTY\tPRICE\tTOTAL")
    for item in purchased:
        if purchased[item] > 0:
            print(item,"\t",purchased[item],"\t",price[item],"\t",purchased[item]*price[item])
            Total_amt += purchased[item]*price[item]
    print("Total Price: ",Total_amt)

while True:
    disp()
    item = int(input("\nEnter the serial number corresponding to the item to be bought: "))
    item = items_list[item-1]

    if(isempty(item)):
        print("\nCant buy ",item,", stock finished")
        continue
    else:
        qty = int(input("Enter the quantity: "))
        decrementer(item,qty)
    proceed = int(input("1.Continue shopping\n2.Bill out\nEnter your choice: "))
    if(proceed == 1):
        continue
    else:
        bill()
        break

        
