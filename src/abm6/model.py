     # -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:17:22 2023

@author: He
"""



from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.geometry as geometry
import my_modules.io as io
import imageio
import os






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






if __name__ == '__main__':
    #read environment
    f='../../data/input/in.txt'
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
    n_iterations=100
    neighbourhood=100

    #creat agents 
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

    
    
    # Model loop
    for ite in range(n_iterations):
        #print("Iteration", ite)
        # Move agents
        #print("Move")
        for i in range(n_agents):
            agents[i].move(x_min, y_min, x_max, y_max)
            agents[i].eat()
            #print(agents[i])
        # Share store
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
        print("Maximum distance between all the agents",  geometry.get_max_distance(agents))
        # Print the total amount of resource
        sum_as = sum_agent_stores(agents)
        print("sum_agent_stores", sum_as)
        sum_e = sum_environment(environment)
        print("sum_environment", sum_e)
        print("total resource", (sum_as + sum_e))
        
        #io.writ_data("../../data/output/out.csv", environment)
        
        for i in range(len(agents)):

            plt.scatter(agents[i].x, agents[i].y, color='red')
            
        
        plt.imshow(environment)
        plt.ylim(y_max / 3, y_max * 2 / 3)
        plt.xlim(x_max / 3, x_max * 2 / 3)
        # Plot the coordinate with the largest x grey
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
        
        
        filename = '../../data/output/images/image' + str(ite) + '.png'
        #filename = '../../data/output/images/image' + str(ite) + '.gif'
        plt.savefig(filename)
        plt.show()
        plt.close()
        images.append(imageio.imread(filename))
        
    imageio.mimsave('../../data/output/out.gif', images, fps=3)
        
        




    
        
    


        
        

    # Plot the coordinate with the largest x grey
    #lx = max(agents, key=operator.attrgetter('x'))
    #plt.scatter(lx.x, lx.y, color='grey')
    # Plot the coordinate with the smallest x blue
    #sx = min(agents, key=operator.attrgetter('x'))
    #plt.scatter(sx.x, sx.y, color='blue')
    # Plot the coordinate with the largest y yellow
    #ly = max(agents, key=operator.attrgetter('y'))
    #plt.scatter(ly.x, ly.y, color='yellow')
    # Plot the coordinate with the smallest y green
    #sy = min(agents, key=operator.attrgetter('y'))
    #plt.scatter(sy.x, sy.y, color='green')
    

    

        

    
    
    
    
    















