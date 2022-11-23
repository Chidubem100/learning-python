# how to reverse a string using the slice method
# str[start:stop:stop]  #thisis called the extended parameter synthax

trial = "genesis"
new_trial = trial[::-1] #the -1 is to tell the code to start reversing it from the right instead from the left
# print(new_trial)

# how to reverse a string using recursion
def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:]) + str[0] 

str = "emeka"
reverse = string_reversal(str)
# print(reverse)           

# print(string_reversal("akama"))


# MAP and FILTER

menu = ["yam","plantain","beans","cassava","banana"]

def find_carbs(food):
    if food[0] == 'c':
        return food

# for map function
map_food= map(find_carbs,menu) # one thing to not here is that the fuction is not called rather it is passed like an argument
for x in map_food:
    print(x)


# for the filter function
map_carbs = filter(find_carbs,menu)
for y in map_carbs:
    print(y)

# the big difference btwn these two is that the filter function returns a new list unlike the map function
# which will return the old list and the values that are true but the ones that are false will be returned as none


z = ["alpha", "bravo","fharlie"]
new_z = [i[0]*2 for i in z]
print(new_z)

def sum(n):
    if n == 1:
        return 0
    return n + sum(n-1) 

a = sum(5)
print(a)       