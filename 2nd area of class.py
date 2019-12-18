"""Calculate area"""

class Area_of():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):
        return (self.a * self.b)
obj=Area_of(10,2)
print("Calculated Area:",obj.display())