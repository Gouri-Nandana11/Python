def isPrime(i):
    if i <= 1:
        return False
    for j in range(3, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

n = int(input())
c=0
for i in range(3,n):
    if isPrime(i):
          c+=1
print(c)