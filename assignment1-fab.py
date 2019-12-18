"""make fibonacci series by comprehension"""
n=int(input("enter the number :"))
l=[0,1]
print(l[-1])
print(l[-2])
list1=[l.append(l[-1]+l[-2]) for a in range(2,n)]
print(l)

"""without comprehension"""
"""n=(int(input("enter the digit:")))
n1=0
n2=1
for key in range(n):
    print(n1,end=' ')
    n1,n2=n2,n1+n2"""