import itertools

from Itertools.helper import fancy_print

letters = list("abcd")
numbers = list(range(2))
names = ["Corey",'Nicole']

fancy_print("Product")
result = itertools.product(numbers,repeat=3)

for result in result:
    print(list(result))

print(list(itertools.combinations(numbers,2)))

fancy_print("Combinations With Replacement")
print((list(itertools.combinations_with_replacement(numbers,3))))