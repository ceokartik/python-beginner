set1={1,3,7,9} #Making a set

# adding to sets
set1.add(12)
print(set1)
set1.add(15)
print(set1) 

# set1.add([1,3,7,9]) #We cannot add list to sets
set1.add((1,3,7,9)) #We can add tuple to sets
print(set1)

print(len(set1)) #Prints length of Set

set1.remove(3)
print(set1)

 