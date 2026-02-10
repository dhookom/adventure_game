"""adventure_game.py
Purpose: Small starter script for the adventure game project.
This file's purpose is to serve as the program entry point and to
provide initial interactive scenarios for the adventure game.
"""


def start_game():
    """Display the game introduction, ask for the player's name,
    and present the initial choice between a forest or a cave.
    Returns a tuple `(player_name, choice)` where `choice` is 'forest' or 'cave'.
    """
    print("Welcome, explorer! Your quest is to find the legendary treasure hidden in an ancient land.")
    print("You'll navigate different locations, face challenges, and make choices that affect the outcome.")
    print()

    # Ask for player's name
    name = input("What is your name, adventurer? ").strip()
    if not name:
        name = "Traveler"
    print(f"Nice to meet you, {name}. Your adventure begins now.")

    # Present the initial choice
    print("Initial choice:")
    print("1) Explore the dark forest")
    print("2) Enter the mysterious cave")

    choice = None
    while choice not in ("forest", "cave"):
        raw = input("Do you choose the forest or the cave? (forest/cave) ").strip().lower()
        if raw in ("1", "forest", "f"):
            choice = "forest"
        elif raw in ("2", "cave", "c"):
            choice = "cave"
        else:
            print("Please enter 'forest' or 'cave' (or 1/2).")

    print(f"You chose the {choice}. Good luck, {name}!")
    return name, choice


def forest_path(player_name: str):
    """Describe the forest scenario and present choices.
    Choices: follow a river or climb a tree. Use if-else to handle the decision.
    Returns a result string: 'win' or 'lose'.
    """
    desc = f"""\n{player_name}, you step into the dense, shadowed forest. The air is cool and the
trees tower above you. You hear the distant sound of running water and notice a tall tree
nearby that might offer a better view."""
    print(desc)
    print()

    print("Choices:")
    print("1) Follow the river — it may lead to sign of civilization or hidden paths.")
    print("2) Climb the tall tree — get a better view of the surroundings.")

    decision = None
    while decision not in ("river", "tree"):
        raw = input("Do you follow the river or climb the tree? (river/tree or 1/2) ").strip().lower()
        if raw in ("1", "river", "r"):
            decision = "river"
        elif raw in ("2", "tree", "t"):
            decision = "tree"
        else:
            print("Please enter 'river' or 'tree' (or 1/2).")

    if decision == "river":
        print("You follow the river. The sound grows louder and you discover a narrow footpath that looks recently used — this could be a lead toward the treasure.")
        return "win"
    else:
        print("You climb the tree carefully. From the top, you spot a plume of smoke in the distance and a faint glimmer near the riverbank — two possible directions to investigate.")
        print("Unfortunately, while investigating you are ambushed by wild creatures and must retreat.")
        return "lose"


def cave_path(player_name: str):
    """Describe the cave scenario and present choices.
    Choices: light a torch or proceed in the dark. Use conditionals to determine outcome.
    Returns a result string: 'win' or 'lose'.
    """
    desc = f"""\n{player_name}, you stand at the mouth of a mysterious cave. The darkness inside is thick, and the air smells of damp stone. You can light a torch to see, or try to proceed carefully without a light."""
    print(desc)
    print()

    print("Choices:")
    print("1) Light a torch — illuminate the cave and reveal hidden features.")
    print("2) Proceed in the dark — move quietly but risk unseen dangers.")

    action = None
    while action not in ("torch", "dark"):
        raw = input("Do you light a torch or proceed in the dark? (torch/dark or 1/2) ").strip().lower()
        if raw in ("1", "torch", "t"):
            action = "torch"
        elif raw in ("2", "dark", "d"):
            action = "dark"
        else:
            print("Please enter 'torch' or 'dark' (or 1/2).")

    if action == "torch":
        print("You light a torch. The cave walls glow with ancient markings, and you spot a hidden alcove containing an old map — this could guide you closer to the treasure.")
        return "win"
    else:
        print("You proceed in the dark. After a few careful steps you stumble over a loose stone and a sudden drop — you manage to stop yourself but lose time and supplies.")
        return "lose"


def play():
    """Run the game loop until the player wins or loses, then offer restart."""
    while True:
        player_name, player_choice = start_game()
        if player_choice == "forest":
            result = forest_path(player_name)
        else:
            result = cave_path(player_name)

        if result == "win":
            print(f"Congratulations, {player_name}! You found the treasure and completed your quest!")
        else:
            print(f"Alas, {player_name}, your adventure ended unsuccessfully this time.")

        # Ask to play again
        again = input("Would you like to play again? (y/n) ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing — farewell, explorer!")
            break


if __name__ == "__main__":
    print("Setup working: adventure_game.py executed successfully")
    play()
