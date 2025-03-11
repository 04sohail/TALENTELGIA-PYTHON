# 1
# 12
# 123
# 1234

n = 1
nl = int(input("Enter Number Of Lines :"))
for i in range(1, nl+1):
    for j in range(1, n+1):
        print(j, end="")
    print("")
    n+=1
    