li = [5,5,5,5,5,5,5,5,5,5]

i = 0
sum1 = 0
sum2 = 0
while i <= (len(li)//2) -1:
    sum1 += li[i]
    sum2 += li[len(li)-1]
    i+=1
if sum1 == sum2:
    print(sum1)
    print("Some is Equal!!")
else:
    print("Sum is not Equal!!")

