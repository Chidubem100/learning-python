# ENCAPSULATION
class Alpha:
    def __init__(self):
        self._a_ = 2.
        self._b = 2.

class MyClass:
    print("hello")
    a = 5
    n_m = a+4
    print(n_m)

    # creating a method
    def hello(self): #the keyword 'self' is a convention that is passed in a method to help point to any instance od that method
        num_1 = 4
        num_2 = 299
        t_num = num_1*num_2
        for x in range(100):
            if x == 50:
                t_n =x*54
                print(t_n)
                return t_n
        return t_num
    pass #this plays as a placeholder to show that there is nothing to be executed yet

# the instantiation kind of operation
my_class = MyClass()

# the attribute referencing type 
my_num = MyClass.n_m
print(my_num)

# refrencing an instance method
print(my_class.n_m)
print(my_class.hello()) #accessing the method


# Myclass is the class name
# my_class is the object name(the object name can be anything)




# Another example

class House:
    num_rooms = 5
    bathrooms = 2
    
    def cost_evalation(self):
        
        print(self.bathrooms)
        pass

house = House()
House.bathrooms = 8 #updated the class attribute
print("Number of bathrooms is" + " " + str(house.bathrooms))    
print("Number of rooms is" + " " + str(house.num_rooms))  



# using the init method
class Recipe():
    def __init__(self,dish,items,time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
        
    def contents(self):
        print("The "+ self.dish + " has " + str(self.items) + \
            " and takes " + str(self.time) + "min tp prepare")


pizza = Recipe("Pizza", ["cheese", "bread", "tomatoes"], 45) 
pasta = Recipe("Pasta", ['penne', "sauce"], 55)               

print(pizza.items)
print(pasta.items)

print(pizza.contents())


# class
class MyFirstClass():
    print("who wrote this")
    index = "Author Book"

    def hand_list(self,philosopher,book,year):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book + year) 

whodunnit = MyFirstClass()
whodunnit.hand_list("sun tzu", "the art of war ", str(2022))            

# using instance objects without afftecting the class
class Payslips:
    def __init__(self,name,payment,amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"    

    def status(self):
        if self.payment == 'yes':
            return self.name + " is paid " + str(self.amount)    
        else:
            return self.name + " is not paid yet"

drogba = Payslips("drogba", "no",2000)
emeka = Payslips("emeka", "no", 1000)            


print(drogba.status(), '\n', emeka.status())

drogba.pay()
print('### AFTER PAYMENT ###')
print(drogba.status(), '\n', emeka.status())


# inheritance
"""
the the original class is called the parent class while the inherited class is called the child class.
the child class do have the behaviour and attributes of the parent class. you can add new properties to the child class and 
you can modify the inherited properties. any change in the parent class will affect the child class


"""
# parent class
class Parent:
    def __init__(self) -> None:
        self.a = "i am a class"

# child class
class Child(Parent):
    pass #empty child class

# child class instance
c = Child()
print(c.a) 

# example
class Employees:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last

class Supervisor(Employees):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)     
        self.password = password

class Chef(Employees):
    def leave_request(self, days):
        return "May I take leave for " + str(days) + " days"

edu = Supervisor("edu", "A" ,"akwaba")

emik = Chef("emik", "E")
james = Chef("james", "J")

print(emik.leave_request(3))
print(edu.password,edu.last,edu.name)
print(emik.name)