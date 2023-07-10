# Import Instaloader and  class from instaloader package
from instaloader import Instaloader, Profile

# Create Instaloader object
ig = Instaloader()

# Taking the instagram username as input from user
username = input("Enter username: ")

# The try-except block that attempts to fetch the profile details of the Instagram user based on the provided username
# If an exception occurs during the retrieval process, it catches the exception and prints the corresponding error message.
try:
    profile = Profile.from_username(ig.context, username)
except Exception as e:
    print(f"Account with the provided username {username} doesn't exist")
    exit()


# Printing the fetched details and storing the profile pic of that account
print(f"Username: {profile.username}")
print(f"Number of Posts Uploaded: {profile.mediacount}")
print(f"{profile.username} is having {profile.followers} followers.")
print(f"{profile.username}is following {profile.followees} people")
print(f"Bio: {profile.biography}")

# Downloading the profile picture of the specified user
ig.download_profile(username, profile_pic_only=True)