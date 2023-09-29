def check(n):
    if n>1 and n/n == 1 and n/1 == n:
        print(f"{n} is a prime number") 
    else:
        print(f"{n} is not a prime number")

print("entrez un numero :")
check(int(input()))


