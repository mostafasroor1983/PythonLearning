# This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Could not find data.txt, {e}")
    content = "default data"
print("Done!")  # Always reaches here