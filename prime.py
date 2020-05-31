def check_prime(n):
    i = 2
    while i**2 <= n:
        if n%i == 0:
            return (False)
        i += 1
    return (True)
