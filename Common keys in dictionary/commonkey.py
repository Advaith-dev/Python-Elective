num1 = int(input("Enter the number of elements in D1: "))

num2 = int(input("Enter the number of elements in D2: "))

D1 = {}
D2 = {}

print("--------------------------")
for i in range(num1):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    D1[key] = value

print("--------------------------")
for i in range(num2):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    D2[key] = value

D1_keys = D1.keys()

print("Common keys are: ",end="")
for k in D1_keys:
    if k in D2:
        print(k ,end="")

#[item for item in keys1 if item in keys2] list comprehension
        
