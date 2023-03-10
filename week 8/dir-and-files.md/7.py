with open('file1.txt','r') as firstfile, open('file2.txt','a') as secondfile:
    for line in firstfile:  
        secondfile.write(line)