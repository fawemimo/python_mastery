letters = ['a','b','c','d']
letters[0] = 'A'
print(letters[::2]) # skip two steps ahead

print(letters[::-1]) # it returns the list in the reverse pattern

# unpacking list
numbers = [1,2,3,4,5,6,7]

first, second, *others, last = numbers # unpacking list
print(first)
print(others)
print(last)


# iterating over the list to get the index 
for index, letter in enumerate(letters): #enumerate returns tuple
    print(index, letter)

# ADD
letters.append('F') # TO ADD TO LIST AT THE END
letters.insert(2,'4') # TO ADD TO LIST AT THE EXACT POSITION
print(letters)

# REMOVE
letters.pop(0) # to remove from the list at the end also it takes the index of the list

letters.remove('b') # takes the values of what to remove from the list

del letters[0:2] # takes the range of the list to be deleted

letters.clear() # removes all the objects in a list


# FIND 
# letters.index('b') # to find the index

# SORTING
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=False) #
print(sorted(numbers))
print(numbers)

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 39)
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item) 
print(items)    

# STEP 2
prices = []
for item in items:
    prices.append(item[1])

# print(prices)

# STEP 2:
# x = map(lambda item: item[1], items)
# print(list(x))

# for item in x:
#     print(item)

# STEP 3:
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)


# LIST COMPREHENSIONS
# [expression for item in items]

# x = [item[1] for item in items]
# print(x)
f = [item for item in items if item[1] >= 10]
print(f)

# ZIP FUNCTION 
list1 = [1,2,3]
list2 = [10,20,30]

print(list(zip('abc',list1,list2)))


# QUEUE
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# TUPLE: we cannot add or remove items just like list

from array import array

numbers = array('i', [1,2,3]) # use array when dealing with large sequence of numbers and encounter large performance problems
print(numbers)

# SET: it returns duplicates, unorder collections of unique items
numbers = [1,1,1,2,3,4,6,7,7]
numbers = set(numbers)
print(numbers)

# UNION SET 
second = {1,5}

print(numbers | second)

# INTERSECTION SET
print(numbers & second)

# DIFFERENT SET
print(numbers - second)

# DIFFERENT SET
print(numbers ^ second)#

# DICTIONARIES
point = dict(x=1, y=2)
print(point)


# values = []
# for x in range(5):
#     values.append( x * 2)
#     print(values)

values = {}
for x in range(5):
    values[x] = x * 2


values = { x *2 for x in range(5) }
print(values)

# GENERATOR OBJECT: are iterables
values = (x*2 for x in range(10))

for x in values:
    print(x)

from sys import getsizeof
values = (x * 2 for x in range(100000))
print('gen: ', getsizeof(values))
values = [x * 2 for x in range(100000)]
print('list: ', getsizeof(values))

# UNPACKING OPERATOR: we can use the unpacking operator to take out any values in any iterable
first = {'x':1}
second = {'x':10, 'y':20}
combined = {**first, **second, 'z':20}  
print(combined)


from pprint import pprint
sentence = 'This is a common interview'

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency, width=1)            
char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True)


print(char_frequency_sorted[0])