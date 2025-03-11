# starPattern_08.py

# A B C D
# A B C
# A B
# A

nl = int(input("Enter Number Of Lines : "))
n = nl
for i in range(1, nl + 1):
    a = 65
    for j in range(1, n+1):
        print(chr(a), end="")
        a+=1
    print("")
    n-=1