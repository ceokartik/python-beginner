#1make a list by []
list1 = [1,4,7,12,16,90]

#2print a list
print(list1)

#3access list using indexes
print(list1[0],list1[5])

#4change list value
list1[0]= 20
print(list1)

#5list can have different data types
list1=['Kartik',18,True,3.5]
print(list1)

#6list slicing
list2=["harry","Tom",45,"Kartik"]
print(list2[2:])

#7list sorting
list3=[14,65,32,68,22,43,68,99,22]
list3.sort()
print(list3)

#8list reverse
list4=[14,65,32,68,22,43,68,99,22]
list4.reverse()
print(list4)

#9list append
list5=[14,65,32,68,22,43,68,99,22]
list5.append(49)
print(list5)

#10list insert
list6=[14,65,32,68,22,43,68,99,22]
list6.insert(3, 'Kartik')
print(list6)

#11pop a value
list7=[14,65,32,68,22,43,68,99,22]
list7.pop(4)
print(list7)

#12remove from list
list8=[14,65,32,68,22,43,68,99,22]
list8.remove(32)
print(list8)

