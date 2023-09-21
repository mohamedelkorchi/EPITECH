# TASK 3 
# Write a function that takes an array of points as argument and displays the points in a nice and
# clean chart.

# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

points=[(0,12),(1,32),(2,42),(3,52)]

def graf(points):

    plt.grid(True)
    plt.plot([x[0] for x in points], [y[1] for y in points], "or" )
    plt.show()

    return

graf(points)