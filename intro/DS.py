# for list data structure

var_list = [1,2,3,4,4]

# ways to print out what you have on your list
print(*var_list)
print(var_list, sep=" ") # the sep keyword is used to seperate or space the items

# ways to add items to the list

var_list.insert(len(var_list), 5) #using the insert method and the len keyword to specify where it should enter

var_list.append(6) #using the append method. there is no need to specify where it should eneter bcz it will automatically follow the sequence

var_list.extend([6,7,8])

# print(var_list, sep=" ")

# ways to remove an item from the list

var_list.pop(4)
#you will have to specify the index of the item you wish to remove

del var_list[5]

print(var_list, sep=" ")

# iterate using for loop

for x in var_list:
    print("value: ", x)


###############
# tuple for DS
# they are immutable

var_tuple = (2,"heello", 4,5, 4.6)

print(var_tuple.count(1))
print(var_tuple[3])

for y in var_tuple:
 print(y) 



##########
# set
#they dont allow duplicate values

var_set = {1,2,3,4,5}
print("set values: ", var_set)  


#########
# dictionaries
# they make useof key value pair and are mutable.
# it doesnt allow duplicate value

var_dict = {1:"test", 'name': 'jim', 'number': 3}
var_dict[1] = "update" #to update a value that is already there
del var_dict[1]
print(var_dict['name']) #to access it using a key value

for x in var_dict: #to iterate over a dictionary. this method only prints out the keys
    print(x)

for key, value in var_dict.items(): # this method is used to print out both the key and value
    print(str(key) + " : " + str(value)) 

print(var_dict)


# ########
# args
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum 

print(sum_of(3,4,2))       

# kwargs
def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return round(sum,2) 

print(sum_of(cake=4.466, beans=38.4, icecream=394.39))       
