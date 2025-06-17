mydict = {"Name":"Max","Age":28,"City":"New York"}
print(mydict)

value = mydict["Age"] # the value of age gets stored in the value variable

#it is mutable and if you want to access some key which is not present it will give keyvalue pair 

mydict["email"] ="mohitnaskar02@gmail.com" #adding a key to a dictionary 

print(mydict)

# mydict.pop() #removes an arbitary element from the dictoionary 

#iterating through the dictionary 
for key,value in mydict.items():
    print(key, value)

#coping a dictonary 
mydict2 = mydict.copy() #copying a dictionary
print(mydict2)

mydict.update(mydict2)
print(mydict)