#Splitting and cleaning strings in Python
csv_row = "Mostafa, 29, Engineer, Dubai "
print(csv_row.strip())  # Remove leading/trailing whitespace
print(csv_row.split(','))  # Split by comma
print("#"*50)


#Slicing strings in Python
name = "Mostafa"
print(name[2])    # Output: s
print(name[-5])   # Output: s
print(name[0:4])  # Output: Most
print(name[0:-3]) # Output: Most
print(name[-3:])  # Output: afa
print(name[:3])   # Output: Mos
print(name[::2])  # Output: Msaa
print("#"*50)


#Cleaning strings in Python
raw_string = "   Hello, World!   "
print(f"'{raw_string.lstrip()}'")  # Output: 'Hello, World! '    
print(f"'{raw_string.rstrip()}'")  # Output: ' Hello, World!'  
print(f"'{raw_string.strip()}'")   # Output: 'Hello, World!' 
print("#"*50)

raw_string2 = "###Hello, World!###"
print(f"'{raw_string2.lstrip('#')}'")  # Output: 'Hello, World!###'    
print(f"'{raw_string2.rstrip('#')}'")  # Output: '###Hello, World!'  
print(f"'{raw_string2.strip('#')}'")   # Output: 'Hello, World!'

is_clean2 = len(raw_string2.strip("#")) == len(raw_string2)
print(f"raw_string2 is_clean: {is_clean2}")  # Output: is_clean2: True
print("#"*50)
