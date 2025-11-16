count = 10    # An integer
price = 3.99  # A float
is_available = True  # A boolean
greeting = "Hello, World!"  # A string  
none = None  # A NoneType

print(type(count), count)
print(type(price), price)
print(type(is_available), is_available)
print(type(greeting), greeting)
print(type(none), none)

print(f"Count: {count}, Price: {price}, Available: {is_available}, Greeting: {greeting}")

print("--- String Operations ---")
# String operations
print(len(greeting))  # Length of the string
print(greeting.upper())  # Convert to uppercase
print(greeting.lower())  # Convert to lowercase
print(greeting.replace("World", "Python")) 


print("---- Integer Operation ------") # Replace substring
print(count.bit_count())  # Number of set bits in the integer
print(count.bit_length())  # Number of bits required to represent the integer