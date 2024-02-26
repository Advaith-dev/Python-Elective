list_1 = eval(input("Enter the first list: "))
list_2 = eval(input("Enter the second list: "))

list_3 = []

for i in list_1:
    if i in list_2:
        list_3.append(i)

print("List 3 = ",list_3)