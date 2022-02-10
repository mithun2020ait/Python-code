#Create a Class
# class MyClass:
#     x = 5

# p = MyClass()
# print(p.x)


#__init__() function
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Suvendu", 25)

# print(p1.name)
# print(p1.age)


#Object methods
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello my name is " + self.name)

p = Person("Suva", 25)
# p.my_function()



class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    
    def my_func(self):
        print("My car is " + self.color +" color" + " and is is " + self.brand)

car = Car("Yellow", "audi")
car.brand = "maruti"
car.color = "black"
car.my_func()

#class without the self keyword
class Cat:
    def __init__(mysilly, name, color):
        mysilly.name = name
        mysilly.color = color

    def my_cat(abc):
        print("The is name is " + abc.name + " and it is " + abc.color + " color")

cat = Cat("pussy", "white")
cat.my_cat()
