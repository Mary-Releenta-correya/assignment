list=[45,73,105,7,54,80]
temp=[]
for n in list:
    sum=0
    for digit in str(n):
        sum=sum + int(digit)
    temp.append(sum)
print("sum of digits in",list,"is",str(temp))

