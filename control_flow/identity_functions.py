# Identity Opertor Example
# check if both operands refer to the same object in memory
a = [1, 2, 3]
b = a
print(a is b)        # True, both refer to the same list object

a1 = 10
a2 = 10
print(f"a1 is a2: {a1 is a2}")           # True, both refer to the same integer object

email = None
print(f"email is None : {email is None}")  # True, email is None