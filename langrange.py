print("program for langrange interpolation")
x=[]
y=[]
n=int(input("enter tha number of datapoints:"))
for i in range(0,n):
    elect=float(input("enter the values of x:"))
    x.append(elect)
print("x=",x)
for i in range(0,n):
    elect=float(input("enter the values of y:"))
    y.append(elect)
print("y=",y)
xr=float(input("enter the value of x to be interpolated"))
fy=0
for j in range(0,n):
    num=1
    den=1
    for i in range(0,n):
        if i!=j:
            num*=(xr-x[i])
            den*=(x[j]-x[i])
    fy=float(fy+(num/den)*y[j])
print("value of xr at x=",xr,'value of y is=',fy)