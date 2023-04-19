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
                    itemtype = int(input())
                    Itemchooser(itemtype)
                    # a function for this thing 
                case 3: 
                    print("Can't think of it so will come back to it later")
                    
                case other: 
                    print("Error: Invalid Option")
                    
                    
def Itemchooser(itemtype):
    match itemtype:
        case 1: 
            print("\tAttack Damage\n")
            #
        case 2: 
            print("\tMagic Damage\n")
            #
        case 3:
            print("\tDefense Items")
            #
        case 4: 
            print("\tBoots")
            #
        case other: 
            print("Error: Ivalid Choice")
            