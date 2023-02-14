def uniq(num):
    for i in range(len(num)):
        s=num.count(num[i])
        if s==1:
            print(num[i])
u=[int(i) for i in input().split()]
uniq(u)