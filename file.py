#Read file
'''
file = open('data.txt', 'r')

for line in file:
    print(line)

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

file.close()
'''

#Outometic close the file using with keyword arguments
'''
with open('data.txt') as file:
    for line in file:
        print(line)
'''

#file read using read()
'''
with open('data.txt') as file:
    print(file.read())
'''

# File write using write()
'''
with open('dataName.txt', 'w') as file:
    file.write("Suvendu Chakrabarty")
'''

# Write more then one file using writeline()
lines_data = ['Suvendu\n', 'Sampa\n', 'Tuntuni\n']
''''
with open('dataName.txt', 'w') as file:
    file.writelines(lines_data)
'''

# Append the data without losing the existing data
with open('dataName.txt', 'a') as file:
    file.writelines(lines_data)