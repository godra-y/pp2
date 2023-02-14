class Rectangle():
    def __init__(self, l, w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
n=int(input())
m=int(input())
newRectangle=Rectangle(n, m)
print(newRectangle.area())