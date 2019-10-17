import sys as s
s.setrecursionlimit(3000)

def depth(n):
    if n == 0 or n == 1:
        return 1
    return n * depth(n-1)

print(depth(1000))