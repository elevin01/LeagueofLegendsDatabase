import Errorfun
import tkinter
"""
def champions(champchoice, root):
    match champchoice:
        case 1:
            print("Enter the champion name: ")
            champname = input()
            Champsearch(champname)

        case 2:
            print("Choose the lane you want to view from below")
            print("1. Top Lane (Baron Lane) ")
            print("2. Mid Lane ")
            print("3. Bot Lane (Dragon Lane - ADC)")
            print("4. Support Lane (Dragon Lane - Support)")
            print("5. Jungle ")
            print("\nEnter your choice: ")
            try:
                lanechoice = int(input())
                Lanesearch(lanechoice)
                # lanesort(lanechoice) #function that will run this
            except:
                Errorfun.Errorcase()

        case other:
            Errorfun.Errorswitch()
"""
def champions(champchoice, root):
    for widget in root.winfo_children():
        widget.destroy()
    champmenu = tkinter.Label(root, text="Champion Selection", font=("Roboto", 20))
    champmenu.pack(pady=15)
    match champchoice:
        case 1:
            champ_label = tkinter.Label(root, text="Enter the champion name: ", font=("Ariel", 16))
            champ_label.pack(pady=10)
            champ_entry = tkinter.Entry(root)
            champ_entry.pack()
            submit_button = tkinter.Button(root, text="Submit", command=lambda: Champsearch(champ_entry.get()))
            submit_button.pack()

        case 2:
            lane_label = tkinter.Label(root, text="\n\nChoose the lane you want to view from below", font=("Ariel",16))
            lane_label.pack(pady=10)
            lane_choices = {"Top Lane (Baron Lane)": "top", "Mid Lane": "mid", "Bot Lane (Dragon Lane - ADC)": "bot",
                            "Support (Dragon Lane - Support)": "sup", "Jungle": "jg"}
            lane_choice = tkinter.StringVar(root)
            lane_choice.set("Select a lane")
            dropdown = tkinter.OptionMenu(root, lane_choice, *lane_choices.keys())
            dropdown.pack()
            submit_button = tkinter.Button(root, text="Submit", command=lambda: Lanesearch(lane_choices[lane_choice.get()]))
            submit_button.pack()

        case other:
            Errorfun.Errorswitch()

def Champsearch(champname):
    #
    champ = str(champname).strip()
    quit()


def Lanesearch(lanechoice):
    lane = ""
    match lanechoice:
        case "top":
            print("\tTop Lane (Baron Lane)")
            lane = "top"
            #
        case "mid":
            print("\tMid Lane")
            lane = "mid"
            #
        case "duo":
            print("\tBot Lane (Dragon Lane - ADC)")
            lane = "duo"
            #
        case "sup":
            print("\tSupport Lane (Dragon Lane - Support)")
            lane = "sup"
            #
        case "jg":
            print("\tJungle ")
            lane = "jg"
        case other:
            Errorfun.Errorswitch()

    quit()
