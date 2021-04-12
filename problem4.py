file_name= input("Enter File Name: ")
from collections import Counter

inFile= open(file_name, "r")
data_set = inFile.read()

split_it = data_set.split()

Counter = Counter(split_it)

most_occur = Counter.most_common(20)
inFile.close()


f = open("popular_Words.txt", "w+")
f.write(str(most_occur))

print("popular words extracted successfully!")
