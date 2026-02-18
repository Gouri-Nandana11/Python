n=10
q = [[1,5,3], [4,8,7], [6,9,1]]
A =[0]*(n+1)
for start,end,value in q:
    A[start]+=value
    A[end+1]-=value

sum =0
res=0
for i in A:
    sum +=i
    res=max(res,sum)
print(res)