print(True)
print(False)
print(not True)
print(not False)
print(True and False)
print(True or False)
print("#"*50)

print(type(True))
print(bool(1))
print(bool(0))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(None))
print(bool())
print(bool(""))
print(bool("Hello"))
print("#"*50)

# Validate using any and all
usernam = ""
email = ""
phone = "963-872632362"

# Allow registration if any of the contact info is provided
print(any([usernam, email, phone]))  # True if any value is truthy

# Allow registration if all contact info is provided
print(all([usernam, email, phone]))  # True if all values are truthy
print(isinstance(True, bool) and isinstance(False, bool))
print("#"*50)

# Boolean conditions operations
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

score = 85
if 95 > score >= 90:
    print("Grade: A")
elif 90 > score >= 80:
    print("Grade: B")
elif 80 > score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
print("#"*50)
