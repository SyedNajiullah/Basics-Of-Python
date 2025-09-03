#What are dictionaries used for?
#Instead of storing data in seperate array like the following

name_arr = ["Syed Najiullah", "Syed Safiullah"]
age_arr = [21, 22]
roll_number_arr = ["lwo312421", "odjld0192"]
gmail_arr = ["najiullahsyed2@gmail.com", "yajra.table@gmail.com"]

#We should store them like the following in dictionaries in key value pairs to increase the code readability and it would become easy to add, update, and delete information.

student_one = {
    "name": "Syed Najiullah",
    "age": 21, 
    "roll_number": "lwo312421",
    "gmail": "najiullahsyed2@gmail.com",
}
student_two = {
    "name": "Syed Safiullah",
    "age": 22, 
    "roll_number": "odjld0192",
    "gmail": "yajra.table@gmail.com",
}
print(student_one)
print(student_two)

#Creating an empty dictionary
my_dict = dict()
print(my_dict)

# Add a new column
my_dict["Name"] = "Syed Najiullah"
my_dict["age"] = 21
my_dict["roll_number"] = "lwo312421"
my_dict["gmail"] = "najiullahsyed2@gmail.com"
print(my_dict)

#deleting a column
del my_dict["roll_number"]
print(my_dict)

#updating a column
my_dict["gmail"] = "twoanother96@gmail.com"
print(my_dict)

# Traversing in dictionary
for keys in my_dict.keys():
    print(keys, end = ", ")
print()
for values in my_dict.values():
    print(values, end=", ")
print()
for key, values in my_dict.items():
    print(f"Key: {key}, value: {values}")

#Searching in dictionary
#searching by keys
if "age" in my_dict:
    print(f"Age found")

#searching by values
search_age = 21
if search_age in my_dict.values():
    print("Name found in dictionary")
else:
    print("Name not found")
    
#Only immutable data types can be made keys in dictionaries such as strings, Boolean, numbers, touples. Things that are mutable are dictionaries and Lists which is wjy they cannot be made keys
foo_correct = {
    "string": "string",
    True: "boolena",
    20: "number",
    (1, 2): "Touple"
}
print(foo_correct)
# The following code results in error
# foo_false = {
#     [1, 2]: "List",
#     {3: 1, 4: 4}: "dict"
# }
# print(foo_false)


# #time complexity of dictionary is 0(1)
# Operation	     Time_Complexity	Description
# Search by key    O(1)	            Instant!
# Add new item     O(1)	            Instant!
# Update value     O(1)	            Instant!
# Delete by key    O(1)	            Instant!
# Search by value  O(n)	            Gets slower
# Get all keys/values O(n)	        Gets slower
