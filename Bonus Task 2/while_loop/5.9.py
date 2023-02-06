n=-1
ind=-1
max=0
len=0
while n!=0:
    n=int(input())
    if n>max:
        max=n
        ind=len
    len+=1
print(ind)