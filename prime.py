N=int(input())
isPrime =[True]*(N+1)
isPrime[0]=isPrime[1]=False
primes =[2]
for i in range(3,N+1,2):
    if isPrime[i]:
        primes.append(i)
        for j in range(i,N+1,i):
            isPrime[j]=False
print(primes)