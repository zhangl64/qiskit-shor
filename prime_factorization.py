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
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            j = n // i
            if is_prime(j):
                return i, j

# Example usage
n = 123456789
p1, p2 = factorize(n)
print(f"{n} = {p1} x {p2}")