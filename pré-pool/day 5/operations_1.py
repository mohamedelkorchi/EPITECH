# TASK 1
# Create a list of 10 numbers.
# Print the result of the multiplication of all elements of this list.

a = [1,2,3,4,5,6,7,8,9,10]
b = 1

for i in range(9):
    b*= a[i]

print(b)
