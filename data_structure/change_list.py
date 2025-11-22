#Adding item to a list using append()
numbers = [10, 23, 45, 23, 67, 89]
print("Original list:", numbers)
numbers.append(100)
print("List after appending 100:", numbers)
print("#"*50)

#Appeding Matrix to demonstrate extend()
matrix = [[1, 2], [3, 4]]
print("Original matrix:", matrix)
matrix.append([5, 6])
matrix[1].append(99)
matrix.extend([[7, 8], [9, 10]])
print("Matrix after extending:", matrix)
print("#"*50)


#Inserting item at a specific index using insert()
numbers.insert(2, 50)
print("List after inserting 50 at index 2:", numbers)
print("#"*50)

matrix[0].insert(1, 88)
print("Matrix after inserting 88 at row 0, index 1:", matrix)
print("#"*50)


#Clearing all items from a list using clear()
temp_list = [1, 2, 3, 4, 5]
print("Temporary list before clearing:", temp_list)
temp_list.clear()
print("Temporary list after clearing:", temp_list)
print("#"*50)

#removing item by value using remove()
numbers.remove(23)
print("List after removing first occurrence of 23:", numbers)
print("#"*50)

#removing item by index using pop()
removed_item = numbers.pop(3)
print("List after popping item at index 3:", numbers)
print("Removed item:", removed_item)
print("#"*50)


matrix2 = [[10, 20], [30, 40], [50, 60]]
popped_row = matrix2.pop(1)
print("Matrix after popping row at index 1:", matrix2)
print("Popped row:", popped_row)
print("#"*50)

matrix2[-1].pop(0)
print("Matrix after popping item at index 0 of last row:", matrix2)
print("#"*50)   

