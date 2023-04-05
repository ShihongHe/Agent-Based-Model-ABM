import random
from matplotlib import pyplot as plt
import operator

class Agent:
    def __init__(self, i):
        """
        The constructor method.

         Parameters
         ----------
         i : Integer
         To be unique to each instance.

         Returns
         -------
         None.

        """
        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        pass
    
    def __str__(self):
        """
        Defining the print format

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.__class__.__name__ + "(id:"+str(self.i)+", x=" + str(self.x)+ ", y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    def move(self, x_min, y_min, x_max, y_max,times):
        """
        Random movement of coordinates

        Parameters
        ----------
        x_min : number
            Limit to the smallest x.
        y_min : number
            Limit to the smallest y.
        x_max : number
            Limit the maximum x.
        y_max : number
            Limit the maximum x.

        Returns
        -------
        None.

        """
        for i in range(times):
            # Change agents[i] coordinates randomly
            # x-coordinate
            rn = random.random()
            if rn < 0.5:
                self.x = self.x + 1
            else:
                self.x = self.x - 1
            if self.x<x_min:
                self.x=x_min
            elif self.x>x_max:
                self.x=x_max
            # y-coordinate
            rn = random.random()
            if rn < 0.5:
                self.y = self.y + 1
            else:
                self.y = self.y - 1
            if self.y<y_min:
                self.y=y_min
            elif self.y>y_max:
                self.y=y_max
        
            


if __name__=="__main__":
    agents = []
    x_min=0
    y_min=0
    x_max=100
    y_max=100
    times=10000
    n_agents=100
     
    for i in range(n_agents):
        # Create an agent
        agents.append(Agent(i))
        #print(agents[i])
        plt.scatter(agents[i].x, agents[i].y, color='black')
        agents[i].move(x_min, y_min, x_max, y_max,times)
        #print("move:",agents[i])
        plt.scatter(agents[i].x, agents[i].y, color='red')
    # Plot the coordinate with the largest x red
    lx = max(agents, key=operator.attrgetter('x'))
    plt.scatter(lx.x, lx.y, color='red',s=100)
    # Plot the coordinate with the smallest x blue
    sx = min(agents, key=operator.attrgetter('x'))
    plt.scatter(sx.x, sx.y, color='blue',s=100)
    # Plot the coordinate with the largest y yellow
    ly = max(agents, key=operator.attrgetter('y'))
    plt.scatter(ly.x, ly.y, color='yellow',s=100)
    # Plot the coordinate with the smallest y green
    sy = min(agents, key=operator.attrgetter('y'))
    plt.scatter(sy.x, sy.y, color='green',s=100)
    plt.show()













