import tkinter
import Champions
import Items
import Players
import Guilds
import Errorfun


def main():
    print("League of Legends Wiki")
    print("----------------------")
    print("\n1. Champions\n2. Items\n3. Players\n4. Guilds")
    print("Choose one of the above options: ")
    # trying to add try here and too lazy to indent everything below
    try:
        choice = int(input())
        match choice:
            # this whole thing can be a separate function but well whatever
            case 1:
                print("You have chosen Champions. Select from the options below\n")
                print("1. Search champion by name")
                print("2. Search champion by lane")
                print("\nEnter your choice: ")
                try:
                    champchoice = int(input())
                    Champions.champions(champchoice)
                except:
                    Errorfun.Errorcase()

            case 2:
                print("You have chosen Items. Select from the options below\n")
                print("\n1. Search Item by name")
                print("2. Sort Item by type")
                print("3. Sort Item by class")
                print("\nEnter your choice: ")
                try:
                    itemchoice = int(input())
                    Items.Item(itemchoice)
                except:
                    Errorfun.Errorcase()

            case 3:
                print("You have chosen Players. Select from the options below\n")
                print("\n1. Search Player by name")
                print("2. Search Player by rank ")
                print("3. Add Player")
                try:
                    playerchoice = int(input())
                    Players.Players(playerchoice)
                except:
                    Errorfun.Errorcase()

            case 4:
                print("You have chosen Guilds. Select from the options below\n")
                print("\n1. Search Guild by name")
                print("2. Add Guild")
                try:
                    guildchoice = int(input())
                    Guilds.Guildsinlol(guildchoice)
                except:
                    Errorfun.Errorcase()

            case other:
                    Errorfun.Errorswitch()
    except:
        Errorfun.Errorcase()


while True:
    main()
    facts = False
    print("Enter 0 to quit ")
    try:
        mainchoice = int(input())
        if mainchoice == 0:
            facts = True
    except:
        print()
    if facts:
        break





