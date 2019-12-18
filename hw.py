z={}
for i in range(1,10):
    a = []
    b=i
    while b!=1:
        if b%2==0:
            b=b//2
            a.append(b)
        else:
            b=3*b+1
            a.append(b)
    print(a)
    z.update({i:len(a)})
abb=max(z.values())
for i,j in z.items():
    if j==max(z.values()):
        print('magic no. is:',i,'and length is:',j)