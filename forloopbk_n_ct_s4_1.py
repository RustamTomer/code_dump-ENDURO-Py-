for i in range(0,15,1):
    print(i,"  ",end="")
    if(i==11):
        break
else:
    print("PROGRAM TERMINATED")

for i in range(0,15,1):
    if(i==11):
        continue
    print(i)
else:
    print("PROGRAM TERMINATED")