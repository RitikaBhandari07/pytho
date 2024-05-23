def fun(x):
    return 2*x**5+3*x**3+7*x-13
a=float(input("enter the first value :"))
b=float(input("enter the second value:"))
fa=fun(a)
fb=fun(b)
print("value of fa :",fa)
print("value of fb :",fb)

if fa==0 or fb==0:
    print("\n it is the limit of root for given equation")
else:
    if (fa*fb)<0.0:
        print("\n there exist a root in between the given interval")
    else:
        print("\n no root")
