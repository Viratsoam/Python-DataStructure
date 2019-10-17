def checkRecursion(n):
    if n == 0 and n == 1:
        return 1
    return (n*checkRecursion(n-1))

n = 1000
print(checkRecursion(n))