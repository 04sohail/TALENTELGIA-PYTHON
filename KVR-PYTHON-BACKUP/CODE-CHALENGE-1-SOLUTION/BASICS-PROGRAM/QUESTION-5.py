# Python Program for compound interest
p = float(input("Enter principle : "))
r = float(input("Enter Rate Of On Interest : "))
t = float(input("Enter Time : "))
a = p*(pow(1+r/100, t))
ci = a - p
print("Compound Interest = ", ci)
