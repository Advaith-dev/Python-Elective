list_1 = eval(input("Enter the list: "))

list_2 = []

for i in list_1:
    if i % 2 == 0:
        list_2.append(i)

print("List 2 = ",list_2)