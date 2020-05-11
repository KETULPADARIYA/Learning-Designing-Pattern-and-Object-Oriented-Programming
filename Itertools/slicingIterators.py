import itertools

letters = list("abcd")
numbers = list(range(2))
names = ["Corey",'Nicole']

sliced = itertools.islice(range(10),5)

print(list(sliced))

sliced = itertools.islice(range(10),1,5)

print(list(sliced))

sliced = itertools.islice(range(10),1,5,2)

print(list(sliced))