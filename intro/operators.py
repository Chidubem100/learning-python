# these are examples of math operators. they are
# addition, subtraction, division and multiplication respectively
from pickle import TRUE


print(2+2)
print(23-4)
print(10/2)
print(10*3)

# logical operators. they example includes
# and, or, not
a = True
x= True
# the 'and operator' has a codition for the both statements to be true in order to print out something or to execute the next function 
if a and x:
    print("All true")

a = False
x= True
# the 'or operator' has a codition for either of the statements to be true in order to print out something or to execute the next function 
if a or x:
    print("All true1")


a = False
x= True
# the 'not operator' checks if the a or the first statement is false and its check against the other statement.
# it will return something if the two are false
# the first part must be false
if not(a) or not(x):
    print("All True")    

