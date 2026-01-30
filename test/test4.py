a = 3
b = 4
def func1():
    global a, b
    a, b = 10, 20

func1()
print(a, b)