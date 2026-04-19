e =int(input("Enter number:"))
f =int(input("Enter  number:"))
g =int(input("Enter  number:"))
if e < f and e < g:
    print("smaller number=",e)
elif f < e and f < g:
    print("smaller number=",f)
else:
    print("smallest number=",g)