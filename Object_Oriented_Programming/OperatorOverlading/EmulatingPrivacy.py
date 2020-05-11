class PrivateExc(Exception): a = "This is Private Field :"

class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateExc
        else:
            self.__dict__[key] = value


class test1(Privacy):
    privates= ['age']

class test2(Privacy):
    privates = ['name','pay']
    def __init__(self):
        self.__dict__['name'] ="Tom"


x  = test1()
y = test2()

try :
    y.age = 20
    x.age = 30
except PrivateExc as e:
    print(e.a,"a")
try :
    x.name = "Bob"
    y.name = "Marli"
except PrivateExc as e:
    print(e.a,"b")


