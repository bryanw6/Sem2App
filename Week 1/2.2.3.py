check_num = int(input("Please input the number up to which you'd like to check for prime numbers: "))

def prime_check(num):
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                return False
        return True
    return False

for num in range(2, check_num + 1):
    if prime_check(num):
        print(num, "is a prime number")
