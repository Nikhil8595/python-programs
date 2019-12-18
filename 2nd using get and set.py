"""Calculate area using Get and Set method"""

class Calc():

    def __set__(self,a,b):
        self.a = a
        self.b = b

    def __get__(self):
        print ("Calculated Area:",self.a *self.b)

obj=Calc()

obj.__set__(20,34)
obj.__get__()