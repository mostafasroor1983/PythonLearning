#Sorting letters list in ascending order
letters = ['d', 'a', 'c', 'b', 'e']
print("Original letters list:", letters)
letters.sort()
print("Letters list sorted in ascending order:", letters)
print("#"*50)

#Sorting numbers list in descending order
numbers = [34, 12, 5, 67, 23]
print("Original numbers list:", numbers)
numbers.sort(reverse=True)
print("Numbers list sorted in descending order:", numbers)
print("#"*50)

matrix = [
    [9, 8, 7],
    [3, 2, 1],
    [6, 5, 4]
]
print("Original matrix:", matrix)
matrix.sort()
print("Matrix sorted based on the first element of each sublist:", matrix)
print("#"*50)   

#Leave the original list unchanged and return a new sorted list
letters = ['d', 'a', 'c', 'b', 'e']
sorted_letters = sorted(letters, reverse=True)
print("Original letters list:", letters)
print("Letters list sorted in descending order using sorted():", sorted_letters)
print("#"*50)


#Revserse the order of elements in a list
fruits = ['apple', 'banana', 'cherry', 'date']
print("Original fruits list:", fruits)
fruits.reverse()
print("Fruits list after reversing the order:", fruits)
print("#"*50)

#Reverse a copy of the original list using slicing
fruits = ['apple', 'banana', 'cherry', 'date']
print("Original fruits list:", fruits)
reversed_fruits = list(reversed(fruits))
print("Fruits list after reversing the order:", reversed_fruits)

