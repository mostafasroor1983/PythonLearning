#Searching substrings in a string
phone = "+963515123456"
print(phone.startswith("+963"))  # Check if string starts with +963
print(phone.endswith("3456"))    # Check if string ends with 3456
print(phone.find("512"))         # Find the index of substring "512"
print(phone.find("999"))         # Find the index of substring "999" (not found)
#print(phone.index("999"))       # Get the index of substring "999" (will raise an error if not found)
print(phone.count("5"))          # Count occurrences of "5"
print("#"*50)

email = "mostafa.sroor@gmail.com"
print(email.startswith("mostafa"))  # Check if email starts with "mostafa"
print(email.endswith("gmail.com"))  # Check if email ends with "gmail.com"
print(email.find("@"))              # Find the index of "@" in the email
print(email.index("@"))             # Get the index of the first "." in the email
