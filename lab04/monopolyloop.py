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
HOUSE_PRICE = 200  # Adjust as necessary
HOTEL_PRICE = 400  # Assuming the same price for simplification; adjust as needed

def input_int(message):
    """Safely captures integer input."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Monopoly Hotel Purchase Decision Program")
    # Ask the user if they own a property on all three places.
    color_group = input("Do you own all the green properties? (y/n): ").lower()

    # If they don't own all the locations, end the program. If they do, ask what they have on Pennsylvania Ave.
    if color_group != "y":
        print("You cannot purchase a hotel until you own all the properties of a given color group.")
        return

    prompt_pa = input_int("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): ")

    if prompt_pa == 5:
        print("You cannot purchase a hotel if the property already has one.")
        return

    prompt_nc = input_int("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): ")
    prompt_pc = input_int("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): ")
    prompt_hotels = input_int("How many hotels are there to purchase? ")

    if prompt_hotels == 0:
        print("There are not enough hotels available for purchase at this time.")
        return

    main_decision(prompt_nc, prompt_pc, prompt_pa, prompt_hotels)

def main_decision(prompt_nc, prompt_pc, prompt_pa, prompt_hotels):
    num_house_pc_need = 4 - prompt_pc
    num_house_nc_need = 4 - prompt_nc
    num_house_total_need = num_house_pc_need + num_house_nc_need
    total_money_need = (num_house_total_need * HOUSE_PRICE) + HOTEL_PRICE
    money = input_int("How much cash do you have to spend? ")

    if total_money_need > money:
        print("You do not have sufficient funds to purchase a hotel at this time.")
        return

    prompt_houses = input_int("How many houses are there to purchase? ")
    if num_house_total_need > prompt_houses:
        print("There are not enough houses available for purchase at this time.")
        return

    # Summary of user inputs
    print("\nSummary of your inputs:")
    print(f"- Own all green properties: Yes\n- Pennsylvania Avenue: {prompt_pa} houses\n- North Carolina Avenue: {prompt_nc} houses\n- Pacific Avenue: {prompt_pc} houses\n- Cash: ${money}\n- Houses to purchase: {prompt_houses}\n- Hotels to purchase: {prompt_hotels}")

    # Decision making for hotel purchase
    if num_house_nc_need > 0 and num_house_pc_need > 0:
        decision_message = "A"
    elif num_house_nc_need > 0:
        decision_message = "B"
    elif num_house_pc_need > 0:
        decision_message = "C"
    else:
        decision_message = "D"

    print_purchase_decision(decision_message, total_money_need, num_house_nc_need, num_house_pc_need)

def print_purchase_decision(decision, total_money_need, num_house_nc_need, num_house_pc_need):
    print(f"\nThis will cost ${total_money_need}.")
    print("Purchase 1 hotel and {num_house_total_need} house(s).")
    print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
    if decision in ["A", "B"]:
        print(f"Put {num_house_nc_need} house(s) on North Carolina.")
    if decision in ["A", "C"]:
        print(f"Put {num_house_pc_need} house(s) on Pacific.")

main()
