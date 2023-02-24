n=int(input())
def genf(n):
    for i in range(n, -1, -1):
        yield i
for i in genf(n):
    print(i)