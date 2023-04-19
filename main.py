import Champions
import Items
from Champions import *
from Items import *

def main():
    print("League of Legends Wiki")
    print("----------------------")
    print("\n1. Champions\n2. Items\n3. Players\n4. Guilds")
    print("Choose one of the above options: ")
    choice = int(input())
    match choice:
        # this whole thing can be a separate function but well whatever 
        case 1: 
            print("You have chosen Champions. Select from the options below\n")
            print("1. Search champion by name")
            print("2. Search champion by lane")
            print("\nEnter your choice: ")
            champchoice  = int(input())
            Champions.champions(champchoice)
                  
        case 2: 
            print("You have chosen Items. Select from the options below\n")
            print("\n1. Search Item by name")
            print("2. Sort Item by type") 
            print("3. Sort Item by class") 
            print("\nEnter your choice: ")
            itemchoice = int(input())
            Items.Item(itemchoice)
                    
        case other: 
            print("Under construction or invalid choice ")
            
main()
