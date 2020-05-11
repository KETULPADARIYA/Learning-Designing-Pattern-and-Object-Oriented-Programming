import itertools
# use to put extreme constant value through map or zip

squares = map(pow,range(10),itertools.repeat(2))
print(list(squares))


repeater = itertools.repeat([12,34,56],times=3)

print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
print(next(repeater))
#
