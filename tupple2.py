mylist=("ritika","prashant","bhandari","sonali","naitik")

# convert tuple into list
temp=list(mylist)
print(mylist)

temp=list(mylist)
temp[2]="iphone"
mylist=tuple(temp)
print(mylist)

temp=list(mylist)
temp.append("mango")
mylist=tuple(temp)
print(mylist)

# while loop -> in while loop you need to give every instruction at different place
i=0
while i<len(mylist):
    print(mylist[i])
    i=i+1

# for loop
for i  in mylist:
    if i=="mobile":
        break
print(i)

mylist2=(10,20,30,40)
ans=mylist + mylist2
print(ans)

ans=mylist*3
print(ans)
