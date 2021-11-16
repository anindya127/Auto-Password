import random
x = "abcdefghijklmnopqrstuvwxyz"
y = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
z = "0123456789"
a = "!@#$%^&*(){}[]"
print("Note: Do not use a number bello 4 !")
A = int(input("Enter the length of the password: "))
m = int(input("Do you want upperclass characters \n1 for yes \n2 for no \n"))
if(m==1):
    b = x+y
    g = random.sample(b,A)
    gg = "".join(g)
    n = int(input("Do you want numbers \n1 for yes \n2 for no \n"))
    if(n==1):
        c = b+z
        h = random.sample(c,A)
        hh = "".join(h)
        o = int(input("Do you want special characters \n1 for yes \n2 for no \n"))
        if(o==1):
            d = c+a
            f = random.sample(d,A)
            print("Your password is: ",end="")
            for i in f:
                print(i,end="")
        elif(o==2):
            f = random.sample(hh,A)
            print("Your password is: ",end="")
            for i in f:
                print(i,end="")
    elif(n==2):
        o = int(input("Do you want special characters \n1 for yes \n2 for no \n"))
        if(o==1):
            d = b+a
            f = random.sample(d,A)
            print("Your password is: ",end="")
            for i in f:
                print(i,end="")
        elif(o==2):
            print("Your password is: ",end="")
            for i in gg:
                print(i,end="")
elif(m==2):
    b = x
    j = random.sample(b,A)
    jj = "".join(j)
    n = int(input("Do you want numbers \n1 for yes \n2 for no \n"))
    if(n==1):
        c = b+z
        k = random.sample(c,A)
        kk = "".join(k)
        o = int(input("Do you want special characters \n1 for yes \n2 for no \n"))
        if(o==1):
            d = c+a
            f = random.sample(d,A)
            print("Your password is: ",end="")
            for i in f:
                print(i,end="")
        elif(o==2):
            f = random.sample(kk,A)
            print("Your password is: ",end="")
            for i in f:
                print(i,end="")
    elif(n==2):
        o = int(input("Do you want special characters \n1 for yes \n2 for no \n"))
        if(o==1):
            d = b+a
            f = random.sample(d,A)
            print("Your password is: ",end="")
            for i in f:
                print(i,end="")
        elif(o==2):
            print("Your password is: ",end="")
            for i in jj:
                print(i,end="")