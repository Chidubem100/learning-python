# global scope
my_global = 10 # this can be accessed any where

def fn1():
    local_v = 1 # this variable can only be accessed inside this function and its an example of local scope 
    print("print my global", my_global)
    print("print my global", local_v)

fn1()

#enclosed scope 
def fn1():
    enclose_v = 4

    def fn2():
        local_y = 1 #this  can only be accesed within this function and not on the outer part
        print("print my enclosed scope", enclose_v)
        print("print my global", local_y)
        # print("print my global", my_global)
    fn2()
    print("print my enclosed scope", enclose_v)

fn1()