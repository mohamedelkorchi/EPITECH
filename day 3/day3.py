############################################################
########################## STRINGS #########################
############################################################ 

# TASK 0

# a = 12 
# print(f'la variable a = {a}')


# TASK 1
# extraire premier et 5eme caractere

# a = 12,5,2,85,45,121,34,54,2
# print(a[4])

# b = "bonjour"
# print(b[0],b[4])


# TASK 2
# sortir le dernier caractere

# a = "azerdcvgh"
# print(a[-1:])


# TASK 3
# In one line, print from the 5th to the 10th character of this string

# a = 1,2,3,4,5,6,7,8,9,10,11
# print(a[4:11])



#########################################################################
########################## STRING METHODS ###############################
#########################################################################

# TASK 0
# Write a snippet of code that transforms any string in lower case.

# a = "BONJOUR"
# print(a.lower())

# TASK 1
# Write a snippet of code that replaces every “tu” in a string by “ta”.
# For instance, the input tutu on the tuki-kata will output tata on the taki-kata

# a = "tuki-kata"
# print(a.replace("tu", "ta"))


# TASK 2 
# Explain the following code and its printed result:

# string = " hello world "  
# position = string . find ("a")  # variable position qui = au find("recherche") de la variable precedente 
# print ( position ) # mettre la position de notre recherche, si elle n'esxiste pas le resultat sera -1 sinon position du premier caractere trouvé


# TASK 3
# Can you predict the result of the following snippet of code?

# p = "abcdefghij"
# print ( p [:: -2][:5][:: -1][3:])

# [:: -2] = "jhfdb"         # inverse et prend de 2 en 2
# [:5] = "jhfdb"            # prend les 5 premiers caractere 
# [:: -1] = "bdfhj"         # inverse et prend de 1 en 1
# [3:] = "hj"               # prend le troisieme jusqu'a la fin 


# TASK 4
# SIMPLIFIER 

# p = "abcdefghij"
# print(p[7::2])  # le 7 est la pour dire qu'on commence au 7eme caractere et le 2 pour dire de prendre de 2 en 2 

# [start: end: step]


# TAKS 5
# Write a snippet of code that prints 10 times a given string.

# a = "10 fois"
# for i in range(10):
#     print(a)


# TASK 6
# Rewrite the previous code in as few characters as possible.

# a = "nabi"
# print(a * 10)


# TASK 7 
# Debug the following code:

# s1 = " Hello "
# s2 = 42                    # mettre des guillemets pour avoir le meme type que le s1  
# concat = s1 + str(s2)      # changer grace au str. avant le nom de la variable pour la transformer en string
# print ( concat )


# TASK 8 
# Complete the following code so that it prints The string "42 is the answer" contains 16 characters.

# s1 = "42"
# s2 = "is"
# s3 = " the answer "
# concat = s1 + s2 + s3
# l = len(concat)
# print (" The string ",concat,"contains", l, "characters ).")
# print(" The string ",concat,"contains", str(len(concat)), "characters ).") # methode sans initier la variable pour la longueur 



###########################################################################################################
############################################### CHALLENGE #################################################
###########################################################################################################

# TASK 0
# Ask the user his/her name and then greet him/her with “Hello username”.

a =  "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
b = a.lower() + a.lower()[::-1]

# name = ["cat", "garden", "mice"]

# total_name = sum(name)                    # FONCTIONNE PAS 
# print(total_name)

# cat = b.count("cat")
# garden = b.count("garden")
# mice = b.count("mice")

# print(cat + garden + mice)



###################################################################################
############################# USER INPUT ##########################################
###################################################################################

# TASK 0 
# Ask the user his/her name and then greet him/her with “Hello username”.

# print("ton nom ?")
# name = str(input())

# print("Hello " + name)


# TASK 1
# Ask the user his/her name and then greet him/her with “Hello Username”, with the user’s name
# always printed with its first (and only the first) letter capitalized.

# print("quel est votre nom ?")               # pas utile 
# name = str(input("ton nom stp ?"))

# print("Hello " + name.title())


# TASK 2
# Prompt the user for two numbers and then print “The sum of the two provided numbers is sum”.

# nb1 = input("ton premier nombre ?")
# nb2 = input("ton deuxieme choix ?")

# print(int(nb1) + int(nb2))


# TASK 3 
# Complete the following snippet of code:

# nb = int(input("choisissez un nombre :"))

# print(type(nb))

# TASK 4 
# Write a program that extracts the first word of each sentences into a string, and then join them to
# make a new sentence. For instance, the input This is a test. Is it possible to fly? Good things come
# to those who never give up. should display This Is Good

# a = "this is a test."
# b = "is it possible to the fly?"
# c = "good things come "

# print(a.split(" ")[:1], b.split(" ")[:1], c.split(" ")[:1])

a = "This is a test. Is it possible to fly? Good things come to those who never give up."

print(a.split("."))

