import random
from matplotlib import pyplot as plt
import operator

#list0=[random.randint(0,99)for i in range(2)]
#list1=[random.randint(0,99)for i in range(2)]
#agents=[list0,list1]
#print(agents)

agents=[]
for i in range(100):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
# Plot the agents
for i in range(100):
    plt.scatter(agents[i][0], agents[i][1], color='black')

# Get the coordinates with the largest x-coordinate
#print(max(agents, key=operator.itemgetter(0)))
max_x=max(agents, key=operator.itemgetter(0))

#overplot the dot with the largest x coordinate in red
plt.scatter(max_x[0],max_x[1],color='red')


#the smallest x coordinate using the colour blue; 
min_x=min(agents, key=operator.itemgetter(0))
plt.scatter(min_x[0],min_x[1],color='blue')

#the largest y coordinate using the colour yellow;
max_y=max(agents, key=operator.itemgetter(1))
plt.scatter(max_y[0],max_y[1],color='yellow')
#the smallest y coordinate using the colour green.
min_y=min(agents, key=operator.itemgetter(1))
print(max_x,min_x,max_y,min_y)
plt.scatter(min_y[0],min_y[1],color='green')

# Move agents
def ChangeRandomly (agents):
    for i in range(len(agents)):
        for j in range(2):
            r = random.random()
            if r < 0.5:
                agents[i][j] +=1
            else:
                agents[i][j] -=1
    return(agents)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
def Calculate (list0,list1):
    distance=((list0[0]-list1[0])**2+(list0[1]-list1[1])**2)**0.5
    return(distance)


distance=Calculate(max_x,max_y)
print("distance",distance)
agents=ChangeRandomly(agents)
distance=Calculate(max_x,max_y)
print("distance",distance)

plt.show()








