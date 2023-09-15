# CHALLENGE 
# Create a list of 1 000 000 random integers and sort it as fast as possible

import random
import time

a = []
startingTime = time.time()

for i in range(1000000):
    a.append(random.randint(0,10))

duration = time.time()-startingTime
print(duration)