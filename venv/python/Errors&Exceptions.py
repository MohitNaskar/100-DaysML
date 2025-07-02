#errors and expections 
#syntax error is the error which takes place when we make structural errors or 
#when we write the code in a wrong way

#type error comes when we try to use unequal data types which each other

#raising an exception

# x = -5
# if x < 0:
#     raise Exception("x should be positive")

#try block
# try:
#     #code that might raise an exception
#     x = 5
#     y = 0
#     z = x / y
# except Exception as e:
#     print("can't devide by 0")
#     print(e)
# finally:
#     print("cleaning")


#user defined expception
class ValueTooHighError(Exception):
    """Raised when the input value is too high"""
    print("lol")

def test(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    else:
        return x

try:
    test(200)
except ValueTooHighError as e:
    print(e)  # prints: Value is too high
finally:
    print("cleaning")  # prints: cleaning

    