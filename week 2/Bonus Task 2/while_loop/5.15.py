n=int(input())
i=0
x=0
x1=0
x2=0
while x<=n:
    x=x1+x2
    x1, x2=x, x1
    i+=1
if n==x2:
    print(i)
else:
    print(-1)    