fruits={"Apple", "Cherry", "Mango", "Banana"}
print(fruits)
print(type(fruits))

#Based out output it is clear that 'set' is always unindexed and unordered.
#Any index concept cannot be used also set is unchangeable though new values can be added.

fruits.add("Orange")
print(fruits)

#As it is a non linear data structure duplicate values cannot be added
fruits.add("Cherry")
print(fruits)

#Numeric inputs are sorted in ascending order by default (tree structure of binary tree format).
numbers={3,10,4,1,9,5,11,6,0}
print(numbers)

numbers.remove(5)
print(numbers)
numbers.discard(6)
print(numbers)
#if we use discard for a num not present in set no error is thrown but in case of remove it happens.

#for concatination of two sets union and update command can be used.
fxn=fruits.union(numbers)
print(fxn)

#If the two sets have any element in common it gets printed only 1 time.
