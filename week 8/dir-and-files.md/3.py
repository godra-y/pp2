import os
path=r'C:\Users\user\Desktop\week 8\dir-and-files.md\file.txt'
print("Test a path exists or not:")
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDirectory name of the path:")
print(os.path.dirname(path))