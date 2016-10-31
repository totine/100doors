#100doors

doors=[]
for n in range (100):
    doors.append(0)

for n in range (1,101):
    for i in range (0,101,n):
        if doors[i-1]==0:
            doors[i-1]=1
        else:
            doors[i-1]=0

#open doors list
open_doors=[]
for n in range (100):
    if doors[n]==1:
        open_doors.append(n+1)

#output
print("The following doors are open: ", end="")
for n in range (len(open_doors)):
    if n < len(open_doors)-1:
        print(str(open_doors[n])+", ", end="")
    else:
        print(str(open_doors[n]))
