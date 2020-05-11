class Prod:
    def __init__(self,value):
        self.value = value
    def __call__(self, *args):
        return sum(self.value*i for i in args)

prod2 = Prod(2)
print(prod2(2,34,4))

print(complex(1,2))