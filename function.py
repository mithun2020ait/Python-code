#Function without parameters
# def greet():
#     print("Hello Suvendu")

# greet()

#Function with parameters
# def greet(name):
#     print("Hello", name)

# greet('Suvendu')
# greet('Mithun')

def greet(name, dish="Pasta"):
    print("Good morning", name)
    print("please eat", dish)

# greet('Suvendu', 'chickn')

#Returning function
def sum_of_list(a):
    return sum(a)

marks = [45, 55, 42, 30]
sum_of_marks = sum_of_list(marks)
# print(sum_of_marks)

def sum(a, b):
    return a+b

print(sum(20, 25))

#Arbitrary arguments
def my_function(*kids):
    print("The youngest child is " + kids[2])

#my_function("Pallibi", "Suvendu", "XYZ")

#Recursion
def sum(n):
    if(n == 1):
        return 1
    return n + sum(n-1)

print(sum(5))

def power(x, y):
    if(y == 0):
        return 1
    return x * power(x, (y-1))

print(power(2,3))



