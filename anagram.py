str1=input("enter an input").split()
str2=input("enter 2nd").split()
if sorted(str1)== sorted(str2):
    print("true")
else:
    print("false")

#or
str1=input("enter an input").split()
str2=input("enter 2nd").split()
from collections import Counter
if Counter(str1)==Counter(str2):
     print("anagram")
else:
    print()
 