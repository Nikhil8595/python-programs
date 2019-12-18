"""Take two list of diffrent length,find out the common elelment between
them with and without duplicate"""

l1=[1,2,3,4,5,6,7,8,11]
l2=[2,3,6,7,8,0,8,7,2,6,9,6,4,11]
l3=[]
count=0

for i in l1:
    for j in l2:
        if j==i:
            l3.append(j)
print(set(l3))

set1={j for i in l1 for j in l2 if i==j}
print(set1)
