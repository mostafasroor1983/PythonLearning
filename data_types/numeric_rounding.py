import math

#Rounding numbers
num1 = 5.6789
print(f"Original number: {num1}")   
rounded_num1 = round(num1, 2)
print(f"Rounded to 2 decimal places: {rounded_num1}")  
rounded_num2 = round(num1)
print(f"Rounded to nearest integer: {rounded_num2}")  
print(f"Truncate the number: {int(num1)}")  
print("#"*50)

# Math module for advanced rounding
num2 = 3.14159
print(f"Original number: {num2}")
ceil_num2 = math.ceil(num2)
print(f"Ceiling value: {ceil_num2}")
floor_num2 = math.floor(num2)
print(f"Floor value: {floor_num2}")
print("#"*50)

num3 = 2.5
print(f"Original number: {num3}")
rounded_num3 = round(num3)
print(f"Rounded value: {rounded_num3}")
print("#"*50)

num4 = 3.5
print(f"Original number: {num4}")
rounded_num4 = round(num4)
print(f"Rounded value: {rounded_num4}")
print("#"*50)