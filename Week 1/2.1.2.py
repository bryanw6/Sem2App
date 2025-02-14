def sum(a,b):
    return a + b 

def sub(a,b):
    return a - b 

def multi(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error. Division by zero."


def sum3(a,b,c):
    return a + b + c

def sub3(a,b,c):
    return a - b - c

def multi3(a,b,c):
    return a * b * c

def divide3(a,b,c):
    if b != 0 and c != 0:
        return a / b / c
    else:
        return "Error. Division by zero."



value = int(input("Do you want 2 or 3 values? "))

if value == 2:
    a = int(input("What is #1? "))
    b = int(input("What is #2? "))
    operator = input("Choose an operator from sum, sub, multi, divide ")
    if operator == "sum":
        result = sum(a,b)
    elif operator == "sub":
        result = sub(a,b)
    elif operator == "multi":
        result = multi(a,b)
    elif operator == "divide":
        result = multi(a,b)
    else: 
        result = "Something went wrong. Please make sure you choose a correct operator"
    print(result)


elif value == 3:
    a = int(input("What is #1? "))
    b = int(input("What is #2? "))
    c = int(input("What is #3? "))
    operator = input("Choose an operator from sum, sub, multi, divide ")

    if operator == "sum":
        result = sum3(a,b,c)

    elif operator == "sub":
        result = sub3(a,b,c)

    elif operator == "multi":
        result = multi3(a,b,c)

    elif operator == "divide":
        if b != 0:
            result = divide3(a,b,c)
        else:
            print("Error. Division by zero.")
    else:
        print("Something went wrong, please make sure you choose a correct operator")
    print(result)

else:
    print("Something went wrong. Please make sure you pick a value that's either 2 or 3")

 