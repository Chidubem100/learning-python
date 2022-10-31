
from unicodedata import name


names = ["duby", "bona", "demi", "santa","zik"]

# for loop
for idx, name in enumerate(names):
    print(idx,name)


# while loop
count = 0
while count < len(name):
    print(names)
    count +=1

# 
for name in range(4):
    for j in range(2):
        print(names, end = " ")
    print()   