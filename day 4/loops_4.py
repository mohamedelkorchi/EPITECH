# TASK 5
# Generate the lyrics of the song “99 bottles of age appropriate bottles on the wall”.
# The songs ends when there is no more bottles on the wall.

b = 99

while b > 0:
    print(f"{b} bottles of age")
    print(f'{b} bottles of age')
    print("take one, pass it around")
    b -= 1
    if b ==0:
        print("no more bottles")
    else:
        print(f"{b} bottles of age")