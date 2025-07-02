# collection : Counter,named tuple,orderedDict,defaultdict,deque
#Counter is a subclass of dict that is specifically designed for counting hashable objects.


from collections import Counter
a = "aaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter.values())
print(my_counter.keys())

#most common elements in the list
print(my_counter.most_common())

#printing only the most common
#use indexing and play around
print(my_counter.most_common(1)[0][0])

#printing it as a list
print(list(my_counter.elements()))

from collections import namedtuple
point = namedtuple("point",'x,y')
pt = point(1,-4)
print(pt.x,pt.y)


from collections import OrderedDict
order_dict = OrderedDict()
order_dict['a'] = 1
order_dict['b'] = 2
order_dict['c'] = 3
print(order_dict)

from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
d.appendleft(4)

d.rotate(-1)