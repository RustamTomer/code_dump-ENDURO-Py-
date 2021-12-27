names=("Rustam", "Kapish", "Yuvraj", "Larry", "Noel")
print(names)
print(type(names))
print(names.index("Larry"))
print(names.count("Yuvraj"))

for n in names:
    print(n)

#Conversion of tuple into list.
my_names=list(names)
print(my_names)
print(type(my_names))
#Now we can add or remove anything.
my_names.append("Harry")
print(my_names)
#Now we can convert the list back into a tuple.
names=tuple(my_names)
print(names)
print(type(names))


