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

# Example usage
n = 15
factors = factorize(n)
if factors is not None:
    p1, p2 = factors
    print(f"{n} = {p1} x {p2}")
else:
    print(f"{n} cannot be factorized into two prime numbers.")