# TASK 10 
# Add 17 elements at the end of your list.

from random import*

a = [1,2]

for i in range(17):                 # 17 ajouts
#  n = randint(22,85)                 # aleatoire entre 22 et 85
 a.append(randint(22,85))                        # append pour ajouter ce qu'il y a dans la variable {n} dans la variable {a}

print(a)