#Coppying list with reference
original_list = [1, 2, 3, 4, 5]
copied_list = original_list  # This creates a reference to the original list
print("Original List before modification:", original_list)
copied_list.append(6)
print("Original List after modification through copied_list:", original_list)
print("#"*50)

# Copying list using slicing,SHALLOW COPY
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]  # This creates a shallow copy of the original list
print("Original List before modification:", original_list)
copied_list.append(6)
print("Original List after modification through copied_list:", original_list)
print("#"*50)

# Copying list using the list() constructor,SHALLOW COPY
original_list = [1, 2, 3, 4, 5]
copied_list = list(original_list)  # This creates a shallow copy of the original list
print("Original List before modification:", original_list)
copied_list.append(6)
print("Original List after modification through copied_list:", original_list)
print("#"*50)

# Copying list using the copy() method ,SHALLOW COPY
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()  # This creates a shallow copy of the original list
print("Original List before modification:", original_list)
copied_list.append(6)
print("Original List after modification through copied_list:", original_list)
print("#"*50)

# Copying list using the copy module ,DEEP COPY
import copy
original_list = [1, 2, 3, 4, 5]
copied_list = copy.deepcopy(original_list)  # This creates a deep copy of the original
print("Original List before modification:", original_list)
copied_list.append(6)
print("Original List after modification through copied_list:", original_list)
print("#"*50)

# Summary of methods to copy a list
print("Summary of methods to copy a list:")
print("1. Using assignment operator (creates reference)")
print("2. Using slicing (creates shallow copy)")
print("3. Using list() constructor (creates shallow copy)")
print("4. Using copy() method (creates shallow copy)")
print("5. Using copy.deepcopy() (creates deep copy)")




