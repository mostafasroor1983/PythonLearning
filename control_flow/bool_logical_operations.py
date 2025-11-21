#Logical Operations in Python

a = True
b = False
# AND operation
and_result = a and b  # False
# OR operation
or_result = a or b    # True
# NOT operation
not_result = not a    # False
print("AND Result:", and_result)
print("OR Result:", or_result)
print("NOT Result:", not_result)
print("#"*50)

# Combining multiple logical operations
x = 10
y = 5
z = 15
complex_result = (x > y) and (z > x) and not (y == z)  # True
print("Complex Logical Operation Result:", complex_result)
