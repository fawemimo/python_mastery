course = "Python Programming"
length = len(course)

print(length)
# to acces the strings
# print(course[0])
# print(course[-1])
# to slice the string
# print(course[0:3])
print(course[:-3])

# Escape sequences
# CONCANTENATION
first = "Mosh"
last = "Adams"

full = F"{first} {last}"
print(full)

# STRING METHODS
print(course.strip()) # it removes the white space from the bginning of the string and the end of the string

#  to get the index of characters in the string
print(course.find('Pro'))

print(course.replace('p', 'j')) # to replace the characters in the string

print('Pro' in course) # to check the existence of characters in the string and it returns boolean
