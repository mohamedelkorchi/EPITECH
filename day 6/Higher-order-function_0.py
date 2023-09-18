# TASK 0
# Write 5 functions, each taking a string s and an integer n as parameters and returning a boolean:

# ✓ funA checks if s contains at least n lowercase letters;
# ✓ funB checks if s contains at least n uppercase letters;
# ✓ funC checks if s contains at least n characters;
#✓ funD checks if s contains at least n special chara0cters;
# ✓ funE checks if s contains at least n numbers.


def funA(s,n):
    count = 0
    for i in range(len(s)):
        if s[i].islower() == True:
            count += 1
    print(count)

    if count >= n:
        return True
    else :
        return False
    
print(funA("Wech LinA",2))


def funA(s,n):
    count = 0
    for i in range(len(s)):
        if s[i].isupper() == True:
            count += 1
    print(count)

    if count >= n:
        return True
    else :
        return False
    
print(funA("Wech LinA",4))