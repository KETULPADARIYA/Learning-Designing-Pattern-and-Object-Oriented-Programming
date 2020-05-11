import itertools

cycle = itertools.cycle([1,2,3])

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))


cycle = itertools.cycle(('On','Off'))

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
