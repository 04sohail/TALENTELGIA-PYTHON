def isPrime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False
    return True


def primes(lst):
    primeslst = []
    for i in lst:
        if isPrime(i):
            primeslst.append(i)
    return primeslst


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = primes(lst)
print(primes)
