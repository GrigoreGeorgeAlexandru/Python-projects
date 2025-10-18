k = int(input("suma maxima: "))
x = int(input("numar: "))
sum=0
while x>=0:

    if k / 2 <= x <=k and x>sum:
        sum = x
        break
    if sum + x <= k:
        sum=sum+x
    x = int(input("numar: "))
print(sum)
