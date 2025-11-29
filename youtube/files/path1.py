from pathlib import Path

# check if folder/file is exists
ecommerce_path = Path("ecommerce")
print(ecommerce_path.exists())
print("#"*50)

#create a new folder
email_path = Path("email")
#print(email_path.mkdir())
print("#"*50)

#loop through the files in one path and print
#path = Path()
path = Path("data_types")
for file in path.glob("*.py"):
    print(file)
print("#"*50)

