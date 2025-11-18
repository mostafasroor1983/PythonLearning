#MNumeric Validation Examples
x = 9.0
is_integer_x = x.is_integer()
print(f"Is x an integer? {is_integer_x}")
y = 10.5
is_integer_y = y.is_integer()
print(f"Is y an integer? {is_integer_y}")
print("#"*50)

z = 7.0
if z.is_integer():
    z = int(z)
print(f"Value of z after validation and conversion: {z} | type: {type(z)}")
print("#"*50)

w = 8.3
if w.is_integer():
    w = int(w)
print(f"Value of w after validation: {w} | type: {type(w)}")
print("#"*50)

a = 12.0
print(f"is {a} an integer? {isinstance(a, int)}")
print(f"is {a} an float? {isinstance(a, float)}")


