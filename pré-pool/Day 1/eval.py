def hidenp(x,y):
    compteur=0
    res=0
    for i in range(len(x)):
        for j in range (len(y)):
            if x[i]==y[j] and j>compteur:
                compteur=j
                res+=1
                break
    if res==len(x):
        print("%d\n"%(1))
    else:
        print("%d\n"%(0))

hidenp("padinton","zasp45a2dizefnt4d5soapdkl45n")
hidenp("abc",("00bc12a"))