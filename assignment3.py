"""Create a list containing reminder of each element from 1 to 1000,
when divided by 7 without duplicate using comperhesion"""


l1=list()
n=int()
for each in range(0,1000):
    l1.append(each%7)
#print((l1))

set={each%7 for each in range(0,1000) }
print(set)
"""
l1=[]
[l1.append(each%7) for each in range(1000) if each%7 in l1]
print(l1)
"""