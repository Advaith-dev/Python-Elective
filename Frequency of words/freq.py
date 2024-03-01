word = input("Enter a string: ")
count_dict = {}

list_words = word.split()

print(list_words)

for i in list_words:
    count_dict[i]= list_words.count(i)

print("Count of each word : ",count_dict)
