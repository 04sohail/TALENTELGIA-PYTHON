# Python Program for factorial of a number
n = int(input("Enter Number To Find The Factorial : "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of {} = {}".format(n, fact))
