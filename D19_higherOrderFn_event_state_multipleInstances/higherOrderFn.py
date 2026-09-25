# A Higher-Order Function (HOF) is a function that does at least one of the following:

# Takes one or more functions as arguments.

# Returns a function as its result.

# In Python, this is possible because functions are first-class citizens—they can be passed around, stored in variables, and manipulated just like integers, strings, or lists.

# 1. Passing a Function as an Argument
# You pass a function name (without parentheses ()) to another function, which then calls it internally.


def add(n1,n2):
  return n1+n2

def subs(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def devide(n1,n2):
  return n1/n2

def calculator(n1,n2,function):
  return function(n1,n2)

result=calculator(1,2,subs)
print(result)