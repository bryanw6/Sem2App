num = int(input("Please input the number you'd like to check "))

def prime_check():
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break

        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")

prime_check()