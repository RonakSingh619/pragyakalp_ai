'''
    Unethical
'''

# -------------------------------- instagrapi --------------------------------
from instagrapi import Client
import json
import time
from datetime import datetime

# Instagram credentials
USERNAME = "alligator.686915"
PASSWORD = "ganeshInsta@69619"
DATA_FILE = "instagram_data.json"

# Initialize Instagram client
cl = Client()
cl.delay_range = [1, 3]  # Avoid rate limiting

def login():
    try:
        cl.login(USERNAME, PASSWORD)
        print("Logged in successfully!")
    except Exception as e:
        print(f"Login failed: {e}")
        if "challenge_required" in str(e):
            handle_challenge()
        return False
    return True

def handle_challenge():
    # Handle Instagram challenge (e.g., email/SMS verification)
    code = input("Enter the verification code sent to your email/SMS: ")
    cl.challenge_resolve(cl.last_json, code)
    print("Challenge resolved, try logging in again.")

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "followers": [],
            "following": [],
            "dms": {},
            "post_likes": {}
        }

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_followers():
    followers = cl.user_followers(cl.user_id)
    return [cl.user_info(user_id).username for user_id in followers.keys()]

def get_following():
    following = cl.user_following(cl.user_id)
    return [cl.user_info(user_id).username for user_id in following.keys()]

def get_dms():
    dms = cl.direct_threads(20)  # Get last 20 threads
    dm_data = {}
    for thread in dms:
        thread_id = thread.id
        messages = cl.direct_messages(thread_id)
        dm_data[thread_id] = {
            "users": [user.username for user in thread.users],
            "messages": [{"sender": msg.user_id, "text": msg.text, "timestamp": msg.timestamp.isoformat()} for msg in messages]
        }
    return dm_data

def get_post_likes():
    posts = cl.user_medias(cl.user_id, 10)  # Last 10 posts
    post_data = {}
    for post in posts:
        likers = cl.media_likers(post.id)
        post_data[post.id] = {
            "code": post.code,
            "likes": [user.username for user in likers]
        }
    return post_data

def track_changes(old_data, new_data):
    print("\n=== Tracking Changes ===")
    
    # Followers changes
    old_followers = set(old_data["followers"])
    new_followers = set(new_data["followers"])
    gained_followers = new_followers - old_followers
    lost_followers = old_followers - new_followers
    if gained_followers:
        print(f"Gained followers: {gained_followers}")
    if lost_followers:
        print(f"Lost followers: {lost_followers}")

    # Following changes
    old_following = set(old_data["following"])
    new_following = set(new_data["following"])
    started_following = new_following - old_following
    stopped_following = old_following - new_following
    if started_following:
        print(f"Started following: {started_following}")
    if stopped_following:
        print(f"Stopped following: {stopped_following}")

    # DMs (new messages)
    for thread_id in new_data["dms"]:
        if thread_id not in old_data["dms"]:
            print(f"New DM thread with {new_data['dms'][thread_id]['users']}")
        else:
            old_msgs = {msg["text"] for msg in old_data["dms"][thread_id]["messages"]}
            new_msgs = {msg["text"] for msg in new_data["dms"][thread_id]["messages"]}
            new_messages = new_msgs - old_msgs
            if new_messages:
                print(f"New messages in thread {thread_id}: {new_messages}")

    # Post likes changes
    for post_id in new_data["post_likes"]:
        if post_id not in old_data["post_likes"]:
            print(f"New post {new_data['post_likes'][post_id]['code']} with likes: {new_data['post_likes'][post_id]['likes']}")
        else:
            old_likes = set(old_data["post_likes"][post_id]["likes"])
            new_likes = set(new_data["post_likes"][post_id]["likes"])
            gained_likes = new_likes - old_likes
            lost_likes = old_likes - new_likes
            if gained_likes:
                print(f"Post {new_data['post_likes'][post_id]['code']} gained likes: {gained_likes}")
            if lost_likes:
                print(f"Post {new_data['post_likes'][post_id]['code']} lost likes: {lost_likes}")

def main():
    if not login():
        return

    # Load previous data
    old_data = load_data()

    # Fetch new data
    new_data = {
        "followers": get_followers(),
        "following": get_following(),
        "dms": get_dms(),
        "post_likes": get_post_likes()
    }

    # Track changes
    track_changes(old_data, new_data)

    # Save new data
    save_data(new_data)
    print(f"\nData saved to {DATA_FILE} at {datetime.now()}")

if __name__ == "__main__":
    main()