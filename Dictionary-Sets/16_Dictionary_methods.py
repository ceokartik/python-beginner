dict1 = {
    "Fast": "In a Quick Manner",
    "Kartik": "A Coder",
    "Marks": [4,8,9], 
    "subdict": {
        "PVAINDIA": "Digital Agency",
        "Services": "Web Development",
        1:2
    }
}

print(dict1.keys()) #Print Keys
print(type(dict1)) #Printing type of dictionary
print(list(dict1.keys())) #Typecasting Possible
print(dict1.values()) #Printing Dictionary Values
print(dict1.items()) #Print (key,values) for all contents of dictionary

#Updating Dictionary
newdict={
    "TEC":"The Epic Code",
    "Marks": [4,8,10] #alters the value of key is same
} 
dict1.update(newdict)
print(dict1) 

#get method

print(dict1.get('Kartik'))
print(dict1.get('Iamnotthere')) #Prints None
print(dict1['Iamnnotthere']) #Throws Error
