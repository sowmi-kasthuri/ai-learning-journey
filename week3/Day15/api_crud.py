# POST — Create Data
'''
Sends new data to the server (e.g., creating a new post, user, or record).
Data usually goes in the request body as JSON.
'''
import requests
'''
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Learning APIs",
    "body": "Testing POST method",
    "userId": 1
} # these tags are defined by the API
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
'''

# PUT — Update Data
'''
Replaces an entire existing record.
Usually includes the resource ID in the URL.
'''

'''
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated content",
    "userId": 1
}
response = requests.put(url, json=payload)
print(response.status_code)
print(response.json())
'''

# 3. DELETE — Remove - You’re deleting a record.
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)
print(response.status_code)   # 200 or 204 (No Content)
