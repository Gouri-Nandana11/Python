inp=input("eneter the string:")
count=0
for i in inp:
    if i =="{":
      count+=1
    elif i =="}":
      count-=1
    if count <0:
      break
if count ==0:
   print("matches")
else:
   print("not")
    
      