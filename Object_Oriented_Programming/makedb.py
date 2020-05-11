from Object_Oriented_Programming.person import Person,Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones',job= 'dev',pay=100000)
tom = Manager('Tom Jones',pay=50000)

import shelve
db = shelve.open('persondb')
for object in [bob,sue,tom]:
    db[object.name] = object

db.close()

print(open('persondb').read())