def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    """Factorize an integer into two prime numbers."""
    if is_prime(n):
        return n, 1
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            j = n // i
            if is_prime(j):
                return i, j
    return None

# Ask the user for input instead of hard-coding
try:
    n = int(input("Enter an integer to factorize: "))
except ValueError:
    print("Please enter a valid integer.")
    exit(1)
if is_prime(n) == True:
    print(f"{n} is a prime number and cannot be factorized.")
    exit(1)    
factors = factorize(n)
if factors is not None:
    p1, p2 = factors
    print(f"{n} = {p1} x {p2}")
else:
    print(f"{n} cannot be factorized into two prime numbers.")