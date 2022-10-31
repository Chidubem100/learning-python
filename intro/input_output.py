# you can use the input function to access or get data from your user
num = input('please  enter a number :' )
print(num)

# you can use the input to access numerous data
firstNum = input("Please enter first number:")
secondNum = input('Please enter your second number :' )

# doing a simple addition arethimetics
# using the int() to convert the string to intergers 
print(int(firstNum) + int(secondNum))


# using concatenation in output
str1 = input("Please enter first name:")
str2 = input('Please enter your second name :' )

print("Hello " + str1 + ' ' + str2)

# using the .format() to concatenate a string
print("Hello {} {}".format(str1,str2))


user_num_1 = input('First number is: ')
user_num_2 = input('Second number is: ')
user_sum = float(user_num_1) + float(user_num_2)
print(user_sum)