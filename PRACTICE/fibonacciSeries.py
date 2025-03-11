def findFibonacci(num):
    fib = [0, 1]
    if num == 0:
        return 0
    elif num == 1:
        return [0]
    elif num == 2:
        return fib
    for _ in range(2, num):
        fib.append(fib[-1]+fib[-2])
    return fib

num = int(input("Enter How Much Number Your Want : "))
fib = findFibonacci(num)
print(fib)
