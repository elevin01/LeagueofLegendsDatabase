import Errorfun
def Guildsinlol(guildchoice):
    match guildchoice:
        case 1:
            print("\nEnter name of the guild: ")
            guildname = str(input()).strip()
            #

        case 2:
            print("\nPlease add all the guild information below to add a guild")
            print("\nEnter guild name: ")
            guildname = str(input()).strip()
            print("Enter guild creator name: ")
            guildcreat = str(input()).strip()
            while True:
                print("Enter guild creator id")
                creatid = str(input()).strip()
                if len(creatid) == 4:
                    break
                else:
                    print("ID's should only be 4 characters long. Try again")
            print("Enter guild level: ")
            try:
                guildlvl = int(input())
            except:
                Errorfun.Errorcase()

            #

        case other:
            Errorfun.Errorswitch()

