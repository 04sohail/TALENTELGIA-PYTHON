# Python Program for n-th Fibonacci number
n = int(input("Enter Number : "))
lst = [0, 1]
a = 0
b = 1
while len(lst) != n:
    nxtn = a + b
    lst.append(nxtn)
    a, b = b, nxtn

print("{}th fibonacci num = {}".format(n, lst[-1]))