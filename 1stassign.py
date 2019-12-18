# x=int(input("enter the digit:"))
# a=0
# b=1
# count1=0
# print(a,end=' ')
# print(b,end=' ')
# for i in range(2,x):
#     count1=a+b
#     print(count1,end=' ')
#     a,b=b,a+b

def gen():
    a=0
    yield a
    b=1
    yield b

    for i in range(8):
        yield a+b
        a,b=b,a+b

a=gen()
for i in range(10):
    print(next(a),end=' ')