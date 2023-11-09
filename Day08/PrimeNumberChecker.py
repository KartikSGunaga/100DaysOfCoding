num = int(input("Enter the number: "))

def isPrime(num):
    if num < 2:
        return False  # Numbers less than 2 are not prime
    for i in range(2, num):
        if num % i == 0:
            return False  # If it's divisible by any number in the range, it's not prime
    return True

if isPrime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
