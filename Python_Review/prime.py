def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number to check if it is prime: "))
print(is_prime(n)) 

