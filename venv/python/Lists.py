myList = ["banana","cherry","apple"]
print(myList)

item = myList[0] #indexing the list
print(item)

# negative indexing 
item1 = myList[-1] # the last element in the list 
print(item1)

# iterating the list 
for item in myList:
    print(item)
    if item == "Banana": #checking if a specific element is in the list 
        break

print(len(myList)) # specifies the lenth of the list 

#using the append function to add an element to the list at the end 
myList.append("grape")
print(myList)
#inserting an element into a particular position in the array 

myList.insert(1,"mango")
print(myList)

# removing the last element from the array we use pop method 
myList.pop()

#removing a specific element from the list 
myList.remove("cherry")

#remove all elements using the clear method
myList.clear()

#resersing the list 
myList.reverse()

#sorting the list 
a = [1,34,6,14,32]
a.sort() #its a inplace sort method and it also makes the changes in the original array 


#slicing the list 

print(a[1:4]) #starts from the index 1 and runs till 3 index and if we dont mention the starting value it sstarts from 0 and if we dont specify the ending value it runs till the end of the list

#coping the list 

copy = myList #this is how you copy the list but if you make any changes in the main list the copy also changes because it points to the same reference in the memory 

copy = myList.copy() #this is how you copy the list and if you make any changes in