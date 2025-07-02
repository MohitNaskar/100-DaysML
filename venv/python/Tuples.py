#immutable order cannot be changed 

mytuple =("max",28,"Boston")
print(mytuple)

#if we enter a single element with out a comma its not recognised as a tuple but as a string 
mytuple[1]  #accessing the element using indexes

#negative index is also possible 
mytuple[-1] #accessing the last element using negative index

#itering over the tuple
for i in mytuple:
    print(i)

#check if an element is in our tuple
if 28 in mytuple:
    print("yes")

#printing the length of the tuple
len(mytuple)

#count elements within the tuple
mytuple.count('o')

# type casting
list(mytuple)

#slicing with tuple 
a = (1,2,4,5,6,7,8)
print(a[1:4]) #slicing the tuple if we dont mention the starting value it sstarts from 0 and if we dont specify the ending value it runs till the end of the list



