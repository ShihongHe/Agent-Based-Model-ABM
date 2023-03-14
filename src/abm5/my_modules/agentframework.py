import random

class Agent:
    def __init__(self, i,environment,n_rows,n_cols):
        """
        The constructor method.

         Parameters
         ----------
         i : Integer
         To be unique to each instance.
         n_rows : Integer
         The number of rows in environment.
         n_cols : Integer
         The number of columns in environment.

         Returns
         -------
         None.

        """
        self.i = i
        self.environment = environment
        self.x = random.randint(n_cols/3 - 1, 2 * n_cols / 3)
        self.y = random.randint(n_rows/3 - 1, 2 * n_rows / 3)
        self.store = 0

    def __str__(self):
        return self.__class__.__name__ + "(id:"+str(self.i)+", x=" + str(self.x)+ ", y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    def move(self, x_min, y_min, x_max, y_max):
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
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store+=self.environment[self.y][self.x]
            self.environment[self.y][self.x]=0
            
        
            














