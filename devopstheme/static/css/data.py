import numpy as np
import math

def data():
    b = np.arange(0, 10, .5)
    for a in b:
        y = (math.sin(math.radians(121+(a*27)))*35)-30
        x = math.cos(math.radians(120+(a*27)))*30+15
#        print (str(a) + "X = " + str(x))
        print (str(a) + "X = " + str(x))

data()
