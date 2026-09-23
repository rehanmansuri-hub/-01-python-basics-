with open("this.txt", "r") as f:
    file1 = f.read()

with open("this_copy.txt", "r") as f:
    file2 = f.read()

if file1 == file2:
    print("Both files are identical.")
else:
    print("Both files are different.")