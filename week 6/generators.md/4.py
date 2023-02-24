import math
a=int(input())
b=int(input())
def square(a, b):
    for i in range(a, b):
        yield math.sqrt(i)
for i in square(a, b):
    print(i)