#Program for a Number and  Deciding whether It is Prime or Not
#BreakStmtEx5.py
n=int(input("Enter a Number for Deciding whether It is Prime or Not:")) # n=5
if(n<=1):
    print("{} Invalid input".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOT PRIME"
            break
    print("{} is {}".format(n,res))
