# itertools : product, permutation, combination, accumulate, groupby and unfinite iterators
from itertools import product
import re
#product of two list
a = [1,2]
b = [3,4]
prod = product(a,b)
# print(list(prod))

from itertools import permutations
#returns all posible ordering of a input 
a = [1,2,3]
permutation = permutations(a)
# print(list(permutation))

from itertools import combinations,combinations_with_replacement
#returns all posible combination of a input
a = [1,2,3,4]
comb = combinations(a,2) #provides list size of two
comb1 = combinations_with_replacement(a,2)
# print(list(comb))
# print(list(comb1))

from itertools import accumulate #gives the accumalted sum for the list
import operator#maxx,mul,div and all other arithmatic functions possible
acc = accumulate(a)
# print(list(acc))
# acc = accumulate(a,func=operator.mul)
# print(list(acc))


from itertools import groupby

def smaller_than_3(x):
    return x < 3
groupobj = groupby(a,key=smaller_than_3)
for key,value in groupobj:
    print(key,list(value))
    