def champions(champchoice):
    match champchoice:
        case 1:
                    print("Enter the champion name: ")
                    champname = input()
                    Champsearch(champname) #function to do the thing
                
        case 2:
                    print("Choose the lane you want to view from below")
                    print("1. Top Lane (Baron Lane) ")
                    print("2. Mid Lane ")
                    print("3. Bot Lane (Dragon Lane - ADC)")
                    print("4. Support Lane (Dragon Lane - Support)")
                    print("5. Jungle ")
                    print("\nEnter your choice: ")
                    lanechoice = int(input())
                    Lanesearch(lanechoice)
                    #lanesort(lanechoice) #function that will run this 
                    
        case other:
                    print("Invalid choice")
                    
def Champsearch(champname):
    #
    champ = str(champname)


def Lanesearch(lanechoice):
    lane = ""
    match lanechoice:
        case 1: 
            print("\tTop Lane (Baron Lane)")
            lane = "top"
            #
        case 2: 
            print("\tMid Lane")
            lane = "mid"
            #
        case 3: 
            print("\tBot Lane (Dragon Lane - ADC)")
            lane = "duo"
            #
        case 4: 
            print("\tSupport Lane (Dragon Lane - Support)")
            lane = "sup"
            #
        case 5: 
            print("\tJungle ")
            lane = "jg"
            #
            
        case other:
            print("Error: Invalid Choice")