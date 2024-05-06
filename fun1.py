def myfunction():
    print("hello world")
myfunction()

def add(a,b):
    c=a+b
    print('addition is',c)
add(20,30)

def add():
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    c=a+b
    return c
ans=add()
print("addition is",ans)


def profile(fname,mname,lname):
    print(fname+" "+mname+" "+lname)
profile('ritika','prashant','bhandari')


def wholename(name):
    for i in name:
        print(i)
profile=["ritika","prashant","bhandari"]
wholename(profile)


def sqr(a):
    return a*a
print(sqr(4))

def cube(a):
    return a**3
print(cube(2))