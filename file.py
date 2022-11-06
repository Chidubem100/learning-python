# this is the traditional way of reading file
file = open("data.txt", mode = 'r')
data = file.readline()

print(data)
file.close()

# this is used to read a file that already exists
with open("data.txt", mode = 'r') as file:
    data = file.readline()
print(data)

# this is used to write or create a new file with some content
with open("new_file.txt", 'w') as data:
    data.write("this is a new file")

# this method is used to write more than one line to a file 
with open("data.txt", 'w') as data:
    data.writelines(["\nthis is a new file","\nTrying tnhis out"])


# this is used to append file and the try-except block was used to handle the errors
try:

    with open("new_file.txt", 'a') as data:
      data.writelines(["\nthis is a new file","\nTrying tnhis out"])
except FileNotFoundError as e:
    print("Error", e)      
 
