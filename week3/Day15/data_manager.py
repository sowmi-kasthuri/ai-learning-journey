import requests
from datetime import datetime

BASE_URL = "https://jsonplaceholder.typicode.com/posts"
LOG_FILE = "crud_log.txt"

# Define log capture
def log_action(action, status, details=""):
    """Write timestamped log entries to crud_log.txt"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {action} - {status} - {details}\n")

# Define create post
def create_post(title,body,id):
    payload = {'title':title, 'body':body, 'id':id}
    try:
        response = requests.post(BASE_URL,json=payload,timeout=5)
        response.raise_for_status()
        data = response.json()
        print("✅ Created:", data)
        log_action("CREATE", "SUCCESS", f"Post ID {data.get('id')}")
        return data
    except Exception as e:
        print("❌ Create failed:", e)
        log_action("CREATE", "FAILED", str(e))
        return {}
    
# Define retrieve post
def get_posts():
    response = requests.get(BASE_URL)
    print(f"📄 Total posts: {len(response.json())}")
    return response.json()

# Define Update post
def update_post(post_id,title,body,user_id):
    payload = {'title':title, 'body':body, 'userid':user_id}
    response = requests.put(f"{BASE_URL}/{post_id}", json=payload)
    try:
        data = response.json()
        print("✏️ Updated:", data)
        log_action("UPDATE", "SUCCESS", f"Post ID {post_id}")
    except ValueError:
        print(f"✏️ Updated Post ID {post_id} successfully (no JSON returned)")
        log_action("UPDATE", "SUCCESS_NO_JSON", f"Post ID {post_id}")
    return response
    
# Define Delete post
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/{post_id}")
    try:
        data = response.json()
        print(f"🗑️ Deleted:", data)
        log_action("DELETE", "SUCCESS", f"Post ID {post_id} - Status {response.status_code}")
    except ValueError:
        print(f"🗑️ Deleted Post ID {post_id} successfully (no JSON returned)")
        log_action("DELETE", "SUCCESS_NO_JSON", f"Post ID {post_id}")
    return response

# Define main
if __name__ == '__main__':
    # create
    new_post = create_post("Learning APIs", "Testing POST method",1)
    post_id = new_post.get("id", 1)

    # Read
    get_posts()

    # Update
    update_post(post_id,"Updated Title","Updated Content",1)

    # Delete
    delete_post(post_id)
