player = input("Enter player name: ")
health = 100
location = "forest"
def show_stat(name,health,location):
    return f"Hi {name}, you are in the {location} with health {health}."

show_stat(player,health,location)

print("\nYou are walking in a forest. There are 2 pathways:\nR(right)\nL(left).")
choice = input("\nWhich one will you choose?: ")
if choice == "R":
    print("\nYou choose to go right.")
    choice = input("\nWhile walking, you saw a woman. Do you talk to her? Y/N: ")
    if choice == "Y":
        health -= 10
        choice = input("\nWhile talking to the woman, she offered you an apple. Do you take it? Y/N: ")
        if choice == "Y":
            health -= 10
            print("\nA. Hide the apple inside your bag.\nB. Bite the apple.")
            choice = input("\nWhat will you do with the apple?: ")
            if choice == "A":
                health += 10
                print("\nYou walked away safely!")
                print("\nWhile walking, you saw a lion.\nA. You walked towards the lion\nB. You ignored the lion")
                choice = input("\nWhat will you do?: ")
                if choice == "A":
                    health = health - health
                    print("\nThe lion ate you.\nGame Over")
                    print("\n"+show_stat(player,health,location)+"\n")
                elif choice == "B":
                    health += 10
                    print("You walked away safely!")
                    print("\n"+show_stat(player,health,location)+"\n")
                else:
                    print("\nThat is not in the choices. Restart game.")
            elif choice == "B":
                health = health - health
                print("\nThe apple is poison and you die.\nGame Over")
                print("\n"+show_stat(player,health,location)+"\n")
            else:
                print("\nThat is not in the choices. Restart game.")
        elif choice == "N":
            health += 10
            print("\nYou politely reject the apple and you walked away safely!")
            print("\nWhile walking, you saw a lion.\nA. You walked towards the lion\nB. You ignored the lion")
            choice = input("\nWhat will you do?: ")
            if choice == "A":
                health = health - health
                print("\nThe lion ate you.\nGame Over")
                print("\n"+show_stat(player,health,location)+"\n")
            elif choice == "B":
                health += 10
                print("You walked away safely!")
                print("\n"+show_stat(player,health,location)+"\n")
            else:
                print("\nThat is not in the choices. Restart game.")
        else:
            print("\nThat is not in the choices. Restart game.")
    elif choice == "N":
        health += 10
        print("\nYou passed by the woman and she approached you.")
        choice = input("\nShe asked if you want an apple. Y/N: ")
        if choice == "Y":
            health -= 10
            print("\nA. Hide the apple inside your bag.\nB. Bite the apple.")
            choice = input("\nWhat will you do with the apple?: ")
            if choice == "A":
                health += 10
                print("\nYou walked away safely!")
                print("\nWhile walking, you saw a lion.\nA. You walked towards the lion\nB. You ignored the lion")
                choice = input("\nWhat will you do?: ")
                if choice == "A":
                    health = health - health
                    print("\nThe lion ate you.\nGame Over")
                    print("\n"+show_stat(player,health,location)+"\n")
                elif choice == "B":
                    health += 10
                    print("You walked away safely!")
                    print("\n"+show_stat(player,health,location)+"\n")
                else:
                    print("\nThat is not in the choices. Restart game.")
            elif choice == "B":
                health = health - health
                print("\nThe apple is poison and you die.\nGame Over")
                print("\n"+show_stat(player,health,location)+"\n")
            else:
                print("\nThat is not in the choices. Restart game.")
        elif choice == "N":
            health += 10
            print("\nYou politely reject the apple and you walked away safely!")
            print("\nWhile walking, you saw a lion.\nA. You walked towards the lion\nB. You ignored the lion")
            choice = input("\nWhat will you do?: ")
            if choice == "A":
                health = health - health
                print("\nThe lion ate you.\nGame Over")
                print("\n"+show_stat(player,health,location)+"\n")
            elif choice == "B":
                health += 10
                print("You walked away safely!")
                print("\n"+show_stat(player,health,location)+"\n")
            else:
                print("\nThat is not in the choices. Restart game.")
        else:
                print("\nThat is not in the choices. Restart game.")
    else:
        print("\nThat is not in the choices. Restart game.") 
elif choice == "L":
    print("\nYou choose to go left.\nWhile walking, you saw 2 box.\nA. Box1\nB. Box2")
    choice = input("\nWhich one will you choose?: ")
    if choice == "A":
        health -= 10
        print("\nThere is a banana.\nYou grabbed the banana and continue walking.")
        print("\nWhile walking, you saw a bear.\nA. Run\nB. Fight")
        choice = input("\nWhat will you do?: ")
        if choice == "A":
            health += 10
            print("\nYou escaped the bear safely!")
            print("\n"+show_stat(player,health,location)+"\n")
        elif choice == "B":
            health = health - health
            print("\nThe bear ate you.\nGame Over.")
            print("\n"+show_stat(player,health,location)+"\n")
        else:
            print("\nThat is not in the choices. Restart game.")
    elif choice == "B":
        health += 10
        print("\nThere is a sword.\nYou grabbed the sword and continue walking.")
        print("\nWhile walking, you saw a bear.\nA. Run\nB. Fight")
        choice = input("\nWhat will you do?: ")
        if choice == "A":
            health = health - health
            print("\nYou tripped while running and you die.\nGame Over.")
            print("\n"+show_stat(player,health,location)+"\n")
        elif choice == "B":
            health += 10
            print("\nYou killed the bear and walked away safely!")
            print("\n"+show_stat(player,health,location)+"\n")
        else:
            print("\nThat is not in the choices. Restart game.")
    else:
        print("\nThat is not in the choices. Restart game.")
else:
    print("\nThat is not in the choices. Restart game.")
