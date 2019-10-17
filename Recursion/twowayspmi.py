def oneway(n):
    if n == 0:
        return
    print(n)
    oneway(n-1)
    # print()
    print(n)

oneway(9)