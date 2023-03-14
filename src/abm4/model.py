# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:17:22 2023

@author: He
"""
import math
import random
import time
import agentframework as af
from matplotlib import pyplot as plt
import operator

a = af.Agent()
b = af.Agent()
print("type(a)", type(a))

# Initialise agents
agents = []

n_agents=10
x_min=0
y_min=0
x_max=100
y_max=100
times=10000
for i in range(n_agents):
        # Create an agent
        agents.append(af.Agent(i))
        #print(agents[i])
        plt.scatter(agents[i].x, agents[i].y, color='black')
        agents[i].move(x_min, y_min, x_max, y_max,times)
        #print("move:",agents[i])
        plt.scatter(agents[i].x, agents[i].y, color='red')
plt.show()



random.seed(0)
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
    distance=[]
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1,len(agents)):
            b = agents[j]
            distance.append(get_distance(a.x,a.y, b.x, b.y))
    return distance
    

def get_arithmetic_mean(agents):
    distance=get_distance_list(agents)
    mean=sum(distance)/len(distance)
    return mean

def get_standard_deviation(agents):
    deviations=0
    mean=get_arithmetic_mean(agents)
    distance=get_distance_list(agents)
    for i in distance:
        deviations+=(i-mean)**2
    standard_deviation=(deviations/len(distance))**0.5
    return standard_deviation

def get_median(agents):
    distance_list=get_distance_list(agents)
    distance_list.sort()
    if len(distance_list)%2:
        median=distance_list[len(distance_list)//2+1]
        
    else:
        median=(distance_list[len(distance_list)//2]+distance_list[len(distance_list)//2]+1)/2
    return median

def get_mode(agents):
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

def timer (n_agents,func):
    """
    Calculated running time
    
    Parameters
    ----------
    n_agents : iterator

    Returns
    -------
    timer : list
        Time and frequency

    """
    timer=[]
    for i in n_agents:
        agents.append(af.Agent())
        start = time.perf_counter()
        distance=func(agents)
        end = time.perf_counter()
        runtime=end-start
        print("Time taken to calculate maximum distance", runtime, "seconds")
        print("distanse",distance)
        timer.append([i,runtime])
    return timer

def ChangeRandomly (agents):
    for i in range(len(agents)):
        r = random.random()
        if r < 0.5:
            agents[i].x +=1
        else:
            agents[i].x -=1
        r = random.random()
        if r < 0.5:
            agents[i].y +=1
        else:
            agents[i].y -=1
    return(agents)





for i in agents:
    plt.scatter(i.x, i.y, color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
plt.show()






 
"""
n_iterations =10
#agents=create_agents(100)
# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99


mean=get_arithmetic_mean(agents)
deviation=get_standard_deviation(agents)
median=get_median(agents)  
distance_dic=get_mode(agents)
print(mean,deviation,median,distance_dic) 



for j in range(n_iterations):
    agents=ChangeRandomly(agents)
    for i in range(len(agents)):
        # Apply movement constraints.
        if agents[i].x < x_min:
            agents[i].x = x_min
        if agents[i].y < y_min:
            agents[i].y = y_min
        if agents[i].x > x_max:
            agents[i].x = x_max
        if agents[i].y > y_max:
            agents[i].y = y_max

mean=get_arithmetic_mean(agents)
deviation=get_standard_deviation(agents)
median=get_median(agents)  
distance_dic=get_mode(agents)
print(mean,deviation,median,distance_dic)










n_agents=range(500,5000,500)

#mean=get_arithmetic_mean(agents)
#deviation=get_standard_deviation(agents)
#median=get_median(agents)  
#distance_dic=get_mode(agents)
#print(mean,deviation,median,distance_dic)  



max_agents=timer(n_agents,get_max_distance)
max_min_tuple=timer(n_agents,get_max_min_distance_tuple)
max_min_list=timer(n_agents,get_max_min_distance_list)
mean=timer(n_agents,get_arithmetic_mean)
standard_deviation=timer(n_agents,get_standard_deviation)
#print(n_agents)

# Plot
plt.title("Time taken to calculate maximum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")

for i in max_agents:
    plt.scatter(i[0], i[1], color='red')
for i in max_min_tuple:
    plt.scatter(i[0], i[1], color='blue')
for i in max_min_list:
    plt.scatter(i[0], i[1], color='yellow')
for i in mean:
    plt.scatter(i[0], i[1], color='green')
"""










