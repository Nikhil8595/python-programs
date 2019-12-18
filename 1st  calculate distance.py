"""Write a program to calculate distance between two points
in the form of x and y coordinates,Display the calculated distance """

# import math
# def calc(x1,y1,x2,y2):
#     dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     return dist
# print(calc(2,4,6,8))
import math
class Calculate:
    def __init__(self,x1,y1):
        self.x1 = x1
        self.y1 = y1
    def add(self):
        return self.x1+self.y1
    def shortDistance(self,p,q):
        return math.sqrt((self.p)**2+(self.q)**2)

obj=Calculate(3,4)
# print(obj.shortDistance())
obj2=Calculate(4,5)
o3=Calculate(6,6)
# print(obj.x1+obj2.x1, obj.y1+obj2.y1)
print(Calculate.shortDistance(abs(obj.x1-obj2.x1), abs(obj.y1-obj2.y1)))
print(shortDistance(abs(o3.x1-obj2.x1), abs(o3.y1-obj2.y1)))
#
#
# # print(obj.display())
