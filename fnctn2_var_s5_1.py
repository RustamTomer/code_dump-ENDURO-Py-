x=10 #Global Variable
y=20 #Global Variable
def add():
    global name
    name = "Rustam"
    print("Hello", name)
    z=x+y #local var
    print("Sum is ",z)
def sub():
    z=x-y
    print("Diff is ", z)

add()
sub()

print(x)
print("Output is this", name)

'''
-Global variables can be accessed outside fnctn but it doesn't go that way for local.
if u try to access local outside 'fn' intrepreter will show error.
-GlobalVars are accesible throughout the program 
which is not posiible if we define the same under 'fn' i.e. if they are made to be local vars.
- To access local var outside 'fn' use command 'global varname' inside defined 'fn'.

-
global name = "Rustam"

- Declaring GloVar like this is incorrect and u will end up getting error.
- python wil self assume input as int or string in above written code but
if u type it as
=> z=int(x)+int(y)
then u can only cast in int string float etc. are no longer castable.
'''