#import math
class Calc():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def display(self):
        return ((self.x1+self.y1),(self.x2+self.y2))
        #return  math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
obj=Calc(2,3,3,4)
print(obj.display())