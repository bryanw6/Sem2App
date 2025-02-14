list = []
number = (input("Please input a number "))
list.append(int(number))

while number != "":
    number = (input("Please input a number "))
    if number != "":
        list.append(int(number))

list = [i for i in list if i % 2 == 0]

print(list)
