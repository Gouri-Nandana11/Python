def coins(amount,coin,dn):
    print(amount,coin,dn)
    if amount==0:
        return 1
    if dn ==0:
        return 0
    if amount< coin[dn-1]:
        return(coins(amount,coin,dn-1))
    return(coins(amount-coin[dn-1],coin,dn)+coins(amount,coin,dn-1))
amount=int(input())
coin=list(map(int,input().split()))
print(coins(amount,coin,len(coin)))

    
    
