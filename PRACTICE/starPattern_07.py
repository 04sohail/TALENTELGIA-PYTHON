# 1234
# 123
# 12
# 1

nl = int(input("Enter Number Of Lines : "))
n = nl
for i in range(1, nl + 1):
    for j in range(1, n+1):
        print(j, end="")
    n-=1
    print("")