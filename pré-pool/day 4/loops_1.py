# TASK 1
# Ask the user a string.
# Display all the characters of this string twice.
# For instance: “taxi” will become “ttaaxxii”.

a = input("entrer un mot : ")

doubled_string = "".join(char * 2 for char in a)

print(doubled_string)