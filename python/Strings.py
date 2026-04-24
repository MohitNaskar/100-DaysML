#ordered immutable datatype
my_string = "Hello World"

print(my_string)

#accessing elements using indexing negative indexing is also possible 
my_string[3]

# slicing in the string 
my_string[0:5] # mention the end value or runs till the end and if we dont mention the start value it starts from the beginin g

#concatinate two sting 
name = "tom"
new_string = name + my_string

print(new_string)

#iterate through the string 
for x in my_string:
    print(x)

#check for a letter in the string
if "p" in my_string:
    print("true")



#striping of white spaces
my_new_string = "      hello     "
my_new_string.strip()

#converting everything to upper case
my_string.upper()

#converting everything to lower string
my_string.lower()

#checking if the string start with a particular string
my_string.startswith("Hello")
my_string.endswith("World")

stringX = "hello"
print(stringX.capitalize()) #capitalizes the first letter of the string

# find replace count

my_string.find("World")
my_string.replace("World","Universe")   

#splitting the string
my_string.split(" ")

#count
my_string.count("l")

#reversing the string
my_string[::-1]
#string[start : end : step]


#check for substring 
my_string.find("he")

#count a specific char in the string
my_string.count("o")

#replacing a word with new word
my_string.replace("World","Universe")

