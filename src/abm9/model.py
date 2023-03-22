     # -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:17:22 2023

@author: He
"""



import tkinter as tk
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.geometry as geometry
import my_modules.io as io
import imageio
import os
import matplotlib.animation as anim
import matplotlib
import requests
import bs4



matplotlib.use('TkAgg')




n_agents=10
x_min=0
y_min=0
n_iterations=100
neighbourhood=100


    
def run(canvas):
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    animation.new_frame_seq()
    canvas.draw()


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


#Executed on the first call to FuncAnimation
def plot():
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


#updata data
def update(frames):
    # Model loop
    global carry_on
    #for ite in range(n_iterations):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
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
    plot()
    #ite = ite + 1
    
#Get Iterator    
def gen_function():
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
        
def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)
    
    
def output():
    pass


      






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
    #agents=create_agents(n_agents)
    
    
    
    
    # Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")

    # For storing images
    global ite
    ite = 0
    images = []
    
    
    
    # Initialise agents

    #url = agdturner.github.io/resources/abm9/data.html
    r = requests.get('http://agdturner.github.io/resources/abm9/data.html', verify=False)
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    print(td_ys)
    print(td_xs)
    agents = []
    for i in range(n_agents):
        # Create an agent
        y = int(td_ys[i].text) + 99
        x = int(td_xs[i].text) + 99
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols, x, y))
        print(agents[i].agents[i]) 
      
    
    # Animate
    # Initialise fig and carry_on
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True
    data_written = False
    #animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    #animation.save("animation.gif", writer="imagemagick")

    # GUI
    root = tk.Tk()
    root.wm_title("Agent Based Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    menu_0 = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Model", menu=menu_0)
    menu_0.add_command(label="Run model", command=lambda: run(canvas))
    menu_0.add_command(label="Write data", command=lambda: output())
    menu_0.add_command(label="Exit", command=lambda: exiting())
    menu_0.entryconfig("Write data", state="disabled")
    # Exit if the window is closed.
    root.protocol('WM_DELETE_WINDOW', exiting)
    tk.mainloop()       
                

                
            
    

       

        
        




    
        
    


        
        


    

        

    
    
    
    
    















