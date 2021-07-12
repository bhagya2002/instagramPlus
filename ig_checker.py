with open("FILE1_NAME") as f1, open("FILE2_NAME") as f2:
    readed1 = f1.readlines()
    readed2 = f2.readlines()

    for eachperson in readed1:
        file = open("notfollowers.txt","a+")
        if eachperson not in readed2:
            file.write(eachperson)
        file.close()