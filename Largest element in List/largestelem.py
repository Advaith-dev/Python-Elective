list_1 = eval(input("Enter the list: "))
print("Largest element in ", list_1 ," = ",max(list_1))
print("smallest element in ", list_1 ," = ",min(list_1))

len_1 = len(list_1)

largest = list_1[0]
smallest = list_1[0]

for i in range(0,len_1 - 1):
    if(largest < list_1[i+1]):
        largest = list_1[i+1]

print("(manual method) Largest element in ", list_1 ," = " , largest)
for i in range(0,len_1 - 1):
    if(smallest > list_1[i+1]):
        smallest = list_1[i+1]

print("(manual method) smallest element in ", list_1 ," = ", smallest)