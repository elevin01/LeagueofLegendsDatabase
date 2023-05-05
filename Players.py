import Errorfun
import tkinter
from tkinter import messagebox
def Players(playerchoice, root):
    for widget in root.winfo_children():
        widget.destroy()
    playerlabel = tkinter.Label(root, text= "Player Menu ", font=("Ariel", 20))
    playerlabel.pack(pady=15)
    match playerchoice:
        case 1:
            playername = tkinter.Label(root, text= "Enter the name of the player name: ", font=("Ariel", 16))
            playername.pack(pady=10)
            name_input = tkinter.Entry(root)
            name_input.pack()
            submit_button = tkinter.Button(root, text="Submit", command=lambda : print(name_input.get()))
            submit_button.pack()

        case 2:
            playerrank = tkinter.Label(root, text="Player List")
            playerrank.pack()

        case 3:
            """
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
            """
            root.geometry("600x500")
            playername = tkinter.Label(root, text="Enter the name of the player name: ")
            playername.pack(pady=10)
            name_input = tkinter.Entry(root)
            name_input.pack()
            playerid = tkinter.Label(root, text="Enter player id: ")
            playerid.pack(pady=10)
            id_input = tkinter.Entry(root)
            id_input.pack()
            lane_choices = {
                            "Top Lane (Baron Lane)": "top",
                            "Mid Lane": "mid",
                            "Bot Lane (Dragon Lane - ADC)": "duo",
                            "Support Lane (Dragon Lane - Support)": "sup",
                            "Jungle": "jg"
                            }
            lane_choice = tkinter.StringVar(root)
            lane_choice.set("Select a lane")
            dropdown = tkinter.OptionMenu(root, lane_choice, *lane_choices.keys())
            dropdown.pack(pady=10)
            rank_choices = [
                     "Iron",
                     "Bronze",
                     "Silver",
                     "Gold",
                     "Platinum",
                     "Diamond",
                     "Master",
                     "Grandmaster",
                     "Challenger"
                ]
            rank_choice = tkinter.StringVar(root)
            rank_choice.set("Select a rank")
            dropdown = tkinter.OptionMenu(root, rank_choice, *rank_choices)
            dropdown.pack(pady=10)
            playerlvl = tkinter.Label(root, text="Enter Player Level: ")
            playerlvl.pack(pady=10)
            lvl_input = tkinter.Entry(root)
            lvl_input.pack()
            submit_button2 = tkinter.Button(root, text="Submit", command=lambda: addplaya())
            submit_button2.pack(pady=20)
            def addplaya():
                player_name = name_input.get()
                player_name = str(player_name)
                if not player_name:
                    Errorfun.Errorswitch()
                    return
                player_id = id_input.get()
                player_id = str(player_id)
                if not len(player_id) == 4:
                    messagebox.showerror("Error", "Player ID length cannot exceed 4 characters")
                    return
                player_lane = lane_choice.get()
                player_lane = str(player_lane)
                if not player_lane:
                    Errorfun.Errorswitch()
                    return
                player_rank = rank_choice.get()
                player_rank = str(player_rank)
                if not player_rank:
                    Errorfun.Errorswitch()
                    return
                player_lvl = lvl_input.get()
                face = False
                try:
                    player_lvl = int(player_lvl)
                    face = False
                except:
                   messagebox.showerror("Error", "Player level must be a number")
                   face = True
                if face:
                    return
        case 4:
            root.geometry("600x500")
            player_namelabel = tkinter.Label(root, text="Edit Player Information", font=("Ariel", 16))
            player_namelabel.pack(pady=15)
            player_ed1 = tkinter.Label(root,text="Enter Player name: ")
            player_ed1.pack(pady=10)
            player_name = tkinter.Entry(root)
            player_name.pack()
            player_ed2 = tkinter.Label(root,text="Enter Player ID: ")
            player_ed2.pack(pady=10)
            player_id = tkinter.Entry(root)
            player_id.pack()
            submit_button2 = tkinter.Button(root, text="Submit", command=lambda: edit01())
            submit_button2.pack(pady=20)
            def edit01():
                #authentication goes here
                player_ed1 = tkinter.Label(root, text="Code not written yet ")
                player_ed1.pack(pady=10)
                Errorfun.Qcase()


        case other:
            Errorfun.Errorcase()
            quit()









