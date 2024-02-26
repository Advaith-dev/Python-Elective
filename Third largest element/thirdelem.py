list_1 = eval(input("Enter the list: "))
for i in range(0,2):
    largest = max(list_1)
    list_1[list_1.index(largest)] = 0
largest = max(list_1)
print("Third largest element = ", largest)