x=[5,4,2,6,3,7,1]
max=x[0]
c=[]
for i in range(1,len(x)):
    if x[i]>max:
        max=x[i]
c.append(max)
print(c)
