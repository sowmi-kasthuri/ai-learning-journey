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
r = requests.get('https://httpbin.org/delay/1',timeout=3)
print(r)
