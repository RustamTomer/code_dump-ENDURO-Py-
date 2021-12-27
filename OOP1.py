class MyClass:
    x=10
    def fun1(self):   #"self" is the curr obj like c++ and java has "this"
        print("From fun1 of MyClass")

o=MyClass()
print(o.x)   # "." is used to access the values of MyClass
o.fun1()