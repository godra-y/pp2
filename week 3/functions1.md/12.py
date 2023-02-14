def histogram( items ):
    for i in items:
        res=''
        times=i
        while(times>0):
            res+='*'
            times=times-1
        print(res)
a=[int(i) for i in input().split()]
histogram(a)