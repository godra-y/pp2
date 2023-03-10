import os
path=r'C:/Users/user/Desktop/week 8/dir-and-files.md/file.text'
print("Only directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("\nOnly files:")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
print("\nAll directories and files :")
print([name for name in os.listdir(path)])