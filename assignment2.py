"""find the numbers divisible by 3 and 9 using comperhension"""

l1=list()
list1=[each for each in range(0,1000) if each % 3==0 if each %9==0]
#list2=[each for each in range(9,1000) if each  %9==0]
print(list1)
#print(list2)

"""for each in range(3,1000):
    if each % 3==0 and each%9==0:
        l1.append(each)
        print(each,end=' ')"""