import random
import string

a=string.ascii_lowercase
b=string.ascii_uppercase
c=string.punctuation
d=string.digits
z=a+b+c+d
print(z)
passlen = 8

z1="".join(random.sample(z,passlen))
print(z1)