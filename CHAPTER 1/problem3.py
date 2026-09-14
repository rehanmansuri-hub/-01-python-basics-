import os

# Specify the directory path
directory_path = '/'  # "." means current directory; change to any path you want

# Get and print contents of the directory
contents = os.listdir(directory_path)

print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)