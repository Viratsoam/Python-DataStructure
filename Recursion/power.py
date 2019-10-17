def power(n,pow):
    if pow == 0:
        return 1
    return n*(power(n,pow-1))

n = int(input("Enter the Number!!"))
pow = int(input("Ente the power!!"))
print(power(n,pow))
