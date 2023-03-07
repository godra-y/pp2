import re
file=open('C:/Users/user/Desktop/week 7/Assignment 5/regex.md/row.txt', 'r', encoding='UTF8')
def camel_to_snake(file):
        import re
        str1=re.sub('(.)([A-Z][a-z]+)', r'\1_\2', file)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
print(camel_to_snake(file.read()))