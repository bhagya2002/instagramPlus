# Get instance
import instaloader
L = instaloader.Instaloader()

# Login or load session
L.login("USERNAME", "PASSWORD") # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "PROFILE USER")

# Print list of followees (who follows me)
    # file = open("FILENAME","w")
    # for follower in profile.get_followers():
    #     username = follower.username
    #     file.write(username + "\n")

    # file.close()

# Print list of followees (who i follow)
    # file = open("FILENAME.txt","a+")
    # for followee in profile.get_followees():
    #     username = followee.username
    #     file.write(username + "\n")

    # file.close()