import mysql.connector
import Errorfun
import GuildData
import PlayerData
import tkinter
from tkinter import messagebox

def Guildsinlol(guildchoice, root):
    for widget in root.winfo_children():
        widget.destroy()
    guildlabel = tkinter.Label(root, text="Guild Menu ", font=("Ariel", 20))
    guildlabel.pack(pady=15)
    root.geometry('600x550')
    match guildchoice:
        case 1:
            guildname = tkinter.Label(root, text="Enter Guild name: ", font=("Ariel", 20))
            guildname.pack(pady=10)
            name_input = tkinter.Entry(root)
            name_input.pack()
            submit_button = tkinter.Button(root, text="Submit", command=lambda: getguild())
            submit_button.pack()

            def getguild():
                guild_name = name_input.get()
                try:
                    guild_name = str(guild_name)
                    if not guild_name:
                        Errorfun.Errorcase()
                        return
                except:
                    Errorfun.Errorswitch()
                GuildData.findGuild(guild_name,root)

        case 2:
            getGuild(root)
            """
            guildlabel2 = tkinter.Label(root, text= "Please enter the guild information below to add a new guild", font=("Ariel",16 ))
            guildlabel2.pack(pady=10)
            guildname1 = tkinter.Label(root, text="Enter Guild name: ")
            guildname1.pack(pady=10)
            guildnameinput = tkinter.Entry(root)
            guildnameinput.pack()
            submit_button3 = tkinter.Button(root, text="Submit", command=lambda: guildnameinput.get())
            submit_button3.pack()
            guildlvl = tkinter.Label(root, text="Enter Guild level: ")
            guildlvl.pack(pady=10)
            guildlvlinput = tkinter.Entry(root)
            guildlvlinput.pack()
            submit_button2 = tkinter.Button(root, text="Submit", command=lambda: guildnameinput.get())
            submit_button2.pack()
            try:
             guildlvlinput = int(guildlvlinput.get())
            except:
                tkinter.messagebox.showerror("Error", "Guild level must be a number")

            guildcrname = tkinter.Label(root, text="Enter Guild creator name: ", )
            guildcrname.pack(pady=10)
            guildcrnameinput = tkinter.Entry(root)
            guildcrnameinput.pack()
            submit_button4 = tkinter.Button(root, text="Submit", command=lambda: guildcrnameinput.get())
            submit_button4.pack()
            #print("\nPlease add all the guild information below to add a guild")
            #print("\nEnter guild name: ")
            #guildname = str(input()).strip()
            #print("Enter guild creator name: ")
            #guildcreat = str(input()).strip()
            #while True:
                #print("Enter guild creator id")
                #creatid = str(input()).strip()
                #if len(creatid) == 4:
                 #   break
                #else:
                #    print("ID's should only be 4 characters long. Try again")
            #print("Enter guild level: ")
            #try:
             #   guildlvl = int(input())
            #xcept:
             #   Errorfun.Errorcase()

            #
            """
            # Look at above two lines again
        case other:
            Errorfun.Errorswitch()


def getGuild(root):
    guildlabel2 = tkinter.Label(root, text="Please enter the guild information below to add a new guild",font=("Ariel", 16))
    guildlabel2.pack(pady=10)
    guildname1 = tkinter.Label(root, text="Enter Guild name: ")
    guildname1.pack(pady=10)
    guildnameinput = tkinter.Entry(root)
    guildnameinput.pack()
    guildlvl = tkinter.Label(root, text="Enter Guild level: ")
    guildlvl.pack(pady=10)
    guildlvlinput = tkinter.Entry(root)
    guildlvlinput.pack()
    guildcrname = tkinter.Label(root, text= "Enter Guild Creator name:")
    guildcrname.pack(pady=10)
    guildcrname_input = tkinter.Entry(root)
    guildcrname_input.pack()
    guildcrid = tkinter.Label(root, text="Enter Guild creator id: ")
    guildcrid.pack(pady=10)
    guildcrid_input = tkinter.Entry(root)
    guildcrid_input.pack()
    submit_button2 = tkinter.Button(root, text="Submit", command=lambda:procesguild())
    submit_button2.pack(pady=20)
    def procesguild():
        guild_name = guildnameinput.get()
        guild_name = str(guild_name)
        if guild_name in GuildData.getAll():
            messagebox.showerror("Error", "Guild already exists")
            return
        guild_crname = guildcrname_input.get()
        guild_crname = str(guild_crname)
        guild_lvl = guildlvlinput.get()
        try:
            guild_lvl = int(guild_lvl)
        except:
            messagebox.showerror("Error", "Guild Level must be a number")
        guild_crid = guildcrid_input.get()
        guild_crid = str(guild_crid)
        if not len(guild_crid) == 4:
            messagebox.showerror("Error", "Creator ID length cannot exceed 4 characters")
            return
        if not PlayerData.authen(guild_crname,guild_crid,root):
            messagebox.showerror("Error", "Invalid Creator name and ID")
            return
        if not guild_name:
            Errorfun.Errorcase()
            return
        if not guild_crname:
            Errorfun.Errorcase()
            return
        if not guild_lvl:
            Errorfun.Errorcase()
            return
        if not guild_crid:
            Errorfun.Errorcase()
            return
        GuildData.addguild(guild_crname,guild_crid,guild_name,guild_lvl,root)

