x = 9
y = 9.9
z = 3 + 9j
print(type(x))      
print(type(y))      
print(type(z))      
print("#"*50)


x1 = 8.99
x1 = int(x1)
print(f"x1 after conversion to int: {x1} | type: {type(x1)}")
print("#"*50)  

y1 = "10.8"
y1 = float(y1)
print(f"y1 after conversion to float: {y1} | type: {type(y1)}")
print("#"*50)

z1 = 5   #real part
z11 = 4.5 #imaginary part
z1 = complex(z1, z11)
print(f"z1 after conversion to complex: {z1} | type: {type(z1)}")
print("#"*50)