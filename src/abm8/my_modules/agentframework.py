import random
import my_modules.geometry as geometry

class Agent:
    def __init__(self, agents, i, environment, n_rows, n_cols):
        """
        The constructor method.

        Parameters
        ----------
        agents : List
            A list of Agent instances.
        i : Integer
            To be unique to each instance.
        environment : List
            A reference to a shared environment
        n_rows : Integer
            The number of rows in environment.
        n_cols : Integer
            The number of columns in environment.

        Returns
        -------
        None.

        """
        self.agents = agents
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        self.store = random.randint(0,99)
        self.store_shares = 0
    
    def __str__(self):
        """
        Defining the print format

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.__class__.__name__ + "(id:"+str(self.i)+", x=" + str(self.x)+ ", y=" + str(self.y) + ", store:"+str(self.store)+", store_shares:"+str(self.store_shares)+")"
    
    def __repr__(self):
        return str(self)
    def move(self, x_min, y_min, x_max, y_max):
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
            
                
    def eat(self):
        """
        eat environment store in store

        Returns
        -------
        None.

        """
        if self.store>=100:
            self.environment[self.y][self.x]+=self.store/2
            self.store-=self.store/2
            
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store+=self.environment[self.y][self.x]
            self.environment[self.y][self.x]=0
            
    def share(self, neighbourhood):
        """
        Shore within threshold shared with each other

        Parameters
        ----------
        neighbourhood : number
            Distance from neighbourhood.

        Returns
        -------
        None.

        """
        # Create a list of agents in neighbourhood
        neighbours = []
        #print(self.agents[self.i])
        for a in self.agents:
            distance = geometry.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
        # Calculate amount to share
        n_neighbours = len(neighbours)
        #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
        #print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares

            
        
            














