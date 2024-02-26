#Duration of investment 
t = int(input("Enter the number of years: ")) 

#Initial balance amount
p = float(input("Enter the starting amount: "))

#Rate of interest
r = float(input("Enter the interest rate: "))

print("Year\tStarting balance\tInterest\tEnding Balance")

for x in range(t):

    #Interest amount
    i = p * (r/100)

    #Interest amount added to initial balance or previous balance
    new = p + i

    print(x+1 ,"%-6.2f"% p, "%-2.2f" % i, "%-6.2f" % new)

    #setting new amount as the initial balance for the next iteration
    p = new
