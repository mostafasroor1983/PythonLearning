#Tuples used to store multiple items in a single variable
#Tuples are ordered, unchangeable, and allow duplicate values
#Tuples are defined by enclosing the items in parentheses ()
#Creating a tuple
my_tuple = ("apple", "banana", "cherry")

#Accessing tuple items
print(my_tuple[1])  # Output: banana    
#Tuples are immutable, so we cannot change their items
#my_tuple[1] = "orange"  # This will raise a TypeError
#However, we can convert the tuple to a list, modify it, and convert it back to a tuple
temp_list = list(my_tuple)
temp_list[1] = "orange"
my_tuple = tuple(temp_list)
print(my_tuple)  # Output: ('apple', 'orange', 'cherry')
#Tuple methods
#count() - returns the number of times a specified value occurs in a tuple
print(my_tuple.count("apple"))  # Output: 1
#index() - searches the tuple for a specified value and returns its position
print(my_tuple.index("cherry"))  # Output: 2

#Tuple unpacking
fruit1, fruit2, fruit3 = my_tuple
print(fruit1)  # Output: apple
print(fruit2)  # Output: orange
print(fruit3)  # Output: cherry

#Looping through a tuple
for fruit in my_tuple:
    print(fruit)
# Output:
# apple
# orange
# cherry

#Tuple length
print(len(my_tuple))  # Output: 3

#Creating a tuple with one item (note the comma)
single_item_tuple = ("apple",)
print(type(single_item_tuple))  # Output: <class 'tuple'>

#Creating a tuple without parentheses
another_tuple = "apple", "banana", "cherry"
print(another_tuple)  # Output: ('apple', 'banana', 'cherry')
print(type(another_tuple))  # Output: <class 'tuple'>

