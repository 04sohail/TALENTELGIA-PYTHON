# 1
# AB
# 123
# ABCD
# 12345

n = 1
r = 2
nl = 5
for i in range(1, nl):
    a = 65
    for i in range(1, n+1):
        print(i, end="")
    print("")
    for i in range(1, r+1):
        print(chr(a), end="")
        a+=1
    print("")
    n+=2
    r+=2