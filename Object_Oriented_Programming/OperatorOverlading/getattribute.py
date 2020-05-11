class empty:
    def __getattr__(self, item):
        if item == 'age':
            return  45

        else:
            raise  AttributeError

X = empty()
print(X.age)

class accesscontrol:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value
        else:
            raise  AttributeError

X =  accesscontrol()
X.age = 40
print(X.age)
print(X.name)