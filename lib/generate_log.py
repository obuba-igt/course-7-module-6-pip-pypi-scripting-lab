from datetime import datetime
import requests


def fetch_data():
    try:
        r = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return {}


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # TEST EXPECTS THIS FORMAT: log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as f:
        for entry in data:
            f.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    post = fetch_data()
    logs = ["User logged in",
            f"Post: {post.get('title', 'fallback')}", "Report exported"]
    generate_log(logs)
