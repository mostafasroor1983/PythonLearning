#Dictionary Example
my_dict = {"name": "John",
           "age": 30,
           "city": "New York"}

#Accessing dictionary items
print(my_dict["name"])     # Output: John
print(my_dict.get("age"))  # Output: 30

#Modifying dictionary items
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

#Adding new items
my_dict["job"] = "Engineer"
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

#Removing items
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 31 , 'job': 'Engineer'}

my_dict.pop("job")
print(my_dict)  # Output: {'name': 'John', 'age': 31}

#Looping through a dictionary
for key in my_dict:
    print(key, my_dict[key])
# Output:
# name John
# age 31        
