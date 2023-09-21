# TASK 2
# Print all integers divisible by 7 from 10 000 to 1.

for i in range(1000,1,-1):    # le -1 sert à inverser la liste
    if i % 7 == 0:
        print(i)