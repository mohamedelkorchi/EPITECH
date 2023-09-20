# TASK 4
# Write a plt_fct function that plots any function taking x as a parameter.
# Its arguments must match the following example.

# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import math
import numpy as np

def f(x):
    return x **2 + x *3 + 2


def plot_fct ( f,x_min,x_max ) :
    x = np.linspace(x_min, x_max, 100)
    y = []

    for i in range(len(x)):
        y.append(f(x[i]))

    plt.plot(x,y)
    plt.grid(True)
    plt.show()
    

plot_fct ( math.sin , 0 , 50)
plot_fct (f , -100 , 200)
plot_fct ( lambda x : x **2 , -10 , 10)
plot_fct ( lambda x : 1/ x , -100 , 100)



