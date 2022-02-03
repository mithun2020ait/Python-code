#Write a function which take a list of name as a argument and greets to "hello", to everyone
def greet_everyone(names):
    for name in names:
        print("hello", name)

name_of_pepole = ['Suvendu', 'Sampa', 'Tuntuni']
greet_everyone(name_of_pepole)