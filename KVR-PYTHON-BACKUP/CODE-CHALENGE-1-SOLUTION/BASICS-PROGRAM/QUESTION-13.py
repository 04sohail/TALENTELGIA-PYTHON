# Python Program for Sum of squares of first n natural numbers
n = int(input("Enter Number : "))
lst = [val**2 for val in range(1, n + 1)]
print("Sum of First {} natural numbers = {}".format(n, sum(lst)))
