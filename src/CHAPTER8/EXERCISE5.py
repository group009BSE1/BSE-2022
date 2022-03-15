count = 0
file = input("Enter file name:")
file = (file + "-short.txt")
with open(file,"r") as a:
    for line in a:
        if line.startswith("From:"):
            continue
        if line.startswith("From"):
            count += 1
            b = line.split()
            print(b[1])
    print(f"There were {count} lines in the file with From as the first word")
