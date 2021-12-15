x=int(input(' Enter first number'))
y=int(input(' Enter second number'))
if(x>y):
    print("x is greater than y")
else:
    print("y is greater than x")

'''
Q.   What happens if we don't add 'int' in syntax ?
Ans. Interpreter will consider input as string type and use memory location to provide answer
     i.e. it will jump to 'else' clause.

If u don't want to write false part u can skip it.
'''

x=int(input(' Enter first number'))
y=int(input(' Enter second number'))
if(x>y):
    print("x is greater than y")

'''
result of this - u won't get any output as u haven't specified what should py provide u with if cond is flase.

Now if u want the same with 'if' clause u can't skip it as the syntax starts with it.
but u can write 'pass' under 'if' part then the program will work.
'''

x=int(input(' Enter first number'))
y=int(input(' Enter second number'))
if(x>y):
    pass
else:
    print("y is greater than x")