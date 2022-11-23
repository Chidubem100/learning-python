sam = {1:'tea',2:'mineral',3:'eba'}

for x in sam:
    print(x)

def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)
recursion(11)

def bigo(numbers):
    for i in numbers:
        print(numbers)

bigo([1,2,3]) 

def d():
    color = 'green'
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("color: " + color)
    color = "red"
color = "red"
d()

numb = 9
class Car:
    numb = 5
    bathroomss = 2
def cost_eval(numb):
    numb = 10
    return numb
class Bike():
    numb = 11
cost_eval(numb)
car = Car()
bike = Bike()
car.numb = 7
Car.numb = 2
print(numb)