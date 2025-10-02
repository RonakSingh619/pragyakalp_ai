import instaloader
from datetime import datetime

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Optional: Log in to access your own account's private data (remove if only public data is needed)
# Replace 'YOUR_USERNAME' and 'YOUR_PASSWORD' with your credentials
try:
    L.login('alligator.686915', 'ganeshInsta@69619')
    print("Logged in successfully!")
except Exception as e:
    print(f"Login failed: {e}. Proceeding without login for public data.")

# Specify the Instagram profile to analyze (replace with your username)
username = 'alligator.686915'

# Load the profile
try:
    profile = instaloader.Profile.from_username(L.context, username)
except Exception as e:
    print(f"Error loading profile: {e}")
    exit()

# Get basic profile info
followers = profile.followers
following = profile.followees
post_count = profile.mediacount
bio = profile.biography
is_private = profile.is_private

# Print basic info
print(f"\nProfile: {profile.username}")
print(f"Followers: {followers}")
print(f"Following: {following}")
print(f"Total Posts: {post_count}")
print(f"Bio: {bio}")
print(f"Private Account: {is_private}")

# Get likes and other details from recent posts (limited to avoid rate limits)
total_likes = 0
total_comments = 0
posts_analyzed = 0
max_posts = 10  # Limit to 10 posts to stay ethical and avoid overloading

print("\nAnalyzing recent posts...")
for post in profile.get_posts():
    if posts_analyzed >= max_posts:
        break
    total_likes += post.likes
    total_comments += post.comments
    posts_analyzed += 1
    print(f"Post {posts_analyzed}: {post.likes} likes, {post.comments} comments, Date: {post.date}")

# Summary of posts
if posts_analyzed > 0:
    print(f"\nSummary of {posts_analyzed} posts:")
    print(f"Total Likes: {total_likes}")
    print(f"Total Comments: {total_comments}")
    print(f"Average Likes per Post: {total_likes / posts_analyzed:.2f}")
    print(f"Average Comments per Post: {total_comments / posts_analyzed:.2f}")
else:
    print("No posts found or unable to access posts.")

# Optional: Save data to a file
with open(f"{username}_stats.txt", "w") as f:
    f.write(f"Profile: {username}\n")
    f.write(f"Followers: {followers}\n")
    f.write(f"Following: {following}\n")
    f.write(f"Total Posts: {post_count}\n")
    f.write(f"Total Likes (last {posts_analyzed} posts): {total_likes}\n")
    f.write(f"Total Comments (last {posts_analyzed} posts): {total_comments}\n")
    f.write(f"Date: {datetime.now()}\n")
print(f"\nData saved to {username}_stats.txt")