# Python Program to check Armstrong Number
n = input("Enter Number : ")
lst = list(n)
a = 0
for i in lst:
    a = a + int(i)**3
if a == int(n):
    print("Armstrong")
else:
    print("Not An Armstrong")
