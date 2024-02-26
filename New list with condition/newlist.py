list_1 = eval(input("Enter the list: "))
list_2 = []

num = int(input("Enter a number: "))

for i in list_1:
    if i < num:
        list_2.append(i)

print("List 2: ",list_2)
