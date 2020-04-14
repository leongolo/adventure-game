import time
import random
import sys
import logging


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(person, weapon):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a monster lives near by.")
    print_pause("In front of you is a house.")
    print_pause("To your left is a dark cave.")
    print_pause(f"In your hand you hold your {weapon}.\n")


def house(person, weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                "out steps " + person + ".")
    print_pause("Help! This is " + person + "'s house.")
    print_pause(person + " attacks you!\n")

    if "golden sword" not in chosen_weapon:
        print_pause("Your fighting spirit and " + weapon +
                    " might not be enough for this.")
    while True:
        choice2 = input("Would you like to (1) fight or (2) hide?\n")
        if choice2 == '1':
            if "golden sword" in chosen_weapon:
                print_pause("\nAs " + person + " jumps at you and "
                            "attacks you, his state of health, "
                            "your fighting spirit and the "
                            "golden sword are on your side.")
                print_pause(person + " sees the golden swords and flees.")
                print_pause("You defeated the " + person +
                            " and are celebrated "
                            "as the village's hero!")

            else:
                print_pause("\nEven your best effort isn't enough...")
                print_pause("With your " + weapon + " under your arm, "
                            "you retreat.")
                print_pause("You have been defeated!")
            play_again()
            break

        elif choice2 == '2':
            print_pause("\nYou run back into the field and "
                        "hide in the grass.\n"
                        "You catch your breath and reevaluate "
                        "your previous choice.\n")
            field(person, weapon)
            break


def cave(person, weapon):
    if "golden sword" in weapon:
        print_pause("\nThis place looks all too familiar.")
        print_pause("Having grabbed the strongest weapon earlier, "
                    "you are ready "
                    "to take on " + person + ".\n")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("In the glooming dark you find a golden sword "
                    "at the end of the cave.")
        print_pause("You pick up the golden sword and are "
                    "ready to fight the monster.")
        print_pause("Feeling more confident with the golden "
                    "sword in your hand, "
                    "you walk back to the house.\n")
        chosen_weapon.append("golden sword")

    field(person, weapon)


def field(person, weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == '1':
            house(person, weapon)
            break
        elif choice1 == '2':
            cave(person, weapon)
            break


def play_again():
    chosen_weapon = []
    choice3 = input("Would you like to play again?\n"
                    "Please enter 'yes' or 'no'.\n").lower()
    if choice3 == "yes":
        print_pause("\nExcellent! Restarting the game...\n\n")
        play_game()
    elif choice3 == "no":
        print_pause("Thank you for playing!")
        sys.exit(0)
    else:
        play_again()


def play_game():
    person = random.choice(["Santa Clause", "Batman",
                            "Donald Trump", "Covid-19"])
    weapon = random.choice(["dandileon", "toothpick", "wine bottle"])
    intro(person, weapon)
    field(person, weapon)


chosen_weapon = []
play_game()