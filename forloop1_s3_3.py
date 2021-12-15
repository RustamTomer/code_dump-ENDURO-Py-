'''
=> c/c++/jav
- syntax :-

for(initialization;condition;incre/decrement)
{
    Statement to iterate
}
- example :
for(int i=0;i<5;i++)
{
    cout<<i;
}

=> python syntax for 'for' loop
for varname in range(initialvalue,endvalue,step)
- example
for i in range(0,5,1):
    print(i)

'''

for i in range(0,5,1):
    print(i,"  ",end="")
else:
    print("PROGRAM TERMINATED")

# step always has to be non-zero.
