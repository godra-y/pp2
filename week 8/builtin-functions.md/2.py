s=str(input())
cntc=0
cnts=0
for i in s:
    if i.isupper():
        cntc+=1
    else:
        cnts+=1
print(cntc)
print(cnts)