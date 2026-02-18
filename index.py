n=10
q = [[1,5,5], [4,8,7], [6,9,1]]
A =[0]*n
for start,end,value in q:
    for i in range(start,end):
        A[i]+=value
        print(A)
print(max(A))


