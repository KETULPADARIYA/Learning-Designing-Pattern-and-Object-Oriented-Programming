import itertools

# combination where order does not matter :('a','b') == ("b","a")
# Permutation where order matters:('a','b') != ("b","a")
from Itertools.helper import fancy_print

letters = list("abcd")
numbers = list(range(4))
names = ["Corey",'Nicole']


# get combinations of two items
result = itertools.combinations(letters,2)

fancy_print("Combinations")
for item in result:
    print(item)

fancy_print("Permutations")

result = itertools.permutations(letters,2)
for item in result:
    print(item)
