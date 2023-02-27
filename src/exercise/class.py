class Agent():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Goat(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hungry = True

class Wolf(Agent):
    def __init__(self, x, y, pack):
        super().__init__(x, y)
        self.pack = pack
        
class Agent():
    def __init__(self, ax, ay):
        self._x = ax
        self._y = ay

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")        
        
    
    
    

class Agent():
    def __init__(self, ax, ay):
        self._x = ax
        self._y = ay

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
        

if __name__ == '__main__':
    a = Agent(0, 0)
    a.x = 3
    print(a.x) # <-- Prints 3
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    