userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

if userReply == "stamps" or userReply == "stm":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope" or userReply == "evlp":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy" or userReply == "cp":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
