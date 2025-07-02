# one line anonymous function 
#lambda arguments : expression

add10 = lambda x:x+10

print(add10(5))

#multiargument lambda function
mult = lambda x,y : x*y
print(mult(5,6))

points2D_sorted = [(1,3),(15,1),(5,-1),(10,4)]

points2D = sorted(points2D_sorted,key = lambda x:x[0] + x[1])

a = [1,2,3,4,5]
b = map(lambda x : x*2,a)

print(list(b))