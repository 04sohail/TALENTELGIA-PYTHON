# Maximum of two numbers in Python
n1 = float(input("Enter First Number : "))
n2 = float(input("Enter Second Number : "))
res = n1 if n1 > n2 else n2
print("Greatest among {} and {} is {}".format(n1, n2, res))