#unordered mutable but cannot have duplicate elements
myset ={1,2,3,4,5}
print(type(myset))

#adding elements to the set
myset.add(6)

#removing elements from the set
myset.remove(2)

#if a element isn't there while using remove it gives key error
#pop discard are also some methods to remove it 

#iterate through the set
for i in myset:
    print(i)

#check if element is there in the set
if 2 in myset:
    print("yes")

odds = {1,3,5,7,9}
even ={2,4,6,8}

primes ={2,3,5,7}

#finding the union
u = odds.union(even)

#calculating the intersection of two sets

i = odds.intersection(primes)

#difference of two set gives on elements that are not present in the first set

result = odds.difference(primes)

result1= odds.symmetric_difference(primes) #provides the unique elements in both the sets


#update can be paired with all the basic math methods 

odds.update(even)
print(odds) #it will add all the elements of even set to the odds set

print(odds.issubset(even)) #elements of odds are subset of element b 

print(odds.issuperset(even)) # is the set odd superset of even or odd contains all the elements from even

print(odds.isdisjoint(even)) #returns true if no same elements


#coping two sets #coping the reference 
resultx = odds
print(resultx)


#using coping methods
resultx = odds.copy() #recommendede


