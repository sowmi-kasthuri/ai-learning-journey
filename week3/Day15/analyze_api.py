# 🧩 Challenge — Fetch, Filter, and Analyze API Data with Pandas 
#  You’ll use this public API: - https://jsonplaceholder.typicode.com/posts
# jsonplaceholder.typicode.com is a free, public, no-auth mock API used for learning and testing. You can call it directly with plain requests.get() — no headers, no .env, no tokens.

'''
Task:
Fetch all posts.
Convert them into a Pandas DataFrame.
Filter posts where userId == 1.
Display only id and title columns.
Print how many posts that user has.
'''
import pandas as pd
import requests
url = "https://jsonplaceholder.typicode.com/comments"

# STEP 1 - Fetch all data and convert to data frame
# call the API and check status code
response = requests.get(url)
print(response.status_code)

# check response
if response.status_code != 200:
    print("❌ Error:", response.status_code, response.text)


# parse json response and convert to pandas
data = response.json()
posts = pd.DataFrame(data)

# STEP 2 - Filter
# print(posts)
post2_df = posts[posts["postId"] == 2]
print(f'Posts for postId')
print('--------------------------------------------')
print(post2_df)
print('--------------------------------------------')
print(f'Count of number of comments : {len(post2_df)}')
print('--------------------------------------------')
print(f'First Comments email : - {post2_df.iloc[0]['email']}')
print('--------------------------------------------')

# STEP 3 - Analyze
# Group by postId and count how many comments per post
comments_count = posts['postId'].value_counts()

# Print top 5 posts by comment count
print(comments_count.head())

# Find the postId with maximum comments
most_commented_post = comments_count.idxmax()
max_comments = comments_count.max()

print(f"Post {most_commented_post} has the most comments ({max_comments}).")

# Step 4 — Save filtered results
post2_df.to_csv("post2_comments.csv", index=False)
print("Saved post2_comments.csv successfully.")