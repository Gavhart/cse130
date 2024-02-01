# 1. Name:
#      Gavin Hart
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program asks the user about the status of properties on Pacific Avenue,
#      North Carolina Avenue, and Pennsylvania Avenue, along with their cash,
#      available houses, and hotels. It then decides whether the user can purchase a hotel
#      for Pennsylvania Avenue and under what conditions, providing cost details if applicable.
# 4. What was the hardest part? Be as specific as possible.
#      Writing this code to do what i wanted it to do was the hardest part. I had to do a lot of research to figure out how to get the code to work properly.
#      I also had to do a lot of trial and error to get the code to work properly.
# 5. How long did it take for you to complete the assignment?
#     It took me about 4 hours to complete this assignment.

# Constants for game prices
def main():
    # Ask the user if they own a property on all three places.
    color_group = input("Do you own all the green properties? (y/n): ").lower()

    # If they don't own all the locations end the program, if they do ask what they have on Pennsylvania Ave
    if color_group == "n":
        print("You cannot purchase a hotel until you own all the properties of",
         "given color group.")
    elif color_group == "y":
        prompt_pa = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    
        # Ask what they have on Pennsylvania Ave, if 5 end. 
        # If they have less then 4 ask about North Carolina Ave
        if prompt_pa == 5:
            print("You cannot purchase a hotel if the property already has one.")
        elif prompt_pa < 5:
            prompt_nc = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
            
            # Ask what they have on North Carolina Ave, if 5 end. 
            # If they have less then 4 ask about Pacific Ave.
            if prompt_nc == 5:
                print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
            elif prompt_nc < 5:
                prompt_pc = int(input("What is on Pacific Avenue? (0:nothing, 1 :one house, ... 5:a hotel): "))

                # Ask what they have on Pacific Ave, if 5 end. 
                # If not, check how many houses they need, if there are
                # enough available at the bank, and if they have enough
                # money.
                if prompt_pc == 5:
                    print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
                else:
                    prompt_hotels = int(input("How many hotels are there to purchase? "))
                    main_a(prompt_hotels, prompt_nc, prompt_pc, prompt_pa)
        
def main_a(prompt_hotels, prompt_nc, prompt_pc, prompt_pa):
    """Return print statements based on how many houses need purchased
    at each location along with the total cost and instructions of 
    what to do with each piece.

    Parameters
        prompt_hotels: Number of hotels available to purchase
        prompt_nc: Number of houses on North Carolina Ave
        prompt_pc: Number of houses on Pacific Ave
        prompt_pa: Number of houses on Pennsylvania Ave

    Return: the volume of the cylinder
    """

    # Determine how many hotels there are to purchase, if zero
    # end. Otherwise compute how many houses are needed on each
    # location as well as the total houses and cost to purchase.
    if prompt_hotels == 0:
        print("There are not enough hotels available for purchase at this time.")
    elif prompt_hotels > 0:
        num_house_pc_need = 4 - prompt_pc
        num_house_nc_need = 4 - prompt_nc
        num_house_pa_need = 4 - prompt_pa
        num_house_total_need = num_house_pc_need + num_house_nc_need + num_house_pa_need
        total_money_need = num_house_total_need * 200 + 200
        money = int(input("How much cash do you have to spend? "))

        # If the user doesn't have enough money, end.
        # If they do figure out if there are enough houses
        if total_money_need > money:
            print("You do not have sufficient funds to purchase a hotel at this time.")
        elif total_money_need <= money:
            prompt_houses = int(input("How many houses are there to purchase? "))

            # If the there aren't enough houses, end
            # otherwise return the cost to purchase the
            # cost and houses needed in each location.
            if num_house_total_need > prompt_houses:
                print("There are not enough houses available for purchase at this time.")
            elif num_house_nc_need > 0 and num_house_pc_need > 0:
                print(f"""\nThis will cost ${total_money_need}.
    Purchase 1 hotel and {num_house_total_need} house(s).
    Put 1 hotel on Pennsylvania and return any houses to the bank.
    Put {num_house_nc_need} house(s) on North Carolina.
    Put {num_house_pc_need} house(s) on Pacific.""")
            elif num_house_nc_need > 0:
                print(f"""\nThis will cost ${total_money_need}.
    Purchase 1 hotel and {num_house_total_need} house(s).
    Put 1 hotel on Pennsylvania and return any houses to the bank.
    Put {num_house_nc_need} house(s) on North Carolina.""")
            elif num_house_pc_need > 0:
                print(f"""\nThis will cost ${total_money_need}.
    Purchase 1 hotel and {num_house_total_need} house(s).
    Put 1 hotel on Pennsylvania and return any houses to the bank.
    Put {num_house_pc_need} house(s) on Pacific.""")

main()
