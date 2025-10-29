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

# Define response code handling
def handle_response(response,action):
    """
    Interpret HTTP response codes, log a readable message, and return parsed JSON when present.
    Returns (data, status_code) where data is parsed JSON or None.

    """
    code = response.status_code
    details = f"Status : {code}"

    # Success with JSON body
    if code in (200,201):
        try:
            data = response.json()
            msg = f"{action.upper()} SUCCESS ({code}) - {data}"
            log_action(action, "SUCCESS", f"{details} - JSON returned")
            print(f"{action.upper()} → {code} ✅")
            return data, code
        except ValueError:
            # No JSON in body despite 200/201
            msg = f"{action.upper()} SUCCESS ({code}) - No JSON"
            log_action(action, "SUCCESS_NO_JSON", details)
            print(f"{action.upper()} → {code} ✅ (no JSON)")
            return None, code
    
    # No Content (commonly DELETE)
    if code == 204:
        log_action(action, "SUCCESS_NO_CONTENT", details)
        print(f"{action.upper()} → {code} ✅ No Content")
        return None, code
    
    # Client errors
    if code == 400:
        log_action(action, "FAILED_BAD_REQUEST", details)
        print(f"{action.upper()} → {code} ⚠️ Bad Request")
        return None, code
    if code == 401:
        log_action(action, "FAILED_UNAUTHORIZED", details)
        print(f"{action.upper()} → {code} 🚫 Unauthorized")
        return None, code
    if code == 403:
        log_action(action, "FAILED_FORBIDDEN", details)
        print(f"{action.upper()} → {code} 🚫 Forbidden")
        return None, code
    if code == 404:
        log_action(action, "FAILED_NOT_FOUND", details)
        print(f"{action.upper()} → {code} ❌ Not Found")
        return None, code
    
    # Server errors
    if code >= 500:
        # include response.text to help debug server-side issues
        log_action(action, "FAILED_SERVER_ERROR", f"{details} - {response.text[:200]}")
        print(f"{action.upper()} → {code} 💀 Server Error")
        return None, code

    # Fallback for other codes
    log_action(action, "FAILED_UNKNOWN", details)
    print(f"{action.upper()} → {code} ⚠️")
    return None, code

# Define create post
def create_post(title,body,user_id):
    payload = {'title':title, 'body':body, 'id':user_id}
    try:
        response = requests.post(BASE_URL,json=payload,timeout=5)
        data, code = handle_response(response, "CREATE")
        if data:
            # Log with the returned id when present
            log_action("CREATE", "SUCCESS", f"Post ID {data.get('id')} - HTTP {code}")
        return data or {}
        
    except Exception as e:
        print("❌ Create failed:", e)
        log_action("CREATE", "FAILED_EXCEPTION", str(e))
        return {}
    
# Define retrieve post
def get_posts():
    try:
        response = requests.get(BASE_URL,timeout=5)
        data, code = handle_response(response, "READ")
        if data is None:
            print("⚠️ No posts returned.")
            return []
            print(f"📄 Total posts: {len(data)}")
            return data
    except requests.exceptions.RequestException as e:
            print("❌ Read failed:", e)
            log_action("READ", "FAILED_EXCEPTION", str(e))
            return []

# Define Update post
def update_post(post_id,title,body,user_id):
    payload = {'title':title, 'body':body, 'userid':user_id}
    try:
        response = requests.put(f"{BASE_URL}/{post_id}", json=payload,timeout=5)
        data, code = handle_response(response, "UPDATE")
        if code in (200, 201) and data:
            log_action("UPDATE", "SUCCESS", f"Post ID {post_id} - HTTP {code}")
        return response
    except requests.exceptions.RequestException as e:
        print("❌ Update failed:", e)
        log_action("UPDATE", "FAILED_EXCEPTION", str(e))
        return None


# Define Delete post
def delete_post(post_id):
    try:
        response = requests.delete(f"{BASE_URL}/{post_id}", timeout=5)
        data, code = handle_response(response, "DELETE")
        if code == 200 or code == 204:
            log_action("DELETE", "SUCCESS", f"Post ID {post_id} - HTTP {code}")
        return response
    except requests.exceptions.RequestException as e:
        print("❌ Delete failed:", e)
        log_action("DELETE", "FAILED_EXCEPTION", str(e))
        return None

# Define main
if __name__ == '__main__':
    logging_note = f"Starting run at {datetime.now().isoformat()}"
    log_action("RUN", "START", logging_note)
    
    # create
    new_post = create_post("Learning APIs", "Testing POST method",1)
    post_id = new_post.get("id", 1)

    # Read
    get_posts()

    # Update
    update_post(post_id,"Updated Title","Updated Content",1)

    # Delete
    delete_post(post_id)
    log_action("RUN", "END", f"Completed at {datetime.now().isoformat()}")
    print("Done.")