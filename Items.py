import Errorfun
import tkinter
import ItemData
from tkinter import messagebox
"""
def Item(itemchoice):
     match itemchoice:
                case 1: 
                    print("Enter item name ")
                    itemname = input()
                    #function to do its thing
                 
                case 2: 
                    print("Please choose the type of items you want to view from the following options")
                    print("\n1. Attack Damage - items that deal physical damage ")
                    print("2. Magic Damage - items that deal magic damage ")
                    print("3. Defense - items that provide health, magic resistance or armor ")
                    print("4. Boots - item that helps with movement speed but can be upgraded to get other abilities ")
                    try:
                        itemtype = int(input())
                        Itemchooser(itemtype)
                        # a function for this thing
                    except:
                        Errorfun.Errorcase()
                case 3: 
                    print("Can't think of it so will come back to it later")
                    
                case other: 
                   Errorfun.Errorswitch()
"""
def Item(itemchoice, root):
    for widget in root.winfo_children():
        widget.destroy()
    itemlabel = tkinter.Label(root, text="Item Selection", font=("Ariel", 20))
    itemlabel.pack(pady=15)
    match itemchoice:
        case 1:
            item_label = tkinter.Label(root, text="Enter Item name:", font=("Ariel", 16))
            item_label.pack(pady=10)
            itemchoice = tkinter.Entry(root)
            itemchoice.pack()
            submit_button = tkinter.Button(root, text="Submit", command=lambda : ItemData.getitem(str(itemchoice.get()),root))
            submit_button.pack()
        case 2:
            item_type = tkinter.StringVar(root)
            itemtypes = ["Fighter", "Mage", "Tank", "Support", "Assassin", "Marksman", "Boots"]
            dropdown = tkinter.OptionMenu(root,item_type, *itemtypes)
            dropdown.pack()
            submit_button = tkinter.Button(root, text="Submit", command=lambda : Itemchooser(item_type.get(),root))
            submit_button.pack()
        case 3:
            itemlabel = tkinter.Label(root, text="ALL ITEMS")
            itemlabel.pack()
            ItemData.allitem(root)
        case other:
            Errorfun.Errorcase()
            quit()


def Itemchooser(itemtype,root):
    type = str(itemtype).strip()
    ItemData.gettype(type,root)

