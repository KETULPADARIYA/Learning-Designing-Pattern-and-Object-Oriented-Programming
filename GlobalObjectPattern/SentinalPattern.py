def function(data= []):
    data.append(1)
    print(data)
    return data

function() # [1]
function() #[1, 1]
function() #[1, 1, 1]
function() #[1, 1, 1, 1]


# for this
def function(data = None):
    if data is None:
        data = []
    data.append(1)
    print(data)
    return data

function() # [1]
function() # [1]
function() # [1]
function() # [1]

# also we can use sentinel
sentinel = object
def function(data = object):
    if data is object:
        data = []
    data.append(1)
    print(data)
    return data

function() # [1]
function() # [1]
function() # [1]
function() # [1]

# some test Every case is False
a = ''
print(a is None)
print(a is object)
print(type(a))

print(0 is None)
print(0 is object)
print(type(0))

print(None is object)

print(a == None)
print(a == object)
print(type(a))

print(0 == None)
print(0 == object)
print(type(0))

print(None == object)



