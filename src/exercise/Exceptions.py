# Catch an exception
import random
try:
    a = 1/random.random()
except:
    a = 0
finally:
    if a == None:
        a = -1
print("Done")