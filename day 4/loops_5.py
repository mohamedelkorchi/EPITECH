# TASK 5
# Write a program that takes an n integer as input and displays, for each integer from 2 to n/2, the
# list of its multiples strictly smaller than n, in descending order.

n = int(input("entre un nombre :"))

for i in range(2,n//2+1):
   k = 1
   multiple = []
   while (k * i < n) :
      multiple.append(k*i)
      k += 1
   print(*multiple[::-1])