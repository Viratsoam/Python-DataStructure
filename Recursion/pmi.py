def pmi(n):
    if n == 0 or n == 1:
        return n
    return (n*(n+1))//2

n = int(input("Enter the number to find the sum of first natural numbers!!"))
print(pmi(n))
