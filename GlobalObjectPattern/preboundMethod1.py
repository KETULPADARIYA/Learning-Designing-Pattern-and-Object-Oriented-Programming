from datetime import datetime

_seed = datetime.now().microsecond%255 + 1
print(_seed)
def set_seed(value):
    ''' reset the state of generator to known value'''
    global _seed
    _seed = value

def random():
    global  _seed
    _seed,carry = divmod(_seed,2) # returns division and modulus
    #ex, divmod(21,3) = (7,0)
    if carry:
        _seed ^= 0xb8
    return _seed

"""
    PROBLEM 1 :
            we never get copy of the set_seed value. copy is need when 
    we are using the threading.
    
    PROBLEM 2 :
        it difficult to decouple the random number generator test if
    we are using global object in each function. To debug or write test
    we have to use different random generator for each function.

    PROBLEM 3 :
        Difficult to Refactor it.
"""