# API Basics playground
import requests

'''
r = requests.get('https://xkcd.com/353/')
print(r)
# print(dir(r)) # attributes and methods of the response object
# print(help(r)) # details of attributes and methods of the response object
print(r.text)
'''
# writing a image in byte format to a file.
'''
r = requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png','wb') as f:
    f.write(r.content)
'''
'''
print(r.status_code) # prints the value of status code from response
print(r.ok) # Binary response true if the status code is 200 or 300
print(r.headers) # prints header information of response
'''

# exercises with httpbin.org
'''
payload = {'page' : 2, 'count' : 25} # define parameters to be used in the request URL
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text) # prints the response from the website
print(r.url)
'''
# exercise for POST
'''
payload = {'username' : 'Sowmi', 'password' : 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)
# print(r.json())
r_dict = r.json()
print(r_dict['form'])
'''

#exercise for auth
'''
r = requests.get('https://httpbin.org/basic-auth/sowmi/testing',auth=('sowmi', 'Testing'))
print(r.text)
print(r)
'''

# handling timeouts
'''
r = requests.get('https://httpbin.org/delay/6',timeout=3)
print(r)
'''

# https://jsonplaceholder.typicode.com/
'''
# Get list of posts
r = requests.get("https://jsonplaceholder.typicode.com/posts")
print(r.status_code)
print(r.json()[0])  # print first post
'''

# Get posts by user
'''
r = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})
print(r.json())
'''

# Create a post (POST request)
'''
payload = {"title" : "Test" , "body" : "Learning API" , "userid" : 1}
r = requests.post("https://jsonplaceholder.typicode.com/posts", json = payload) #json method sends the payload in the body and not in the URL
print(r.json())
'''

# 👉 Site: https://randomuser.me/api/  - Returns randomly generated user data.
# this is for sinle user in response
'''
r = requests.get('https://randomuser.me/api/')
data = r.json()

print(data)
user = data["results"][0]
print(user["name"]["first"], user["name"]["last"])
print(user["location"]["country"])
'''

# get multiple users in response
'''
r = requests.get('https://randomuser.me/api/', params={"results" : 5})
data = r.json()
print(data)

for user in data["results"]:  # Loop through the json response and print the user detail
    name = user["name"]
    gender = user["gender"]
    email = user["email"]
    fname = name["first"] + " " + name["last"]
    print(fname + ' ---' + gender + '---' + email)
'''

# Print details of users from India
'''
r = requests.get('https://randomuser.me/api/', params={"results" : 10, "nat" : "IN,US"})
data = r.json()
print(data)

for user in data["results"]:
    name = user["name"]
    gender = user["gender"]
    email = user["email"]
    fname = name["title"] + ". " + name["first"] + " " + name["last"]
    print(fname + ' --- ' + gender + ' --- ' + email)
'''

# 🐈 3. Cat Facts
# 👉 Site: https://catfact.ninja/fact
for _ in range(5):
    r = requests.get("https://catfact.ninja/fact")
    print(r.json()["fact"])
    print("__________________________________________________")