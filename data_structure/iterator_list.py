#enumerate example
my_list = ['apple', 'banana', 'cherry']
enumerated_list = enumerate(my_list, start=1)    
print("Using enumerate() to get index and value:",list(enumerated_list))
print
for index, value in enumerated_list:
    print(f"Index: {index}, Value: {value}")
print("#"*50)

#iterator example
my_list = [10, 20, 30, 40, 50]
iterator = iter(my_list)
print("Using next() to iterate through the list:")
print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30
print(next(iterator))  # Output: 40
print(next(iterator))  # Output: 50
print("#"*50)   

#Iteraing for reverse order
my_list = [1, 2, 3, 4, 5]
reverse_iterator = reversed(my_list)  #Iterable for reverse order
print("Using reversed() to iterate through the list in reverse order:")
for item in reverse_iterator:  
    print(item)
print("#"*50)

#Using map to apply a function to each item
my_list = [1, 2, 3, 4, 5]
squared_iterator = map(lambda x: x**2, my_list)
print("Using map() to apply a function to each item in the list:", list(squared_iterator))
print("#"*50)

letters = ['a', 'b', 'c']
letters_iterator = map(str.upper, letters)
print("Using map() to convert each letter to uppercase:", list(letters_iterator))
print("#"*50)   

#Using filter to filter items based on a condition
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_iterator = filter(lambda x: x % 2 == 0, my_list)
print("Using filter() to get even numbers from the list:", list(even_iterator))
print("#"*50)

letters = ['a', '', 'c', 'd', None, False,'e']
filtered_iterator = filter(None, letters)
print("Using filter() to remove falsy values from the list:", list(filtered_iterator))
print("#"*50)


