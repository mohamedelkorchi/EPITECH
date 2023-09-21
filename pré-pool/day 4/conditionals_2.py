# TASK 2 
# Ask an integer to the user:

def check_numbers(n):
    if n%2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is oden')

print("entrer un nombre : ")
check_numbers(int(input()))