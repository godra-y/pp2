s=str(input())
t=s.split()[::-1]
v=[]
for i in t:
    v.append(i)
print(" ".join(v))