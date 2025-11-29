import requests

post_id = 2
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
response = requests.get(url)
data = response.json()
print(data)
print(type(data))
print(data.keys()) #return keys of dict as List
print(f"UserId : {data["userId"]}")
print("#"*50)