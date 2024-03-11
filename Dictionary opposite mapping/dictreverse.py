dict_1 ={}

num = int(input("Enter the number of elemnts in the dictionary: "))

for i in range(num):
    key = input("Enter the key: ")
    value = input("Enter the value: ")

    dict_1 [key] = value

print(dict_1)
keys = list(dict_1.keys())
values = list(dict_1.values())

dict_1.clear()

for i in range(num-1,-1,-1):
    newkey = keys[i]
    newval = values[i]
    dict_1[newkey] = newval

print("Reverse mapped dictionary: ",dict_1)