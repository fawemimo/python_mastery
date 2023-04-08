# Parameter is the input that you define for your functions

# An Argument is actual value for a given parameter

"""
We have two types of functions
1. Perform a task
2. Return a value
"""

# xtra argument
def multiply(*numbers):
    print(numbers)

multiply(3,4,5,6,7,5,4,3,3,3)    


def save_user(**users):
    print(users['name'])



save_user(name='Promise', age=22, courses='Python')


def fizz_buzz(input):
    if int(input) % 3 == 0:
        print('Fizz')
    if input % 5 ==0:
        print('Buzz')
    if input % 5 == 0 and input % 3 == 0:
        print('FizzBuzz')    
    
    return input

fizz_buzz(int(15))        