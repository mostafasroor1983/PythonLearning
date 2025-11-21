person = ["Alice", 30, "Engineer", "New York"]
name, age, profession, city = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
print(f"City: {city}")
print("#"*50)

coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"X: {x}")
print(f"Y: {y}")
print(f"Z: {z}")
print("#"*50)
data = ["Bob", 25, "Designer", "Los Angeles", "Extra Value"]
name, age, profession, *extra = data
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
print(f"Extra: {extra}")
print("#"*50)

#Skipping values during unpacking
info = ["Charlie", 28, "Doctor", "Chicago"]
name, _, profession, _ = info
print(f"Name: {name}")
print(f"Profession: {profession}")
print("#"*50)

#Skipping values during unpacking
name, *_, city = info
print(f"Name: {name}")
print(f"City: {city}")
print("#"*50)

numbers = [1, 2, 3, 4, 5]
first, *_, last = numbers
print(f"First: {first}")
print(f"Last: {last}")
print("#"*50)
