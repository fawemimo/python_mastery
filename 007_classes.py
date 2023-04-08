# Class: is a blueprint for creating new objects 
# Object: is an instance of a class

# CONSTRUCTORS

class Point:
    def __init__(self,x, y): # this is called a constructor
        self.x = x
        self.y = y  # instance attributes

    @classmethod # is the way of extending the meta of a functions behaviour    
    def zero(cls): # when defining a class method we called it cls
        return cls(0,0)

    def draw(self):
        print(f'point ({self.x}, {self.y})')

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10,20)
other = Point(1,2)
combined = point + other
print(combined.x,combined.y)


# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):    
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self): 
#         return iter(self.__tags)       


# class Product:
#     def __init__(self, price):

#         self.price = price

#     @property
#     def get_price(self):
#         return self.__price    

#     @price.setter
#     def price(self, value):    
#         if value < 0 :
#             raise ValueError('Price cannot be negative')
#         self.__price = value

# product = Product(-50)    
# print(product.price)        

# inheritance 

class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print('Eat')

class Mammal(Animal):

    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print('Walk')


m = Mammal()
m.eat
print(m.age)
#

class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print('Append Called')    
        super().append(object)


list = TrackableList()
list.append('1')


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
