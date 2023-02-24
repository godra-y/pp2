n=int(input())
m=0
while n!=0:
    k=int(input())
    if k!=0 and n<k:
        m+=1
    n=k
print(m)
