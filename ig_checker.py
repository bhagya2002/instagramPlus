# get a list of people who dont follow you
with open("followees.txt") as f1, open("followers.txt") as f2:
    readed1 = f1.readlines()
    readed2 = f2.readlines()

    for eachperson in readed1:
        file = open("notfollowers.txt","a+")
        if eachperson not in readed2:
            file.write(eachperson)
        file.close()