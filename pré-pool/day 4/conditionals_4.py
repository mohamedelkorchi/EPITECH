# TASK 4
# Ask the user to input an integer:

a = int(input())

if a == 42 :
    print("OK")
elif a <= 21:
    print("OK")
elif a % 2 == 0 :
    print("OK")
elif a/2 < 21:
    print("OK")
elif a % 2 != 0 and a >= 45:
    print("OK")
else:
    print("you got wrong my poor friend")
