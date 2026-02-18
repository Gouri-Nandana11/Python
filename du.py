inp=input("enter the string:")
count=0
alt=0
for i in inp:
    if i =="u":
        alt +=1
    elif i =="d":
        alt-=1
    if alt ==0 and i =="u":
        count +=1
print(count)
