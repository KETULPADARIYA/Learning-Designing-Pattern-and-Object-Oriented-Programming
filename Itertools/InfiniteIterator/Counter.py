import itertools

counter = itertools.count()

data = [100,200,300,400]

daily_data = list(zip(itertools.count(),data))

print(daily_data)

print(next(counter))
print(next(counter))

#different strat and step
counter = itertools.count(5,2.45)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

