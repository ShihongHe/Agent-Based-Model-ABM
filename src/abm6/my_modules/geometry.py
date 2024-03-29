import math
import time
import model



  
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
    """
    Calculate the maximum distance to store in the list

    Parameters
    ----------
    agents : list
        A list of stored coordinates

    Returns
    -------
    distance : list
        Store a list of all distances between coordinates.

    """
    distance=[]
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1,len(agents)):
            b = agents[j]
            distance.append(get_distance(a.x,a.y, b.x, b.y))
    return distance
    

def get_arithmetic_mean(agents):
    """
    Calculate the arithmetic mean

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    mean : Number
        Calculate the mean of all coordinate distances.

    """
    distance=get_distance_list(agents)
    mean=sum(distance)/len(distance)
    return mean

def get_standard_deviation(agents):
    """
    Calculate the standard deviation

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    standard_deviation : Number
        Calculate the standard deviation of all coordinate distances.

    """
    deviations=0
    mean=get_arithmetic_mean(agents)
    distance=get_distance_list(agents)
    for i in distance:
        deviations+=(i-mean)**2
    standard_deviation=(deviations/len(distance))**0.5
    return standard_deviation

def get_median(agents):
    """
    Calculate the median

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    median : Number
        Calculate the median of all coordinate distances


    """
    distance_list=get_distance_list(agents)
    distance_list.sort()
    if len(distance_list)%2:
        median=distance_list[len(distance_list)//2+1]
        
    else:
        median=(distance_list[len(distance_list)//2]+distance_list[len(distance_list)//2]+1)/2
    return median

def get_mode(agents):
    """
    Calculate the mode

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    key : Number
        Number of mode for all coordinate distances.
    value : Number
        DThe value of the mode of all coordinate distances.

    """
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
    Calculate the max and min distance store in the tuple

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    distance_tuple : Tuple
        A tuple that holds the maximum and minimum distances of all coordinates.

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
    """
    Calculate the max and min distance store in the list

    Parameters
    ----------
    agents : list
        A list of stored coordinates.

    Returns
    -------
    distance_list : List
        A list that holds the maximum and minimum distances of all coordinates.

    """
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

def timer (n_agents,func,name):
    """
    Calculate time spent

    Parameters
    ----------
    n_agents : iterator
        iterator.
    func : function
        function.
    name : str
        function name.

    Returns
    -------
    timer : list
        Time and frequency.

    """
    
    timer=[]
    for i in n_agents:
        print(i)
        agents=model.create_agents(i)
        start = time.perf_counter()
        num=func(agents)
        end = time.perf_counter()
        runtime=end-start
        print("Time taken to calculate ",name,":", runtime, "seconds")
        print(name,num)
        timer.append([i,runtime])
    return timer
