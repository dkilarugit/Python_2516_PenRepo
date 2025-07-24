a = 5
b = 3.2
c = a + b
print("Sum:",c)
print("Data type of c:", type(c))

""" Output:
Sum: 8.2
Data type of c: <class 'float'>"""

a = 5
b = "Hello"
c = a + b
print("Sum:",c)
print("Data type of c:", type(c))

"""Output:
    c = a + b
        ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'"""