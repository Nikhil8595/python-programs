import string
import random
a=string.ascii_lowercase
b=string.ascii_uppercase
c=string.punctuation
d=string.digits
z=a+b+c+d
x=[]
a1=random.choice(a)
b1=random.choice(b)
c1=random.choice(c)
d1=random.choice(d)

x.append(a1)
x.append(b1)
x.append(c1)
x.append(d1)
#x.extend(random.choices(z,k=4))
for i in range(4):
    x.append(random.choice(z))


random.shuffle(x)
print(''.join(x))
