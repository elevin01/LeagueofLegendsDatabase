import Errorfun
import tkinter
import Databsestuff
from tkinter import messagebox
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
            print("2. Middle Lane ")
            print("3. Bottom Lane (Dragon Lane - ADC)")
            print("4. Support Lane (Dragon Lane - Sup)")
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
            submit_button = tkinter.Button(root, text="Submit", command=lambda: Champsearch(champ_entry.get(),root))
            submit_button.pack()

        case 2:
            lane_label = tkinter.Label(root, text="\n\nChoose the lane you want to view from below", font=("Ariel",16))
            lane_label.pack(pady=10)
            lane_choices = {"Top Lane (Baron Lane)": "top", "Mid Lane": "mid", "Bot Lane (Dragon Lane - ADC)": "duo",
                            "Support Lane (Dragon Lane - Support)": "sup", "Jungle": "jg"}
            lane_choice = tkinter.StringVar(root)
            lane_choice.set("Select a lane")
            dropdown = tkinter.OptionMenu(root, lane_choice, *lane_choices.keys())
            dropdown.pack()
            submit_button = tkinter.Button(root, text="Submit", command=lambda: Lanesearch(lane_choices[lane_choice.get()],root))
            submit_button.pack()

        case other:
            Errorfun.Errorswitch()

def Champsearch(champname,root):
    #
    champ = str(champname).strip()
    Databsestuff.Champion_name(champ,root)


def Lanesearch(lanechoice,root):
    lane = str(lanechoice)
    if not lane:
        messagebox.showerror("!", "Choose a lane")
        return
    Databsestuff.lane_choice(lane,root)


