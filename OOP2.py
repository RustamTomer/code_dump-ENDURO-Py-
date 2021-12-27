class MyClass:
    x=0 #class variable has a scope throughout the class.
    def __init__(self,x):
        print("init fn")
       # self.x=x #no need to call init fn as creating obj is enough to call it.
        # now no need of setData as init is present
 #   def setData(self,x): #x declared within function has scope only in function
  #      self.x=x #classVar x get the value of localVar x which is 10.

    def printData(self):
        print("x is", self.x) #prints the value of classVar x.

o=MyClass(10)
#o.setData(10)
o.printData()













        