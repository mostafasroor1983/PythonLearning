#Transformations

price_str = "19.99"
price_float = float(price_str)
print(type(price_str))    # Output: <class 'str'>
print(type(price_float))  # Output: <class 'float'>
print(price_float)        # Output: 19.99

price1 = "10,999"
print(price1.replace(",", "."))  # Output: 10000 
price_float = float(price1.replace(",", "."))
print(type(price_float))  # Output: <class 'float'>
print(price_float)       # Output: 10000

print("--- Operators ---")
lname = "Mostafa"
fname = "Srour"
full_name = lname + " " + fname
print(full_name)   # Output: Mostafa Srour


print("--- fString ---")
age = 24
greeting = f"Hello, My name is {full_name}, and my age is {age} years old."
print(greeting)   # Output: Hello, My name is Mostafa Srour, and my age is 24 years old.

