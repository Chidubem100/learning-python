items =["cup","kettle","coffe granules","milk","cream","sugar"]

cup = False
kettle = False
coffe_granule = False
milk = False
cream = False
sugar = False



if milk == True:
    print("milk present")
else:
    print('not present')



def make_a_coffe(need):
    for x in need:
        if "milk" == items:
            print('milk is present')



print(make_a_coffe(items))        