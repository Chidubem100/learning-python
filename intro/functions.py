


def calc_tax(bill, tax_rate):
    return round((bill * tax_rate)/100.00, 2)

# print("Total Tax:", calc_tax(178,15))    
# print("Total Tax:", calc_tax(2899,30))


##### ALGORITHM #########
# an algorith is step my step way of solving a problem



# Lets check if the string is a palindrome

def isPalindrome(str):
    start_index = 0
    end_index = len(str)-1

    # iterate over the string and check if the start index
    # is not same to the end index then it should return false
    for x in str:
        if str[start_index] != str[end_index]:
            return False
    return True

# print(isPalindrome('civic')) 

#linear time
def find_num(num):
    count = 0
    for x in range(100):
        if x == num:
            print(count)
            return x
        count += 1

# print(find_num(70))            


# this is an example of pure function
names = ['ogo','ifelu','ebube','rayo']

def add_to_list(names, Nname):
    nList = names.copy()
    nList.append(Nname)
    return nList

print(add_to_list(names,'ifeudo'))
    