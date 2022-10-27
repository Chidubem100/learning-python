# they are different types of data types that are made use in pytho. They include
# Numeric, Sequence, Dictionary, Boolean and Set.
# to check the type of  a data in python you should use the functon 'type(var name)'

a = 10.0 #the data type is the float numeric data type
print(type(a))

b = 10
print(type(b)) #integer numeric type

name = 'chempath'
print(type(name)) #string type of the sequence

courses = ['chempath', 'hemath', 'microbiology', 'histopat']
print(type(courses)) # list type of the sequence

ed = {'a:33', 'b:33.4'}
ed = ['a'] #list type of the sequence
print(ed)
print(type(ed))

################
#strings in python can be in single or multiple line
varP = "how are you my friend" #single line
print(varP)

varR = 'how do you do,\
i know some times,\
e be like say'
print(varR)

#  you can concatenate a string. that is like joining to seperate strings or values to give a single value
x = "chega "
y = "shege"
print(x + y)


##########
# python is zero indexing 
# you can use the len() to check the length of a character
x = "hey"
print(len(x))
#  you can access the characters of a string just like un an array
name = 'john'
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# SOME BUILT-IN FUNCTIONS