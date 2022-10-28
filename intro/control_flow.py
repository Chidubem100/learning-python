bill_total = 1433
discount1 = 10
discount2 = 20

# making use of the 'if, elif, and else' statement to control the flow of the programme
# if the total bill is greater than 100 and less than 100 then it should run the next logic
if bill_total > 100 and bill_total < 200: 
    print("Bill is greater than 100")
    bill_total = bill_total - discount1
    # if it is more than 200 then it should the next logic
elif bill_total > 200:
    print("Bill is greater than 200")
    bill_total = bill_total- discount2
else:
    # if the other 2 statements are not met then this logic should be returned
    print("Bill is less than 100")

print("Total bill: " + str(bill_total))    



# the match statement can be a better alternative to the if statement
http_status = 500

match http_status:
    case 200 | 201:
        print("success")
    case 400 :
        print("bad request")
    case 500 | 501:
        print("server error")        
    case _:
        print("unknown")    


# -----------------#
# for loop = used to iterate over a sequence

fav_col = ['blue', "black", "white", "green", "yellow"]

for i in range(5): #first example
    print("looping....", i)

for item in fav_col:
    print("my favourite colour:", item)

for idx,item in enumerate(fav_col):
    print(idx, item)


fav_col = ['blue', "black", "white", "purple", "pink"]
count = 0

while count < len(fav_col):
    print('fav color ', fav_col[count])
    count += 1