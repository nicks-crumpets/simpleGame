import time
import random

# All locations in the game, organised with: title, description, and their exits, optionally their items

# <editor-fold desc="All locations in the game">

locations = {0: {
    "title": "Deep forest",
    "desc": "Welcome to the deep forest, in a dark corner in the middle of nowhere",
    "exits": {
        "north": 1,
        "east": 3
    },
    "items": []
}, 1: {
    "title": "Forest, west corner",
    "desc": "You're in the west corner of the forest, you find a machete!",
    "exits": {
        "south": 0,
        "north": 2,
        "east": 4
    },
    "items": [
        "machete",
    ]
}, 2: {
    "title": "Trapped area",
    "desc": "You find a bear trap!",
    "exits": {
        "south": 1,
        "east": 5
    },
    "items": [

    ],

}, 3: {
    "title": "Forest, south",
    "desc": "You find a rusty key, to pick up type: 'take'",
    "exits": {
        "east": 6,
        "west": 0,
        "north": 4
    },
    "items": [
        "key",
    ]

}, 4: {
    "title": "Forest - Center",
    "desc": "You stand before a large oak tree, would you like to fight the boss?, type 'fight' ",
    "exits": {
        "west": 1,
        "south": 3,
        "east": 7,
        "north": 5
    },
    "items": [

    ],
},
    5: {
    "title": "Forest - north",
    "desc": "You find nothing but an old media collection with the name 'Ja#ie' etched into it",
    "exits": {
        "south": 4,
        "west": 2,
        "east": 8,
    },
    "items": [
        "Fishing net"
    ],
},
    6: {
    "title": "lake",
    "desc": """You find a lake""",
    "exits": {
        "south": 4,
        "west": 2,
        "east": 8,
    },
    "items": [

    ]
},
    7: {
    "title": "Forest - east",
    "desc": "You get caught by a bear trap, but manage to free yourself (-10HP)",
    "healthModifier": -10,
    "exits": {
        "south": 6,
        "north": 8,
        "west": 4,
    },
    "items": []
},
    8: {
    "title": "Forest - north east",
    "desc": """You find a small blunt knife
     DMG: 2
     You see a cave entrance to your left, enter? [cave]""",
    "exits": {
        "south": 4,
        "west": 2,
        "east": 8,
        "cave": 9,
    },
    "items": []
},
    9: {
    "title": "cave",
    "desc": """You look around the cave and see mould in the cave walls
    You see a matchstick looking figure in the distance, continue?
    
    -- This is a point of no return, you must continue -- 
    """,
    "requires": "key",
    "exits": {
        "cave": 10,
    },
    "items": []
},
    10: {
    "title": "BOSS FIGHT - SPENCER",
    "desc": """The matchstick man looks you in the eyes and challenges you to a fight...
    
    to agree to his challenge, type 'fight'""",
    "exits": {
        "THERE IS NO RETURN, FIGHT OR BURN": 0,
    },
    "items": [],
}
}

enemies = {0: {
    "title": "SPENCER",
    "desc": "The matchstick man looms over you, ready to lunge a punch at you",
    "health": 50,
    "dmg": 7,
},
    1: {
    "title": "Oaky McTree",
    "desc": "Okay the tree shakes his leaves in pure anger",
    "health": 25,
    "dmg": 4,

    }
}

# sets variables for the enemies so that data inside them can be retrieved
enemyOne = enemies[0]
enemyTwo = enemies[1]

# </editor-fold>

# <editor-fold desc="Player inventory & stats">
# ----- Inventory & stats ----- #
player = {
    "location": 0,
    "health": 100,
    "atk": 7
}

# Player inventory
playerInventory = []

# </editor-fold>

# Prints the player location in a function
def display_location(loc):
    print("+-----------------------------------------+")
    # Prints the location title and description (& whitespace)
    print(loc["title"])
    print(loc["desc"])
    print()
    # prints the items in the area, * to remove the brackets and quote marks
    print("You look around and see these items: ", end="\n")
    print(*loc["items"], sep = ",")

    # Prints text above the exit options
    print("Exits:")

    # Prints all possible exits
    for i, v in loc["exits"].items():
        print(i, "-", locations[v]["title"])

def fighting(enemyName, playerHP, enemyHP, playerDMG, enemyDMG):
    endFight = True
    while endFight:

        if enemyHP <= 0:
            break
        if playerHP <0:
            break

        attack = input("""Attack?
        1. Punch
        2. Use weapon
        3. Run away
        """)
        attack = attack.lower()

        if attack == "1" or attack == "punch":
            # Player fights the enemy
            enemyHP = enemyHP - playerDMG
            print(f"You deal {playerDMG}Hp of damage! {enemyName} is at {enemyHP}Hp")
            time.sleep(1)
            print(f"{enemyName} fights back!")
            # Enemy fights the player
            playerHP = playerHP - enemyDMG
            time.sleep(1)
            print(f"You took {enemyDMG}Hp of damage! You have {playerHP}Hp")
            time.sleep(1)

        elif attack == "2" or attack == "weapon":
            # enemyHP = enemyHP - playerWeaponDMG
            playerHasWeapon = "machete" in playerInventory
            if playerHasWeapon:
                print("You use your machete!")
                enemyHP = enemyHP - playerDMG * 2
                print(f"You deal {playerDMG * 2}Hp of damage! {enemyName} is at {enemyHP}Hp")
                time.sleep(1)
                print(f"{enemyName} fights back!")
                # Enemy fights the player
                playerHP = playerHP - enemyDMG
                time.sleep(1)
                print(f"You took {enemyDMG}Hp of damage! You have {playerHP}Hp")
                time.sleep(1)
            else:
                print("You don't have a weapon!")

        elif attack == "3" or attack == "run away":
            if enemyName == "SPENCER":
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("There is no escape from SPENCER...")
                time.sleep(1)
                print("Fight, or surrender")
                time.sleep(1)
                # skips all other statements returns to top of loop for fighting
                continue

            elif hasTriedRunning is True:
                print("You tried running once, you don't have the energy to try again")


            # heads/tails style of 50/50 for running away (50% chance to be able to run away)
            runAttempt = random.randint(1,2)
            if runAttempt == 1:
                print("You successfully run away!")
            elif runAttempt == 2:
                print(f"You couldn't run away, {enemyName} caught you!")
                hasTriedRunning = True
            else:
                print("You don't have a weapon!")
        if attack == "exit":
            endFight = False

        # if either side HP reaches 0 or lower, the fight ends

    if enemyHP <= 0:
        print(f"{enemyName} defeated!")
        print()

        if enemyName == "SPENCER":
            print("You win!")
            exit()

    elif playerHP <= 0:
        print(f"You were defeated!")

def engine():
    print("""
    This game is in development.
    --- !Do not redistribute when this message is present! ---
    """)

    # ---- AREA TO ADD ANY NOTICES TO THE PLAYER, CONTROLS ETC. ---- #
    print("""
    CONTROLS:
    --- No case sensitivity is required ---
    To access your inventory at any point, type: 'inv'
    At each location, there will be direction options of north, south, east and west, type one to move
    if a direction is not on the list, you won't be able to move there
    
    -- Picking up & dropping items --
    If you want to pick up an item in an area, type 'take' 
    To drop items, type 'drop' and then the item name
    
    ^^^ THERE'S INSTRUCTIONS UP HERE ^^^
    
    """)

    time.sleep(3)
    print("let the game begin!")
    time.sleep(1)
    # ------------------------------------------------------------- #

    # Runs over repetitively, so the player can keep carrying out actions
    while True:

        # <editor-fold desc="Player location setup">

        # changes the current location of the player in the dictionary
        current_location = player["location"]
        # Sets the variable 'loc' to the current player location
        loc = locations[current_location]
        # Displays the current location of the player [display_location] function
        display_location(loc)
        # Tells the player what items are in the area they're in


        # </editor-fold>

        # <editor-fold desc="User Input section">

        # Displays arrows where the player should type
        action = input(">>> ")
        # makes the 'action' variable into lowercase so the input isn't case-sensitive
        action = action.lower()

        # </editor-fold>

        # Exit option to quit the game, available at any time
        if action == "exit":
            break

        # <editor-fold desc="NSEW Standard player movement">

        if action == "south" and "south" in loc["exits"]:
            # Prints what the user did
            print("\nYou go south")
            # Sets the location to what the direction exit is set to in the location
            # e.g. if north is loc [3], location is set to location 3
            player["location"] = loc["exits"]["south"]

        elif action == "north" and "north" in loc["exits"]:
            print("\nYou go north")
            player["location"] = loc["exits"]["north"]

        elif action == "east" and "east" in loc["exits"]:
            print("\nYou go east")
            player["location"] = loc["exits"]["east"]

        elif action == "west" and "west" in loc["exits"]:
            print("\nYou go west")
            player["location"] = loc["exits"]["west"]

        # </editor-fold>

        # <editor-fold desc="Entering into locked areas requiring items">

        # Instructions for entering the cave area, checks if the cave exists in the options
        if action == "cave" and "cave" in loc["exits"]:
            # Checks if the key is in the player inventory
            if "key" in playerInventory:
                # Tells the player what area they are going to
                print("\nYou go through the cave")
                # Changes the location in the player dictionary to what was under 'cave'
                player["location"] = loc["exits"]["cave"]

                # Fallback if the player doesn't have a key
            else:
                # Tells the player they need to find a key
                print("You need a key to open the creaky cave door")

        # </editor-fold>

        # prints players inventory
        if action == "inv" or action == "inventory":
            print(playerInventory)

        # resting to restore health, only works in the lake
        if action == "rest":
            if loc["title"] == "lake":

                # Easter egg - 1% chance to fall in the lake and drown
                fallInLake = random.randint(1,100)
                if fallInLake == 69:
                    print("You fall in the lake")
                    time.sleep(1)
                    print("You drown to your death")
                    time.sleep(1)
                    player["health"] = 0

                # max out player health
                player["health"] = 100
                print("You rest by the lake for some time")
                time.sleep(1)
                print(f"You now have {player['health']}Hp")
            else:
                print("You can't rest here! It's far too dangerous!")
        # ----------------------------------------------- #

        # calls on the fighting function if the player initiates a fight
        if action == "fight":
            if player["location"] == 10:
                fighting(enemyOne["title"], player["health"], enemyOne["health"], player["atk"], enemyOne["dmg"])
            elif player["location"] == 4:
                fighting(enemyTwo["title"], player["health"], enemyTwo["health"], player["atk"], enemyTwo["dmg"])
            else:
                print("There's no enemy here!")

        # <editor-fold desc="Player picking up ANY (woo!!) item if it's in the area">

        # if the action is take and there is a key in the items section of the area

        if action == "take" and any(loc["items"]):
            # 'key' gets added to the players' inventory individually, uses extend so the key works
            playerInventory.extend(loc["items"])
            # Tells the player that they have taken the items in their inventory
            print(f"\n-- You take {', '.join(loc['items'])} --")
        else:
            continue

        if action == "drop" and any(playerInventory):
            itemToDrop = input("What item do you want to drop?")

            if itemToDrop in playerInventory:
                # removes the item from playerInventory
                playerInventory.remove(itemToDrop)

                # in the location dictionary, in the current location, in the items list, append the dropped item
                locations[loc['items']].append(itemToDrop)

                print(f"DEBUG: Area: {loc["title"]}, items in area: {loc["items"]}")
                # Lets the player know what they dropped and where
                print(f"You removed {action} and dropped it in the {loc["title"]}")
            else:
                # If the player doesn't have the item in their inventory, it tells them & lets them try again
                print(f"You don't have {itemToDrop} in your inventory!")
                continue

            # If you drop an item in the lake you lose it, haha lol
            if loc["title"] == "lake":
                # removes the item from the location, because it sunk, duh
                locations[loc["items"]].remove(itemToDrop)
                print(f"""You dropped your {itemToDrop} in the {loc["title"]}, you watch it sink to the bottom
                        Items lost: {itemToDrop}""")




        # </editor-fold>

        # <editor-fold desc="Player stats access (Inventory & health)">

        # Player can check their inventory at any turn, by typing inv or inventory
        # --- MAKE THESE TWO INTO SEPARATE FUNCTIONS, AND HEALTH SHOULD BE CALLED AFTER EVERY HIT AGAINST THE PLAYER & HEALING
        if action == "inv" or action == "inventory":
            # * is ALL wildcard, prints the items in playerInventory separated by a \n character
            print("Your Inventory:", *playerInventory, sep="\n")

        # Allows the player to see their health if they type 'health'
        if action == "health":
            print(f"Your health is:{player["health"]}")

        # </editor-fold>

        # If a 'general' health change exists for an area, it gets applied to the players health
        # Applies to both negative effects, and if the area is healing
        if "healthModifier" in loc:
            player["health"] += loc["healthModifier"]

        # If a health increase takes it over 100, this keeps the max at 100, lazy, but it works :)
        if player["health"] > 100:
            player["health"] = 100

        # if the player health reaches zero, say: game over and quit game
        if player["health"] < 0:
            print("--- GAME OVER ---")
            exit()




# Runs everything in the game engine function, the main 'brain' of the game
engine()