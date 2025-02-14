names = []

name = input("Enter name ")
names.append(name)

while name != "":
    name = input("Enter name ")
    names.append(name)

    if name == "":
        names.remove("")
        names.sort(reverse=True)
        print(names)