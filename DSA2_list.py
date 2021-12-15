name=[]
print(name)
print("Size of list is", len(name))
name.append("Rustam")
name.append("Olaf")
name.append("Jeff")
name.append("Ryan")
name.append("Jeff")
print(name)
print(name[0])
print(name[1])
'''
append adds data to end of list
to add in b/w use 'insert'
'''
name.insert(2,"Derek")
print(name)
# to remove element use 'pop' which removes data from end of list.
# name.pop()
# print(name)
# to remove particular data use 'remove'
# name.remove("Olaf")
# print(name)

for i in range(0,len(name)):
    print(name[i])

# short version of 'for' used in DSA

#for n in name :
#    print(n)

# n uses data in mentioned list and prints as long as list has data.
# 'count' is there to check repetition

print("Jeff has appeared", name.count("Jeff"), "times")

# to check if element is in list or not as well as index no. =>
if "Ryan" in name:
    print("Found Ryan at", name.index("Ryan"), "Index")
else:
    print("Not Found")

if "Olaf" in name:
    x=name.index("Olaf")
    name.remove("Olaf")
    name.insert(x,"Harry")
    print(name)
else:
    print("Olaf Not Found")

# if copies of data are there in list initial index data will get removed by using 'remove'.

#sorting 
name.sort()
print("Sorted list is as follows", name)

# to get descending list =>
name.sort(reverse=True)
print("Sorted list is as follows", name)

# slicing list
print(name[0:3])

# DS type identify
print(type(name))

#ADDITION OF LISTS
lst1=[1,2,3]
lst2=[4,5,6]
lst3=lst1+lst2
print(lst3)

#'clear' fn
lst2.clear()
print(lst2)
print(lst3)
#list still present in memory though.
lst3=lst1+lst2          #list 3 is updated
print(lst3)             #prints only 1 2 3, since list 2 is empty

'''
to del from mem as well use 'del'
'''
del lst2
print(lst2)
print(lst3)
