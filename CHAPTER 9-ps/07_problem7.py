with open("log.txt", "r") as f:
    lines = f.readlines()

for line_number, line in enumerate(lines, start=1):
    if "python" in line.lower():
        print("Python found on line:", line_number)