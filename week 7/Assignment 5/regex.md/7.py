import re
file=open('C:/Users/user/Desktop/week 7/Assignment 5/regex.md/row.txt', 'r', encoding='UTF8')
def snake_to_camel(file):
        import re
        return ''.join(x.capitalize() or '_' for x in file.split('_'))
print(snake_to_camel(file.read()))

