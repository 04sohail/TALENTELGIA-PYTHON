# Python program to print all Prime numbers in an Interval
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


s = int(input("Enter starting : "))
e = int(input("Enter ending : "))

lst = [val for val in range(s, e + 1) if is_prime(val)]
print(lst)