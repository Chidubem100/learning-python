
from distutils.command.install_egg_info import to_filename


total_bill = 1890
discount1 = 20
discount2 = 10

if total_bill > 1000 and total_bill < 1500:
    x = total_bill-discount2
    print("Total bill is "+ str(x))
elif total_bill > 1500:
    y = total_bill - discount1
    print("Total bill is "+ str(y))
else:
    print("Total bill is less than 1000")        


######
# I used the input to get the price and i first converted the input to interger

q = int(input("Price: "))   
dicount = 2
dicount1 = 4


if q > 30 and q < 100:
    p = q - dicount
    print("Total bill is "+ str(p))
elif q > 100:
    w = q - dicount1
    print("Total bill is "+ str(w))
else:
    print("total bill is too low for a discount")         


####
shoe = int(input("price of shoe: "))
bag = int(input("price of bag: "))
wig = int(input("price of wig: "))
spray = int(input("price of spray: "))

discount = 10
discount3 = 15

totalPrice = shoe + bag + wig + spray


if totalPrice > 70 and totalPrice < 100:
    rPrice = totalPrice - discount
    print("Total bill is "+ str(rPrice))
elif totalPrice > 100:
    redPrice = totalPrice - discount3
    print("Total bill is "+ str(redPrice))
else:
    print("Total price does is not available for discount")        
    