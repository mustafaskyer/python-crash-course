"""
Create a function called square that takes in a number and returns the square of that number. If what's passed in is not a float or an int, return None
"""

def square(num):
    if type(num) == int or type(num) == float:
        return num ** 2
    else:
        return None