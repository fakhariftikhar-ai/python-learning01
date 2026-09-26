X = 10 # Global variable

def my_function():
    global x
    x = 5
    y = 4 # local variable
    print(y)

my_function()
print(x)