import random



# Initialise variable x0 y0 x1 y1
list0=[random.randint(0,99)for i in range(2)]
list1=[random.randint(0,99)for i in range(2)]
print("list0",list0,"list1",list1)


# Change  randomly
def ChangeRandomly (coordinates):
    for i in range(2):
        r = random.random()
        if r < 0.5:
            coordinates[i] +=1
        else:
            coordinates[i] -=1
        print(coordinates[i])
    return(coordinates)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
def Calculate (list0,list1):
    distance=((list0[0]-list1[0])**2+(list0[1]-list1[1])**2)**0.5
    return(distance)

distance=Calculate(list0,list1)
print("distance",distance)
list0=ChangeRandomly(list0)
list1=ChangeRandomly(list1)
distance=Calculate(list0,list1)
print("distance",distance)




