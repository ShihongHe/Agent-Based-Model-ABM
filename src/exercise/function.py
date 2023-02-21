# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:08:21 2023

@author: He
"""
def add(num1, num2):
    return num1 + num2
print(add(20,30)) # Prints 50

def add(num1 = 0, num2 = 0):
    print(num1,num2)
    return num1 + num2
print(add(3)) # Prints 3

#def add(num1 = 0, num2):
#    return num1 + num2
#print(add(3))

def add(num1, num2):
    return num1 + num2
print(add(num2 = 30, num1 = 50))

def add(*nums):
    r = 0
    for num in nums:
        r += num
    return r
print(add(1,2,3,4,5,6,7)) # Prints 28

def add(*nums):
    r = 0
    for num in nums:
        r += num
    return r
a = [1,2,3,4]
print(add(*a)) # Prints 10
print(add(1,*a, 2)) # Prints 13

def f1(a, **details):
    print(a)
    print(details)

f1(1, b=2, c=3)

def f1(a, b, c):
    print(a)
    print(b)
    print(c)

d = {'b':2, 'c':3}
f1(1,**d)


def f1(a, b=2, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

l = [10, 20, 30]
d = {'c': 100, 'd': 200}

f1(1, 3, *l, **d)

a = 10
def f1():
    print(a) # Prints 10;
print(a) # Prints 10.
f1()
print(a) # Prints 10.

a = 10
def f1():
    global a
    a = 20
    print(a) # Prints 20.
print(a) # Prints 10.
f1()
print(a) # Prints 20 as the function changes the global a.


a = 1
def f1():
    a = 2
    def f2():
        nonlocal a
        a = 3
        print(a) # Prints 3.
    f2()
    print (a) # Prints 3.
f1()
print(a) # Prints 1.


import random
import time

def timer(func):
    """
    Get the run time of the decorated function.

    Parameters
    ----------
    func : The function to be timed.
        DESCRIPTION.

    Returns
    -------
    Tuple
        The run time then func output.
    """
    def inner_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        run_time = time.perf_counter() - start
        return run_time, value
    return inner_timer


@timer#creat_agents=timer(creat_agents)
def create_agents(n_agents):
    """
    A function to create a list of agents. The decorator will print the time
    it takes to run this function.

    Parameters
    ----------
    n_agents : Integer
        The number of agents to create.

    Returns
    -------
    agents : List
        A list of the created agents.

    """
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    return agents

# Create agents
n_agents = 1000000
run_time, agents = create_agents(n_agents)
print(run_time, "seconds to create", n_agents, "agents.")

# A lamda to return the result of dividing a by b.
x = lambda a, b : a / b

print(x(1, 2)) # <-- Prints 0.5.

def add(x):
    """
    Calculate and return all the elements of x added together.

    Parameters
    ----------
    x : Tuple
        The things to add.

    Returns
    -------
    r : Things added.
        All the things in x added together.

    """
    r = 0
    for y in x:
        r = r + y
    return r

def multiply(x):
    """
    Calculate and return all the elements of x multplied together.

    Parameters
    ----------
    x : Tuple
        The things to multiply.

    Returns
    -------
    r : Things multiplied.
        All the things in x multiplied together.

    """
    r = 1
    for y in x:
        r =r* y
    return r

def caller(func, args):
    """
    A function that calls the function func passing in the
    arguments args.

    Parameters
    ----------
    func : Function
        The (name of the) function to be called.
    args : Tuple
        The arguments to be passed to func
    Returns
    -------
    Whatever is returned from func(args)
    """
    return func(args)

print(caller(add, (1, 2, 3))) # Prints 6
print(caller(multiply, (1, 2, 3, 4, 5, 6))) # Prints 720

class Mark:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return "name=" + self.name + " grade=" + str(self.grade)

def getGrade(mark):
    return mark.grade

marks = [Mark("name1", 50), Mark("name2", 70), Mark("name3", 60)]
print("Unordered marks:")
for mark in marks:
    print(mark)

# Sort marks using a callback
marks.sort(key=getGrade)
print("Ordered marks:")
for mark in marks:
    print(mark)

from functools import partial

def f(x, y, z):
    return x + y + z

# A partial function that calls f with x = 1 and y = 2.
pf = partial(f, 1, 2)

print(pf(3)) # Prints 6























