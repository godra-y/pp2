import re
file=open('C:/Users/user/Desktop/week 7/Assignment 5/regex.md/row.txt', 'r', encoding='UTF8')
result=re.sub('[ ,.]', ':', file.read())
print(result)