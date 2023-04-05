     # -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:17:22 2023

@author: He
"""



import time
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.geometry as geometry
import my_modules.io as io
import imageio
import os
import matplotlib.animation as anim


#Number of initialized objects
n_agents=10
x_min=0
y_min=0

#Number of initialization cycles
n_iterations=100

#Distance thresholds for neighbourhoods
neighbourhood=100


    



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
        agents.append(af.Agent(agents,i,environment,n_rows,n_cols))
    return agents


def sum_environment(env):
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
            
def sum_agent_stores(agents):
    """
    Calculation of the sum of the storemn

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



def plot():
    """
    Executed on the first call to FuncAnimation

    Returns
    -------
    fig : TYPE
        DESCRIPTION.

    """
    #Clear the canvas
    fig.clear()
    
    #Limit x, y range
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.imshow(environment)
    
    #plot
    for i in range(n_agents):
        plt.scatter(agents[i].x, agents[i].y, color='black')
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
    global ite
    #Save the images and name each one
    filename = '../../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show()
    
    #Adding metadata for images in images
    images.append(imageio.imread(filename))
    return fig

def update(frames):
    """
    updata data

    Parameters
    ----------
    frames : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # Model loop
    global carry_on
    #for ite in range(n_iterations):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
    #move and eat
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    #print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", geometry.get_max_distance(agents))
    # Print the total amount of resource
    sum_as = sum_agent_stores(agents)
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment(environment)
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))

    # Stopping condition
    # Random
    #if random.random() < 0.1:
    if sum_as / n_agents > 80:
        carry_on = False
        print("stopping condition")

    #Plot
    #global ite
    
    #Plot the coordinates after the move
    plot()
    #ite = ite + 1


 
def gen_function():
    """
    Get Iterator   

    Yields
    ------
    TYPE
        Iterator.

    """
    global ite
    ite = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (ite < n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Write data
        print("write data")
        io.write_data('../../data/output/out7.txt', environment)
        imageio.mimsave('../../data/output/out7.gif', images, fps=3)
        data_written = True


        






if __name__ == '__main__':
    #read environment
    f='../../data/input/in.txt'
    environment,n_rows, n_cols = io.read_data(f)
    # Initialise agents
    agents = []

    
    # The maximum an agents x coordinate is allowed to be.
    x_max = n_cols - 1
    # The maximum an agents y coordinate is allowed to be.
    y_max = n_rows - 1
    
    #creat agent
    agents=create_agents(n_agents)
    
    
    
    
    # Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")

    # For storing images
    global ite
    ite = 0
    images = []
    
    # Animate
    # Initialise fig and carry_on
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True
    data_written = False
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    #animation.save("animation.gif", writer="imagemagick")       
            
                
            
    

       

        
        




    
        
    


        
        


    

        

    
    
    
    
    















