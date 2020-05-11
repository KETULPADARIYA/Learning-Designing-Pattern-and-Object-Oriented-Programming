class Square:
    def __init__(self,start,stop):
        self.value = start -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

print("square")
for i in Square(1,5):
    print(i,end= ' ')
x = Square(1,5)
while True:
    print(next(x))