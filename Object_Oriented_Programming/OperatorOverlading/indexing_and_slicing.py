class Indexer:
    # don't need instant constructor
    def __getitem__(self, item):
        return item ** 2

X = Indexer()
print("X[2]",X[2])

for i in range(5):
    print(f"X[{i}]",X[i],end=' ')
print()
#### SLice bounds
L = [5,6,7,8,9]
print(L[2:4])
print(L[slice(2,4)])
print(L[slice(1,None)])

################# class Indexer
class Indexer:
    data =list(range(12))
    def __getitem__(self, item):
        print("get_item \t",item)
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value


X = Indexer()
print(X[2])
print(X[2:])
print(X[:3])


###################
class stepper:
    def __getitem__(self, item):
        return self.data[item]

X = stepper()
X.data = 'spam'
print(X[2])
print([ i for i in X])
