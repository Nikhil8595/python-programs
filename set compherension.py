a={2:'a',3:'c',4:'asa'}
b=iter(a.keys())
c=iter(a.values())
#print(b[1])
print(b.__next__())
print(c.__next__())
print(next(b))