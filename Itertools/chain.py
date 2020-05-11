"""

when we have millions of data of rows table we want to merge two or three set
if we use the list combination then we are doing inefficient way
"""
import itertools


letters = list("abcd")
numbers = list(range(2))
names = ["Corey",'Nicole']

itertool_fun =  itertools.chain(letters,numbers,names)

for i in itertool_fun:
    print(i)