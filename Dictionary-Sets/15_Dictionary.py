#syntax of dictionary
dict1 = {
    "Fast": "In a Quick Manner",
    "Kartik": "A Coder",
    "Marks": [4,8,9], #Lists in Dictionary
    "subdict": { #Dictionary in Dictionary
        "PVAINDIA": "Digital Agency",
        "Services": "Web Development"
    }
}

#printing dictionary
print(dict1)
print(dict1['Fast'])
print(dict1["Kartik"])
print(dict1["Marks"]) #Printing Lists in Dictionary
print(dict1["subdict"]) #Printing Dictionary in Dictionary
print(dict1["subdict"]['Services']) #Printing Value of one index of Dictionary in Dictionary

#Dictionary Facts
# Unordered, Mutable, Indexed, Cannot contain duplicate keys


