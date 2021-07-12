# Get instance
import instaloader
L = instaloader.Instaloader()

# Login or load session
L.login("look_its_bhagya", "Dipuajay77") # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "look_its_bhagya")

# Print list of followees (who follows me)
    # file = open("bhagya_followers.txt","w")
    # for follower in profile.get_followers():
    #     username = follower.username
    #     file.write(username + "\n")

    # file.close()

# Print list of followees (who i follow)
    # file = open("bhagya_followees.txt","a+")
    # for followee in profile.get_followees():
    #     username = followee.username
    #     file.write(username + "\n")

    # file.close()


with open("bhagya_followees.txt") as f1, open("bhagya_followers.txt") as f2:
    readed1 = f1.readlines()
    readed2 = f2.readlines()

    for eachperson in readed1:
        file = open("notfollowers.txt","a+")
        if eachperson not in readed2:
            file.write(eachperson)
        file.close()