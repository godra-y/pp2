n=-1
max=0
cnt=0
while n!=0:
    n=int(input())
    if n>max:
        max, cnt=n, 1
    elif n==max:
        cnt+=1
print(cnt)