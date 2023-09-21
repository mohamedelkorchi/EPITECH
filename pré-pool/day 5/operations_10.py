# TASK 10
# Test this code and try to explain it:

first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
magic = [* zip ( first_name , last_name [:: -1]) ]

print ( magic [0])
print ( magic [3])
print ( magic [1][0])        # LE DEUXIEME CROCHET EST POUR CHOISIR LA VARIABLE
print ( magic [0][1])
print ( magic [2])