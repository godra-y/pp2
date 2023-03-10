import os
print('Exist:', os.access(r'C:\Users\user\Desktop\week 8\dir-and-files.md\file.txt', os.F_OK))
print('Readable:', os.access(r'C:\Users\user\Desktop\week 8\dir-and-files.md\file.txt', os.R_OK))
print('Writable:', os.access(r'C:\Users\user\Desktop\week 8\dir-and-files.md\file.txt', os.W_OK))
print('Executable:', os.access(r'C:\Users\user\Desktop\week 8\dir-and-files.md\file.txt', os.X_OK))