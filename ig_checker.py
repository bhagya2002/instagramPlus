with open("bhagya_followees.txt") as f1, open("bhagya_followers.txt") as f2:
    readed1 = f1.readlines()
    readed2 = f2.readlines()

    for eachperson in readed1:
        file = open("notfollowers.txt","a+")
        if eachperson not in readed2:
            file.write(eachperson)
        file.close()

    
    # for trial in readed1:
    #     if trial in readed2:
    #         file = open("notfollowers.txt","w")
    #         file.write(trial + "\n")
    #         file.close()

    #    for followee in f1.readlines():
           
    #        if followee != readed:
                # file = open("notfollowers.txt","w")
                # username = followee
                # file.write(username + "\n")
                # file.close()