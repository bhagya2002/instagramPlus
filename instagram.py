# Get instance
import instaloader
L = instaloader.Instaloader()

# Login or load session
L.login('USERNAME', "PASSWORD") # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "USERNAME")

# Print list of followees (who follows me)
file = open("followees.txt","w")
for follower in profile.get_followers():
    username = follower.username
    file.write(username + "\n")

file.close()

# Print list of followers (who i follow)
file = open("followers.txt","a+")
for followee in profile.get_followees():
    username = followee.username
    file.write(username + "\n")
        
file.close()