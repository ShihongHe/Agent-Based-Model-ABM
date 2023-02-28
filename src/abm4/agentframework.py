import random
from matplotlib import pyplot as plt


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
        return self.__class__.__name__ + "(id:"+str(self.i)+", x=" + str(self.x)+ ", y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    def move(self, x_min, y_min, x_max, y_max,times):
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
plt.show()













