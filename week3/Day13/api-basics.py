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
'''
for _ in range(5):
    r = requests.get("https://catfact.ninja/fact")
    print(r.json()["fact"])
    print("__________________________________________________")
'''

'''
🧩 Exercise: RandomUser Filter & Safe Access

Write a short script that:
Calls the RandomUser API for 5 users from India.
Checks if results exists and is not empty.
Loops through the users.
Prints each user’s full name (first last) and country.
If either name or location is missing, prints "Data missing" instead of crashing.

💡 Example Output
Ravi Kumar - India
Anita Menon - India
Data missing
'''
'''
r = requests.get('https://randomuser.me/api/', params={"results" : 100, "nat" : "IN,US"})
data = r.json()


if data.get("results"):  # check for empty results else give key error
    for user in data["results"]:
        name = user.get('name', {})
        location = user.get('location', {})
        fname = name.get('first', 'unknown')
        lname = name.get('last', 'unknown')
        country = location.get('country', 'Data Missing')
        print(fname + ' ' + lname + ' - ' + country)
else:
    print("No results found")
'''

# combine .get() and try..except for error handling
'''
if data.get('results'):
    for user in data['results']:
        try:

            # safely get the name and location dict.  Default to empty {} if no data available
            name_info = user.get('name', {})
            location_info = user.get('location', {})

            # get fname, lname and country
            fname = name_info.get('first', 'unknown')
            lname = name_info.get('last', 'unknown')
            country = location_info.get('country', 'unknown')

            #print name and country
            print(f'{fname} {lname} - {country}')
        
        except KeyError as e: # handling missing keys
            print(f"Missing Keys : {e}")
        
        except Exception as e: #handling random errors
            print(f"Unexpected error : {e}")
'''

'''
Use Random User API:
# Get 20 users, filter only from USA
# Extract: name, email, age, location
# Only show people over 30


r = requests.get("https://randomuser.me/api/", params = {"results" : 20 , "nat" : "IN,US"})
data = r.json()
# print(data)

if data.get('results'):
    for user in data['results']:
        try:
            name_dict = user.get('name', {})
            location_dict = user.get('location', {})
            age_dict = user.get('dob', {})

            # get fname, lname and country
            fname = name_dict.get('first', 'unknown')
            lname = name_dict.get('last', 'unknown')
            country = location_dict.get('country', 'unknown')
            age = age_dict.get('age')
            email = user.get('email', 'unknown')

            # print name, email, age, location
            print(f'Name: - {fname} {lname}; Age: - {age}; Country: - {country}; Email: - {email}')
        
        except KeyError as e:
            print(f'Missing Keys - {e}')
        
        except Exception as e:
            print(f'Unknown error - {e}')

'''

'''
Use JSONPlaceholder:
# Get all posts
# Find posts by userId=1
# Count comments per post
'''
'''
Method - 1 make multiple comment call for each post 

# 1. Get all posts
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()

#2. filter posts by userid = 1
user_posts = [post for post in posts if post['userId'] == 1]

#3. For each post count its comments
for post in user_posts:
     post_id = post["id"]
    # Get comments for this specific post
     comments = requests.get("https://jsonplaceholder.typicode.com/comments", params= {"postId" : post_id}).json()
     count = len(comments)
     print(f"Post ID {post_id} : {count} Comments")
'''

# Method 2 -  1 Post call and 1 comment call.
#1. Make the posts and comments call once
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
comments = requests.get("https://jsonplaceholder.typicode.com/comments").json()

# 2. filter posts for userid = 1
user_posts = [post for post in posts if post["userId"] == 1]

# 3. count comments per post
comment_count = {}
for comment in comments:
    pid = comment["postId"]
    comment_count[pid] = comment_count.get(pid,0) + 1 # Get comment count for specific PID else initialise

#4. Print PID, Post and Comment count
for post in user_posts:
    pid = post["id"]
    title = post["title"]
    count = comment_count.get(pid,0)
    print(f"PostID : {pid} : Title : {title} : Count : {count}")

