#Combining two lists into a list of tuples
print("#"*50)
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
com_list = list1 + list2
com_list2 = [list1, list2]
multiplied_list = list1 * 3
print("Combined List using + operator:", com_list)  
print("Combined List as list of lists:", com_list2)
print("Multiplied List using * operator:", multiplied_list)
print("#"*50)


#Extending a list with another list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list1.extend(list2)
print("List after extending with another list:", list1)
print("#"*50)


#Using zip to combine two lists into a list of tuples
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
zipped_list = list(zip(list1, list2))
zipped_list2 = list(zip(list1, list2, "Hi"))
print("Zipped List using zip():", zipped_list)
print("Zipped List with different lengths using zip():", zipped_list2)
print("#"*50)



