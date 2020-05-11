from itertools import zip_longest


data = list(range(5))

longer_data = list(range(8))

print(list(zip_longest(longer_data,data)))