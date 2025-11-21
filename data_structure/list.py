empty = []
print("Empty list:", empty)
print("Type of empty list:", type(empty))
print("#"*50)

mixed_list = [1, True, "two", 3.0, [4, 5], (6, 7)]
print("Mixed list:", mixed_list)
print("Type of mixed list:", type(mixed_list))
print("#"*50)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Matrix (2D list):", matrix)
print("Type of matrix:", type(matrix))
print("#"*50)

for row in matrix:
    for item in row:
        print("Item:", item)
print("#"*50)

python = list("Python")
for char in python:
    print("Character:", char)
