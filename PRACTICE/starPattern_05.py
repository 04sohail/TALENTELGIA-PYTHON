# ****
# ***
# **
# *

nl = int(input("Enter Number Of Lines : "))
nst = nl
for i in range(1, nl+1):
    for j in range(1, nst+1):
        print("*", end="")
    print("")   
    nst-=1
