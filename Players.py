import Errorfun
def Players(playerchoice):
    match playerchoice:
        case 1:
            print("Enter the name of the player name: ")
            playername = str(input()).strip()

        case 2:
            print("\nPlayer List\n\n")

        case 3:
            print("Enter player username: ")
            playeruser = str(input()).strip()
            while True:
                print("Enter player id")
                playerid = str(input()).strip()
                if len(playerid) == 4:
                    break
                else:
                    print("ID's should only be 4 characters long. Try again")

            lane_mapping = {
                    "jungle": "jungle",
                    "jg": "jungle",
                    "top": "top",
                    "baron": "top",
                    "baron lane": "top",
                    "mid": "mid",
                    "mid lane": "mid",
                    "duo": "bottom",
                    "adc": "bottom",
                    "bottom": "bottom",
                    "dragon lane": "bottom",
                    "bot": "bottom",
                    "sup": "support",
                    "support": "support"
                }
            while True:
                print("Enter player main_lane: ")
                playerlane = str(input()).lower().strip()
                if playerlane in lane_mapping:
                    playerlane = lane_mapping[playerlane]
                    break
                else:
                    print("Invalid input. Choose from:")
                    print("\n Top\n Mid\n Jungle\n Duo\n Support\n")

            rank_mapping = {
                    "1": "Iron",
                    "2": "Bronze",
                    "3": "Silver",
                    "4": "Gold",
                    "5": "Platinum",
                    "6": "Diamond",
                    "7": "Master",
                    "8": "Grandmaster",
                    "9": "Challenger"
                }
            while True:
                print("\nEnter player rank from the options below")
                print(
                        "\n1. Iron\n2. Bronze\n3. Silver\n4. Gold\n5. Platinum\n6. Diamond\n7. Master\n8. Grandmaster\n9. Challenger")
                try:
                    user_input = input().strip()
                    if user_input in rank_mapping:
                        playerrank = rank_mapping[user_input]
                        print("You have chosen: ", rank_mapping[user_input])
                        break
                    else:
                       Errorfun.Errorswitch()
                except:
                    Errorfun.Errorcase()

            print("Enter player level: ")
            try:
                playerlevel = int(input())
            except:
                Errorfun.Errorcase()






