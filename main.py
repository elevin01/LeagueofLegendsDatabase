import tkinter
import Champions
import Items
import Players
import Guilds
import Errorfun
import sys

def main():
    while True:
        choices = ["Champions", "Items", "Players", "Guilds"]
        root = tkinter.Tk()
        root.geometry('600x300')
        root.title("League of Legends Wiki")
        label = tkinter.Label(root, text="League of Legends Wiki", font=("Roboto", 24))
        label.pack(pady=20)
        label2 = tkinter.Label(root, text= "This is a guide to the world of League of Legends.\nPlease select an option from the dropdown menu below to get started.", font=("Arial", 16))
        label2.pack(pady=10)
        input=""
        """
        print("League of Legends Wiki")
        print("----------------------")
        print("\n1. Champions\n2. Items\n3. Players\n4. Guilds")
        print("Choose one of the above options: ")
        """
        try:
            choice = tkinter.StringVar(root)
            choice.set("Select one of the following")
            dropdown = tkinter.OptionMenu(root, choice, *choices)
            dropdown.pack()
            submit_button = tkinter.Button(root, text="Submit", command=lambda:lime())
            submit_button.pack()

            def lime():
                menu(choice.get(), root)

            submit_button = tkinter.Button(root, text="Quit", command=lambda: sys.exit())
            submit_button.config()
            submit_button.pack(pady=20)
            root.mainloop()

        except:
            #print("It's this!")
            Errorfun.Qcase()




def menu(choice,root):
    for widget in root.winfo_children():
        widget.destroy()
    match choice:
        # this whole thing can be a separate function but well whatever
        case "Champions":
            try:
                label = tkinter.Label(root, text="You have chosen Champions.\nSelect from the options below\n", font=("Arial",16))
                label.pack(pady=10)
                champbutton1 = tkinter.Button(root, text=" Search champion by name", command=lambda : Champions.champions(1, root))
                champbutton1.pack()
                champbutton2 = tkinter.Button(root, text= "Search champion by lane", command=lambda : Champions.champions(2, root))
                champbutton2.pack()
                #champchoice = int(input())
                #Champions.champions(champchoice)
            except:
                Errorfun.Errorcase()
        case "Items":
            try:
                label2 = tkinter.Label(root, text= "You have chosen Items.\nSelect from the options below", font=("Ariel",16))
                label2.pack(pady=10)
                itembutton1 = tkinter.Button(root, text= " Search Item by name", command=lambda : Items.Item(1,root))
                itembutton1.pack()
                itembutton2 = tkinter.Button(root, text= " Sort Item by type  ", command= lambda : Items.Item(2,root))
                itembutton2.config(width=15)
                itembutton2.pack()
                itembutton3 = tkinter.Button(root, text= " Show all Items ", command= lambda : Items.Item(3,root))
                itembutton3.config(width=15)
                itembutton3.pack()
                #itemchoice = int(input())
                #Items.Item(itemchoice)
            except:
                Errorfun.Errorcase()

        case "Players":
            try:
                label3 = tkinter.Label(root, text= "You have chosen Players.\nSelect from the options below", font=("Ariel",16))
                label3.pack(pady=10)
                playerbutton1 = tkinter.Button(root, text= " Search Player by name", command=lambda : Players.Players(1,root))
                playerbutton1.pack()
                playerbutton2 = tkinter.Button(root, text= " Sort Player by level ", command= lambda : Players.Players(2,root))
                playerbutton2.config(width=15)
                playerbutton2.pack()
                playerbutton3 = tkinter.Button(root, text= " Add Player ", command= lambda : Players.Players(3,root))
                playerbutton3.config(width=15)
                playerbutton3.pack()
                playerbutton4 = tkinter.Button(root, text= " Edit Player ", command= lambda : Players.Players(4,root))
                playerbutton4.config(width=15)
                playerbutton4.pack()

                #playerchoice = int(input())
                #Players.Players(playerchoice)
            except:
                Errorfun.Errorcase()

        case "Guilds":
            try:
                label4 = tkinter.Label(root, text= "You have chosen Guilds. Select from the options below\n", font= ("Ariel",16))
                label4.pack(pady=10)
                guildsbutton1 =tkinter.Button(root, text= " Search Guild by name", command=lambda : Guilds.Guildsinlol(1,root))
                guildsbutton1.pack()
                guildsbutton2 = tkinter.Button(root, text= " Add Guild", command=lambda : Guilds.Guildsinlol(2,root))
                guildsbutton2.config(width=15)
                guildsbutton2.pack()
                #guildchoice = int(input())
                #Guilds.Guildsinlol(guildchoice)
            except:
                Errorfun.Errorcase()
        case other:
            print("called it")
            Errorfun.Qcase()

main()







