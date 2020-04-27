"""
If  own application’s architecture is too deeply compromised for coders to easily pass the instance everywhere it’s
needed, they can always store the instance as a module global in one of their own modules for the use of the rest of
 their code.
"""

from datetime import datetime


class Random(object):

    def __init__(self):
        self.set_seed(datetime.now().microsecond%255 + 1)
    def set_seed(self,value):
        """ reset the state of generator to known value"""
        self.seed = value

    def random(self):


        self.seed,carry = divmod(self.seed,2) # returns division and modulus
        #ex, divmod(21,3) = (7,0)
        if carry:
            self.seed ^= 0xb8
        return self.seed




"""
Why :
1. some variable uses dynamically change structure like our example instance uses datetime 
which interacts with system pool.
2. Pseudo-random number generators : generate random number of sequences according to our seeds
    are an interesting case of a resource whose behavior can be even more desirable when
     shared. If you are the lone caller to an instance, you see its completely predictable repeating sequence of values.
      If instead you are sharing that instance with other code, the generator will appear to skip ahead in its sequence 
      unpredictably each time other callers have themselves called the generator.
3.Since most users of random, including several modules within the Standard Library, import it specifically to use its
     module-level calls, it is rare for the pre-built Random instance that powers them to languish unused.
    
"""
