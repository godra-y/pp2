N=int(input())
def genf(N):
    for i in range(1, N+1):
        yield i**2

for i in genf(N):
    print(i)