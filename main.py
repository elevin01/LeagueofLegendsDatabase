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
            match champchoice:
                case 1:
                    print("Enter the champion name: ")
                    champname = input()
                    #champsearch(champname) #function to do the thing
                
                case 2:
                    print("Choose the lane you want to view from below")
                    print("1. Baron lane\n2. Mid lane\n3. Dragon lane - ADC\n4. Dragon lane - Support\n5. Jungle")
                    print("\nEnter your choice: ")
                    lanechoice = int(input())
                    #lanesort(lanechoice) #function that will run this 
                    
                case other:
                    print("Invalid choice")
                  
        case 2: 
            print("You have chosen Items. Select from the options below\n")
            print("\n1. Search Item by name")
            print("2. Sort Item by type") 
            print("3. Sort Item by class") 
            print("\nEnter your choice: ")
            itemchoice = int(input())
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
                    # a function for this thing 
                case 3: 
                    print("Can't think of it so will come back to it later")
                    
                case other: 
                    print("Invalid option")
                    
        case other: 
            print("Under construction or invalid choice ")
            
main()
