def isPrime(num):
    if num<=1:
        return False
    for n in range(2, int(num **0.5) + 1):
        if num % n == 0:
            return False
    return True


def rangeOfPrime(arr):
    primes = []
    for i in arr:
        if isPrime(i):
            primes.append(i)
    return primes

lst = [int(i) for i in input("Enter Numbers With Spaces Between Them : ").split(" ")]
primes = rangeOfPrime(lst)
print(primes)
