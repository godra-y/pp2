def count_lines(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
        return i+1
print(count_lines(r'C:/Users/user/Desktop/week 8/dir-and-files.md/file.txt'))