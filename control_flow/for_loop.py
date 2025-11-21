for i in [1,2,3,4,5]:
    print(i)

for i in range(1,6):
    print(i)

for i in range(0,16,2):
    print(i)

for char in "Hello":
    print(char)

for item in ["apple", 42, 3.14, True]:
    print(item)
print("#"*50)

scores = [85, 90, 78, 92, 88]
total = 0
for score in scores:
    total += score
    print("Current total:", total)
print("Total Score:", total)
print("#"*50)

names = ["Alice", "Bob", "", "Charlie"]
for name in names:
    if name == "":
        break #continue
    print("Hello,", name)
else:
    print("All names have been greeted.")
print("#"*50)
