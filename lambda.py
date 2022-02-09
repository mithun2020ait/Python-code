#Lambda function
x = lambda a: a + 10

# print(x(5))

#Lambda function with multiple argument
x = lambda a, b: a * b

print(x(5,6))

def my_function(n):
    return lambda a: a *n

mydouble = my_function(3)

print(mydouble(11))