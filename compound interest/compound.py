t = int(input("Enter the number of years: "))
p = float(input("Enter the starting amount: "))
r = float(input("Enter the interest rate: "))

print("Year\tStarting balance\tInterest\tEnding Balance")

for x in range(t):
    i = p * (r/100)
    new = p + i
    print(x+1,"\t",p,"\t","%0.2f" % i,"\t","%0.2f" % new)
    p = new
