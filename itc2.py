income = int(input("Enter your income: "))

sal_income = bool(input("Is this salary based income? T/F: "))
if sal_income:
    income -= 50000 #standard deduction, if the income is salary based

regime = input("Input the type of regime NEW/OLD: N/O: ")
regime = regime.lower()

tax_amount = 0

if regime == "n": 
    tax_slab = int(income/300000)
    if income > 700000: #Rebate of 25000
        if tax_slab == 0:
            tax_amount = 0
        elif tax_slab == 1:
            tax_amount =  income * .05
        elif tax_slab == 2:
            tax_amount = 15000 + ((income - 600000) * .1)
        elif tax_slab == 3:
            tax_amount = 45000 + ((income - 900000) * .15)
        elif tax_slab == 4:
            tax_amount = 150000 + ((income - 1200000) * .2)
        elif tax_slab >= 5:
            tax_amount = 240000 + ((income - 1500000) * .3)
    else:
        print("No tax") # No tax if income is less than 7Lakhs
elif regime == "o":
    if income