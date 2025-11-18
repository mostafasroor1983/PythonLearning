country = "Syria"
print(f"Is country alphabetic? {country.isalpha()}")  # True
city = "Damascus123"
print(f"Is city alphanumeric? {city.isalnum()}")  # True
postal_code = "12345"
print(f"Is postal code numeric? {postal_code.isdigit()}")  # True
mixed = "Data2024"
print(f"Is mixed alphanumeric? {mixed.isalnum()}")  # True
whitespace_str = "   \t\n"
print(f"Is whitespace_str only whitespace? {whitespace_str.isspace()}")  # True
empty_str = ""
print(f"Is empty_str empty? {empty_str == ''}")  # True