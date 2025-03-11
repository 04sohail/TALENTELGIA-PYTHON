# Python program to check whether a number is Prime or not
def isprime(n):
    if n < 2:
        return "Not A Prime"
    else:
        for i in range(2, n//2):
            if n % i == 0:
                return "Not A Prime"
        return "Prime"


n = int(input("Enter Number : "))
print("{} is {}".format(n, isprime(n)))
