#Analyzing and processing a list of numbers
numbers = [10, 23, 45, 67, 89, 12, 34, 56, 78, 90]
print("Original list of numbers:", numbers)
print("Type of numbers list:", type(numbers))
print("#"*50)

#Calculating the sum of all numbers in the list
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)
print("#"*50)

#Finding the maximum and minimum values in the list
max_value = max(numbers)
min_value = min(numbers)
print("Maximum value in the list:", max_value)
print("Minimum value in the list:", min_value)
print("#"*50)

#Calculating the average of the numbers in the list
average = total_sum / len(numbers)
print("Average of the numbers:", average)
print("#"*50)   

#Sorting the list in ascending order
sorted_numbers = sorted(numbers)
print("Sorted list (ascending):", sorted_numbers)
print("#"*50)

#Sorting the list in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Sorted list (descending):", sorted_numbers_desc)
print("#"*50)

#Filtering even and odd numbers from the list
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("#"*50)

#Finding the index of a specific number in the list
specific_number = 45
if specific_number in numbers:
    index = numbers.index(specific_number)
    print(f"Index of {specific_number} in the list:", index)
else:
    print(f"{specific_number} is not in the list.")
print("#"*50)

#Counting occurrences of a specific number in the list
count_number = 23
occurrences = numbers.count(count_number)
print(f"Occurrences of {count_number} in the list:", occurrences)
print("#"*50)

#checking if a number exists in the list
check_number = 100
exists = check_number in numbers
print(f"Does {check_number} exist in the list?:", exists)
print("#"*50)

#check the equality of two lists
list_a = [10, 23, 45]
list_b = [10, 23, 45]
are_equal = list_a == list_b
are_identical = list_a is list_b
print(f"Are list_a and list_b equal, holding the same values?:", are_equal)
print(f"Are both lists identical?:", are_identical)
print("#"*50)

#All and any functions
all_greater_than_five = all(num > 5 for num in numbers)
any_greater_than_eighty = any(num > 80 for num in numbers)
print("Are all numbers greater than 5?:", all_greater_than_five)
print("Is any number greater than 80?:", any_greater_than_eighty)
print("#"*50)









