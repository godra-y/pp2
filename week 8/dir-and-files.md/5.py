fruits=['apple', 'banana', 'pear']
with open('file.txt', "w") as myfile:
        for i in fruits:
                myfile.write("%s\n" % i)
drop=open('file.txt')
print(drop.read())