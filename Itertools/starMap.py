import itertools
# use to put extreme constant value through map or zip

squares = map(pow,range(10),itertools.repeat(2))
print(list(squares))

squares = itertools.starmap(pow,[(0,2),(1,2),(2,2)])
print(list(squares))
