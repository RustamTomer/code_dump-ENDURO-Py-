i=10
while(i>0):
    print(i)
    if i==5:
        break
    i-=1
else:
    print("While Loop Ends")

#'else' clause isn't executed if break statement is present.

#if u want to print output in same line then use this.

i=10
while(i>0):
    print(i,"  ",end="")
    if i==5:
        break
    i-=1
