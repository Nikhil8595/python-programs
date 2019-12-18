class Account(object):   #"""single"""
    pass
class user(object):
    pass

class user(Account):      #"""multilevel"""
    a=12
    def func(self):#self is keyword it automatically gets passed
        print(a)

a=user()
b=list()

a.func()

class user():
    pass
