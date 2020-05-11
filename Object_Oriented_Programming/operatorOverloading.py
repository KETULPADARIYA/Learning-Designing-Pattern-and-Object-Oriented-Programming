class A:
    def __init__(self,x):
        self.x = x

    def __add__(self, other):
        if type(other) in [ str,int]:
            return self.x + other
        return self.x+other.x

b = A(12)
c = A(33)
print(type(b))
print(b+12)