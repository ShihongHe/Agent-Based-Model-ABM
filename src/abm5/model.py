     # -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:17:22 2023

@author: He
"""
import math
import random
import time
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io
import csv





#random.seed(0)
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
    
def get_distance(x0,y0,x1,y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).

    """
    distance=math.sqrt((x0-x1)**2+(y0-y1)**2)
    return distance

def get_max_distance(agents):
    
    """
    Calculate the max distance

    Parameters
    ----------
    agents : list
        A list of stored coordinates

    Returns
    -------
    max_distance : number
        max distance

    """
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1,len(agents)):
            b = agents[j]
            distance = get_distance(a.x,a.y,b.x,b.y)
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
    return max_distance

def get_distance_list(agents):
    """
    Calculate the maximum distance to store in the list

    Parameters
    ----------
    agents : list
        A list of stored coordinates

    Returns
    -------
    distance : list
        Store a list of all distances between coordinates.

    """
    distance=[]
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1,len(agents)):
            b = agents[j]
            distance.append(get_distance(a.x,a.y, b.x, b.y))
    return distance
    

def get_arithmetic_mean(agents):
    """
    Calculate the arithmetic mean

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    mean : Number
        Calculate the mean of all coordinate distances.

    """
    distance=get_distance_list(agents)
    mean=sum(distance)/len(distance)
    return mean

def get_standard_deviation(agents):
    """
    Calculate the standard deviation

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    standard_deviation : Number
        Calculate the standard deviation of all coordinate distances.

    """
    deviations=0
    mean=get_arithmetic_mean(agents)
    distance=get_distance_list(agents)
    for i in distance:
        deviations+=(i-mean)**2
    standard_deviation=(deviations/len(distance))**0.5
    return standard_deviation

def get_median(agents):
    """
    Calculate the median

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    median : Number
        Calculate the median of all coordinate distances


    """
    distance_list=get_distance_list(agents)
    distance_list.sort()
    if len(distance_list)%2:
        median=distance_list[len(distance_list)//2+1]
        
    else:
        median=(distance_list[len(distance_list)//2]+distance_list[len(distance_list)//2]+1)/2
    return median

def get_mode(agents):
    """
    Calculate the mode

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    key : Number
        Number of mode for all coordinate distances.
    value : Number
        DThe value of the mode of all coordinate distances.

    """
    distance_list=get_distance_list(agents)
    distance_dic={}
    for i in distance_list:
        if i in distance_dic:
            distance_dic[i]+=1
        else:
            distance_dic[i]=1
    for key,value in distance_dic.items():
        if(value == max(distance_dic.values())):
            return key,value

def get_max_min_distance_tuple(agents):
    """
    Calculate the max and min distance store in the tuple

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    distance_tuple : Tuple
        A tuple that holds the maximum and minimum distances of all coordinates.

    """
    max_distance = 0
    min_distance=math.inf
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1,len(agents)):
            b = agents[j]
            distance = get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            min_distance = min(min_distance, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
    distance_tuple=(min_distance,max_distance)
    return distance_tuple

def get_max_min_distance_list(agents):
    """
    Calculate the max and min distance store in the list

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    distance_list : List
        A list that holds the maximum and minimum distances of all coordinates.

    """
    max_distance = 0
    min_distance=math.inf
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1,len(agents)):
            b = agents[j]
            distance = get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            min_distance=min(min_distance,distance)
            #print(min_distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
    distance_list=[min_distance,max_distance]
    return distance_list

def timer (n_agents,func,name):
    """
    Calculate time spent

    Parameters
    ----------
    n_agents : iterator
        iterator.
    func : function
        function.
    name : str
        function name.

    Returns
    -------
    timer : list
        Time and frequency.

    """
    
    timer=[]
    for i in n_agents:
        print(i)
        agents=create_agents(i)
        start = time.perf_counter()
        num=func(agents)
        end = time.perf_counter()
        runtime=end-start
        print("Time taken to calculate ",name,":", runtime, "seconds")
        print(name,num)
        timer.append([i,runtime])
    return timer



def add_environment(env):
    """
    Calculation of the sum of the environments

    Parameters
    ----------
    env : list
        List of environments.

    Returns
    -------
    sum_values : number
        Sum of environmental values.

    """
    sum_values=0
    for i in range(len(env)):
        for j in range(len(env[i])):
            sum_values+=env[i][j]
    return sum_values
            
def add_store(agents):
    """
    Calculation of the sum of the store

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    sum_store : number
        Sum of all store values.

    """
    sum_store=0
    for i in range(len(agents)):
        sum_store+=agents[i].store
    return sum_store

def writ_environment(address,data):
    """
    Storing the environment locally

    Parameters
    ----------
    address : str
        Address for writing documents.
    data : list
        Data for writing files.

    Returns
    -------
    None.

    """
    f = open(address, 'w', newline='')
    writer = csv.writer(f, delimiter=',')
    for row in data:
        writer.writerow(row) # List of values.
    f.close()
    
    
#File address
f='../../data/input/in.txt'

#Read the file
environment,n_rows, n_cols = io.read_data(f)

# Initialise agents
agents = []

n_agents=10
x_min=0
y_min=0
# The maximum an agents x coordinate is allowed to be.
x_max = n_cols - 1
# The maximum an agents y coordinate is allowed to be.
#y_max = 99
y_max = n_rows - 1
times=100

#Create agents
for i in range(n_agents):
    agents.append(af.Agent(i,environment,n_rows,n_cols))


#eat and move
for i in range(len(agents)):
    for j in range(times): 
        #plt.scatter(agents[i].x, agents[i].y, color='black')
        agents[i].eat()
        agents[i].move(x_min, y_min, x_max, y_max)
    plt.scatter(agents[i].x, agents[i].y, color='red')
#writ_environment("../../data/output/out.csv", environment)

#write environment
io.writ_data("../../data/output/out.csv", environment)


#To plot the agents on the environment    
plt.imshow(environment)    
    
#sum environment and sum store
sum_values=add_environment(environment)
sum_store=add_store(agents)
print(sum_values,sum_store,sum_values+sum_store)
    

# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='grey')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)
plt.show()













