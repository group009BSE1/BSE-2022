list1 = []
list2 = []
filename = input('enter file name: ')
with open(filename,"r") as file:
    for line in file:
        x = line.rstrip()
        for a in line.split():
            list1.append(a)
        for a in list1:
            if a not in list2:
                list2.append(a)
    list2.sort()
    print(list2)
