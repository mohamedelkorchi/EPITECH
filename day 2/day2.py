##########################################################
####################### VARIABLE ######################### 
##########################################################

# task 1 

# s = sum(int('1'* i) for i in range(1,10))
# powers = [s** i for i in range(2,8)]

# print(f'Sum: {s}')
# for i, p in enumerate(powers, 2):
#  print(f'Power {i}: {p}')

# methode Lina

# a = 0
# res = 0
# for i in range(1,10) : 
#  b = a * 10 + 1
#  a = b 
#  print(b)
#  res+= a 
#  print(res)

#  print("results : ")
#  for j in range(2,7):
#   print(j, res**j)

# task 2 

# result = 17**1024
# print(result)
 
# autre methode 

# a = 2
# for i in range(1,10):
#     b = a * 2
#     a = b 

# print(17**b)

###########################################
################# MODULO ##################
###########################################

# task 1 

# result = 42 / 4
# print(result)
# a = 42 // 4
# print(a)
# b = 42 % 4
# print(b)

# autre methode 

# a = 42
# b = 4

# c = a / b 
# print(c)

# d = a // b
# print(d)

# e = a % b
# print(e)

# task 2

# def extract(l):
#     pair = []
#     impair = []
#     for x in l:
#         if(x%2 == 0):
#             pair.append(x)
#         else:
#             impair.append(x)

#     print("La liste des entiers pair est : ",pair)
#     print("La liste des entiers impair est : ",impair)
# # Tester l'algorithme
# l =[23,4,56,7,8,9,0,18,7,6,55,43,2]
# print(extract(l))

# AUTRE METHODE 

# def check_numbers(n):
#     if n % 2 ==0:
#         print(f"{n} est pair")
#     else:
#         print(f"{n} est impair")

# # test fonction 
# print("Entrez un nombre")
# check_numbers(int(input()))

# task 3

# def sum(n):
#     if n // 10 == 0:
#         return n 
#     else:
#         return n % 10 + sum(n//10)
    
# print(sum(123434565))
# print(sum(345567426))
# print(sum(44490320097))


# task 4 

# a = 12.24
# b = 424242.8412

# print(int(a))
# print(int(b))


# task 5

# a = 12.24
# b = 424242.8412

# print (a%1)
# print(b%1)

# challenge 

# a = 12.24
# b = 424242.8412

# print (a%1 , b%1)


#############################################################
########### ARCHIMEDES CONSTANT AND MORE ####################
#############################################################


# TASK 1 

# # def pi():
# pi = 0 
# n = 4
# d = 1
# for i in range (1,1000000):
#     a = 2 * (i % 2) - 1  # si modulo pair ca fera une addition sinon soustraction 
#     pi += a * n / d  # += pour incrémenter 
#     d += 2
# print(round(pi,1000))
# # pi()