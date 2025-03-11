#Program for Demonstrating global Key word
#GlobalKwdEx3.py
def  incr():
	global a,b
	a=a+1
	b=b+1

def modify():
	global a,b
	a=a*10
	b=b*10

def  update():
	global a
	a=a*2
	c=b-10 # we Need Not to write global b bcoz we are just accessing global variable 'b'
	print("\tLocal Var Val of c in update()={}".format(c))

#Main Program
a,b=10,20 # Here 'a' and 'b' are called Global Variables
print("Main Prog: a={} and b={} before incr()".format(a,b)) # 10 20
incr() # Function Call
print("Main Prog: a={} and b={} after incr()".format(a,b)) # 11   21
modify()
print("Main Prog: a={} and b={} after modify()".format(a,b)) # 110  210
update()
print("Main Prog: a={} and b={} after update()".format(a,b)) # 220  210
