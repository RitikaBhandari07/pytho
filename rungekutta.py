print("program for runge kutta method")
def f(x,y):
    return(x+y)
x0=float(input("enter the value of x0"))
y0=float(input("enter the value of y0"))
xr=float(input("enter the value of x at which y is to be found "))
h=float(input("enter the value of stepsize "))
while(x0<xr):
    k1=h*f(x0,y0)
    k2=h*f(x0+h/2,y0+k1/2)
    k3=h*f(x0+h/2,y0+k2/2)
    k4=h*f(x0+h,y0+k3)
    k=1/6*(k1+2*k2+2*k3+k4)
    print("k=",k)
    y1=y0+k
    x1=x0+k
    print("y1=",y1)
    print("x1=",x1)
    x0=x1
    y0=y1
print("end")