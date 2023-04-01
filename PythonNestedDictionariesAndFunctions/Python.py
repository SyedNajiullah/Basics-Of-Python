def printDictionary(carDict): # TO PRINT THE DICTIONARY
    for key, value in carDict.items():
        print(key, ":-")
        for innerKey, innerValue in value.items():
            print("\t",innerKey, ":", innerValue)

def search(carDict):  # TO SEARCH DICTIONARY IN A NESTED DICTIONARY
    isFound = False
    outerSearch = input("Enter Outer Key to search:")
    if outerSearch not in carDict:
        print("Value Not Found")
        isFound = True
    else:
        innerSearch = input("Enter Inner Key to search:")
        for key, values in carDict.items():
            for innerKey, innerValues in values.items():
                if innerSearch == innerKey:
                    isFound = True
                    break
            if isFound == True:
                break
        if isFound == True:
            print(f"Value of {outerSearch} and {innerSearch} is {carDict[outerSearch][innerSearch]}")
        else:
            print("Value Not Found")
            
def add(carDict): # TO ADD A NESTED DICTIONARY
    outerSearch = input("Enter Outer Key to add:")
    if outerSearch in carDict:
        print("Key Already found")
    else:
        name = input("Enter car name:")
        colour = input("Enter car colour:")
        company = input("Enter car company:")
        newDict = {
            "Name" : name,
            "Colour": colour,
            "Company": company
        }
        carDict[outerSearch] = newDict

def remove(carDict): # TO REMOVE A DICTIONARY
    outerSearch = input("Enter Outer Key to remove:")
    if outerSearch not in carDict:
        print("Outer Key is not present")
    else:
        del carDict[outerSearch]

#CREATING DICTIONARY

carDict = {
    "Car1" : {
        "Name" : "Tesla Model S",
        "Colour" : "BLack",
        "Company" : "Tesla"
    },
    "Car2" : {
        "Name" : "Toyota Camry",
        "Colour" : "White",
        "Company" : "Toyota"
    },
    "Car3" : {
        "Name" : "Porsche 911",
        "Colour" : "Black",
        "Company" : "Porshe"
    }
}
#PRINTING DICTIONARY
printDictionary(carDict)
#SEARCHING DESIRED VALUE BY USER
search(carDict)
#ADD VALUE IN A DIRECTORY
add(carDict)
print("\t--------------------------------")
print("\t---AFTER ADDING DIRECTORY IS ---")
print("\t--------------------------------")
printDictionary(carDict)
#REMOVE VALUE IN A DIRECTORY
remove(carDict)
print("\t----------------------------------")
print("\t---AFTER DELETING DIRECTORY IS ---")
print("\t----------------------------------")
printDictionary(carDict)