print("#" * 50)
multiple = lambda x: x * 2
add = lambda x, y: x + y
print("multiple(5) : ", multiple(5))  # Output: 10
print("add(3, 7)   : ",add(3, 7))        # Output: 10
print("#" * 50)


check_in = lambda item, string: item in string
print("check_in('a', 'apple') : ", check_in('a', 'apple'))  # Output: True
print("check_in('b', 'apple') : ", check_in('b', 'apple'))  # Output: False
print("#" * 50)

prices = ['$88.10', '$45.00', '$23.50', '$12.75']
remove_dollar = lambda price: float(price.replace('$', ''))
print("Original prices: ", prices)
cleaned_prices = list(map(remove_dollar, prices))
average_price = sum(cleaned_prices) / len(cleaned_prices)
print("Cleaned prices: ", cleaned_prices)  # Output: [88.1, 45.0, 23.5, 12.75]
print("Average price: ", average_price)  # Output: 42.5875
print("#" * 50)

#Filtering with lambda
numbers = [10, 23, 45, 60, 72, 91]
is_even = lambda x: x % 2 == 0
even_numbers = list(filter(is_even, numbers))
print("Original numbers: ", numbers)
print("Even numbers: ", even_numbers)  
print("#" * 50)

#Sorting with lambda
students = [('Alice', 25), ('Bob', 20), ('Charlie', 23) , ('David', 22)]
sorted_students = sorted(students, key=lambda student: student[1])
print("Original students: ", students)
print("Sorted students by age: ", sorted_students)
print("#" * 50)

