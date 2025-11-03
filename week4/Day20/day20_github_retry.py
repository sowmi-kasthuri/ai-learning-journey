import requests, logging, time

#configure logging
logging.basicConfig(
    filename="github_retry.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define callgithubapi function
def call_github_api(username, retries=3, backoff=2):
    url = f"https://api.github.com/users/{username}/repos"

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                print(f"Fetched {len(data)} repos successfully")
                logging.info(f"Fetched {len(data)} repos successfully")
                
                for repos in data:
                    print(repos['name'])
                break
            else:
                print(f" Error : {response.status_code} : {response.text}")
                logging.error(f" Error : {response.status_code} : {response.text}")

        except requests.exceptions.RequestException as err:
            print(f"Error : {err}")
            logging.error(f"Error : {err}")
        
        if attempt <  retries:
            print(f"retrying in {backoff} seconds")
            logging.info(f"retrying in {backoff} seconds")
            time.sleep(backoff)
            backoff *= 2
        else:
            print("Failed after multiple attempts")
            logging.error("Failed after multiple attempts")

#define main
if __name__ == "__main__":
    username = input("Enter Github Username : ")
    call_github_api(username)