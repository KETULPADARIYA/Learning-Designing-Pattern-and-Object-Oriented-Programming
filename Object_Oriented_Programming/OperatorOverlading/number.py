
class Number:
    def __init__(self,start):
        self.data = start

    def __sub__(self, other):
        if type(other) == Number:

            return Number(self.data - other.data)
        else:
            return Number(self.data - other)



if __name__ == '__main__':
    X = Number(2)
    Y = Number(3) - 4

    print(Y.data)
    X = Number(2)
    Y = Number(3) - Number(4)
    print(Y.data)

