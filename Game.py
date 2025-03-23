
import Gamefunctions

def main():
    """
    Main function to run the game.

    Prompts the user for their name, displays a welcome message,
    and calls functions from Gamefunctions to interact with the user.
    """
    name = input("Enter your name: ")
    Gamefunctions.print_welcome(name, 40)
    print()

    monster = Gamefunctions.random_monster()
    print("A wild monster appears!")
    for key, value in monster.items():
        print(f"  {key}: {value}")
    print()

    item_price = input("Enter the item price (e.g. some real number like 5.00): ")
    starting_money = input("Enter your starting money (e.g., some real number like 10.00): ")
    try:
        quantity = int(input("Enter the quantity to purchase: "))
    except ValueError:
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1
    purchased, remaining = Gamefunctions.purchase_item(item_price, starting_money, quantity)
    print(f"You purchased {purchased} item(s) and have ${remaining} left.")
    print()

    print("Welcome to the shop:")
    Gamefunctions.print_shop_menu("Sword", 100, "Shield", 80)

    user_hp = 50
    user_gold = 20
    max_hp = 100 

    while True:
        print(f"\nYou have {user_hp} HP and {user_gold} gold.")
        print("What would you like to do?")
        print("  1) City")
        print("  2) Fight a monster outside of the city")
        print("  3) Sleep (Restore up to 10 HP)")
        print("  4) Quit")

        choice = input("Enter your choice: ")

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        choice = int(choice)

        if choice == 1:
            print("\nYou head to the city. You see beautiful buildings, and shops all around")

        elif choice == 2:
            user_hp, user_gold = Gamefunctions.fight_monster(user_hp, user_gold)
            if user_hp <= 0:
                print("\nYou died. Game Over.")
                break

        elif choice == 3:
            heal_amount = 10
            old_hp = user_hp
            user_hp = min(user_hp + heal_amount, max_hp)
            print(f"\nYou rest, restoring {user_hp - old_hp} HP. Your HP is now {user_hp}.")

        elif choice == 4:
            print("\nThanks for playing!")
            break

    print("Exiting game.")


if __name__ == "__main__":
    main()