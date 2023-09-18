# TASK 0
# Write 5 functions, each taking a string s and an integer n as parameters and returning a boolean:

# ✓ funA checks if s contains at least n lowercase letters;



# ✓ funE checks if s contains at least n numbers.


# def funA(s,n):
#     count = 0
#     for i in range(len(s)):
#         if s[i].islower() == True:
#             count += 1
#     print(count)

#     if count >= n:
#         return True
#     else :
#         return False
    
# print(funA("Wech LinA",2))



# ✓ funB checks if s contains at least n uppercase letters;

# def funB(s,n):
#     count = 0
#     for i in range(len(s)):
#         if s[i].isupper() == True:
#             count += 1
#     print(count)

#     if count >= n:
#         return True
#     else :
#         return False
    
# print(funB("Wech LinA",4))


# ✓ funC checks if s contains at least n characters;

# def funC(s,n):
#     count = 0
    
#     if count >= len(s):
#         return True
#     else :
#         return False
    
# print(funA("Oue c'est ssa",15))


#✓ funD checks if s contains at least n special chara0cters;

def funD(s, n):
   
   count = 0

   for c in s:
       if (c.isalpha() or c.isdigit() or c == " "):
        return False
       else :
           count += 1
           return True

   if count >= n:
     return True
   else :
     return False
       
print(funD("Wech le @$ mec du 94", 1))




