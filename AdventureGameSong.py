#Skylin Song
#10/3/19
#adventureCode
print("level 1, Get through the cave system.\nStart GAME: You look in your hand and you see a broadsword")
swordName = input("hmmm betsy doesnt fit, what do you name it: ")
swordName = str(swordName)
print ("You have named your broadsword",swordName,)

print("As you stand up you see two rocky and dark caves leading down pitch dark pathways")
choice1 = input("Cave entrance One or Two:")
choice1 = choice1.lower()

if choice1 == "one":
    print("The cave is dark and cold and out of nowhere you hear a deathly moan and the smack of bare feet on the cave floor getting louder and louder")
    print ("Out of the darkness a zombie appears")
    choice2 = input("Do you attack the zombie or run:")
    choice2 = choice2.lower()

    if choice2 == "attack the zombie":
        print("You run at it and swing", swordName)
        choice3 = input("quick how many times do you swing your sword:")
        choice3 = int(choice3)

        if choice3>5:
            print("You regain your senses and in the distant you see an old man who offers you food and water. \nYou eat the food")
            choice4 = input ("You have to pay for it now, how many gold pieces do you give him:")
            choice4 = float (choice4)

            if choice4 >=10:
                 print ("the man takes you to the exit of the cave very happy with the tip, Congratulations you beat level 1")
            elif (choice4 >5) and (choice4 < 10):
                print("The man is insulted by the amount you have offered. He turns around and disapears into the darkness. You wind up getting lost in the cave and die of dehydration")
                print ("GAME OVER")
            else:
                print("You have nothing?, he says. After you have eaten my food and drank my valuable water. He pulls out a sword and your vision goes dark")
                print ("GAME OVER")
        else:
            print ("Your sword gets stuck in the zombie and it bites you")
            print ("GAME OVER")

    elif choice2 == "run":
        print("The zombie catches you in 3 strides and eats you alive")
        print ("GAME OVER")
    else:
        print ("You didnt make a decision in time, the zombie jumps on you and eats your face")
        print ("GAME OVER")

elif choice1 == "two":
    print ("You walk into the second entrance and a stalagmite falls from the roof slicing right though you")
    print ("GAME OVER")
else:
    print("You walk into a bears den and get viciously torn apart.")
    print("GAME OVER")

