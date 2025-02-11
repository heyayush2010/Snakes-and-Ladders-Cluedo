import random
import time

# Cluedo code

# The dice
NUMBERS = ["1", "2", "3", "4", "5", "6"]

def roll_dice():
    return random.randint(1, 6)

# Assign values to game characters and conditions
CHARACTERS = ["Miss Scarlett", "Colonel Mustard", "Mr. Green", "Mrs. Peacock", "Professor Plum"]
WEAPONS = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope"]
ROOMS = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
CROSS_OUT = {"characters": [], "weapons": [], "rooms": []}  # Items that have been excluded

def setup_game():
    hidden_character = random.choice(CHARACTERS)
    hidden_weapon = random.choice(WEAPONS)
    hidden_room = random.choice(ROOMS)
    return hidden_character, hidden_weapon, hidden_room

def get_clue(room):
    clues = {
        "Kitchen": ["A character is nearby.", "A weapon was found in the corner.", "No one has entered this room today."],
        "Ballroom": ["The windows are locked.", "Someone might have passed through this room.", "It seems a weapon was placed here recently."],
        "Library": ["You hear a faint noise coming from a hidden room.", "The lights flicker occasionally.", "A weapon is under a chair."],
        "Conservatory": ["The plants are well maintained.", "A suspicious footprint near the window.", "A glass vase is missing."],
        "Dining Room": ["There are food stains on the table.", "A strange sound came from the adjacent room.", "The curtains are drawn."],
        "Billiard Room": ["The pool table is disturbed.", "A cue ball is missing.", "The lights are dim in this room."],
        "Lounge": ["A chair is tipped over.", "A strange smell is in the air.", "There's a shadow near the window."],
        "Hall": ["You hear footsteps approaching.", "A door creaks loudly.", "The floor is dusty."],
        "Study": ["There are papers scattered around.", "A book is missing from the shelf.", "A faint smell of tobacco."],
    }
    return random.choice(clues.get(room, ["No clue available for this room."]))

def cross_out_item(item, category):
    if item not in CROSS_OUT[category]:
        CROSS_OUT[category].append(item)
        print(f"{item} has been crossed out from your list.")
    else:
        print(f"{item} is already crossed out.")

def make_accusation():
    accusation_character = input(f"Accuse a character from {CHARACTERS}: ").strip()
    accusation_weapon = input(f"Accuse a weapon from {WEAPONS}: ").strip()
    accusation_room = input(f"Accuse a room from {ROOMS}: ").strip()
    return accusation_character, accusation_weapon, accusation_room

def play_cluedo(hidden_character, hidden_weapon, hidden_room):
    current_room = random.choice(ROOMS)
    print(f"You start in the {current_room}.")
    
    while True:
        input("Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"You rolled a {roll}.")
        
        # Move to a new room
        current_room_index = ROOMS.index(current_room)
        new_room_index = (current_room_index + roll) % len(ROOMS)
        current_room = ROOMS[new_room_index]
        print(f"You moved to the {current_room}.")
        
        # Get a clue card for the current room
        clue = get_clue(current_room)
        print(f"Clue card: {clue}")
        
        print("\nMake your guess:")
        guess_character = input(f"Choose a character from {CHARACTERS}: ").strip()
        guess_weapon = input(f"Choose a weapon from {WEAPONS}: ").strip()
        guess_room = current_room  # The guess room is the current room
        
        print(f"Guess: {guess_character} with the {guess_weapon} in the {guess_room}")
        
        if (guess_character == hidden_character and 
            guess_weapon == hidden_weapon and 
            guess_room == hidden_room):
            print("Congratulations! You have guessed the correct character, weapon, and room!")
            break
        else:
            print("Incorrect guess. Try again.")
            cross_out_item(guess_character, "characters")
            cross_out_item(guess_weapon, "weapons")
            cross_out_item(guess_room, "rooms")
        
        # Ask if player wants to make an accusation
        accuse = input("Do you want to make an accusation? (yes/no): ").strip().lower()
        if accuse == "yes":
            accusation_character, accusation_weapon, accusation_room = make_accusation()
            if (accusation_character == hidden_character and 
                accusation_weapon == hidden_weapon and 
                accusation_room == hidden_room):
                print("Your accusation is correct! You win!")
                break
            else:
                print("Your accusation is incorrect. You lose.")
                break

def watch_cluedo(hidden_character, hidden_weapon, hidden_room):
    current_room = random.choice(ROOMS)
    print(f"The simulation starts in the {current_room}.")
    
    while True:
        roll = roll_dice()
        print(f"Rolled a {roll}.")
        
        # Move to a new room
        current_room_index = ROOMS.index(current_room)
        new_room_index = (current_room_index + roll) % len(ROOMS)
        current_room = ROOMS[new_room_index]
        print(f"Moved to the {current_room}.")
        
        guess_character = random.choice(CHARACTERS)
        guess_weapon = random.choice(WEAPONS)
        guess_room = current_room  # The guess room is the current room
        print(f"Guess: {guess_character} with the {guess_weapon} in the {guess_room}")
        
        if (guess_character == hidden_character and 
            guess_weapon == hidden_weapon and 
            guess_room == hidden_room):
            print("The correct character, weapon, and room have been guessed!")
            break


# Snakes and Ladders code

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time is up!")

def roll_dice_snakes_ladders():
    return random.randint(1, 6)

def move_player(player, position, roll):
    new_position = position + roll
    if new_position > 100:
        new_position = position  # Player cannot move beyond 100
    return new_position

def check_snake_or_ladder(position):
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    if position in snakes:
        print(f"Player landed on a snake at {position}! Going down to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Player landed on a ladder at {position}! Going up to {ladders[position]}")
        return ladders[position]
    return position

def play_snakes_and_ladders():
    player_positions = [0, 0]
    player_turn = 0

    while True:
        input(f"Player {player_turn + 1}'s turn. Press Enter to roll the dice...")
        roll = roll_dice_snakes_ladders()
        print(f"Player {player_turn + 1} rolled a {roll}")
        player_positions[player_turn] = move_player(player_turn, player_positions[player_turn], roll)
        player_positions[player_turn] = check_snake_or_ladder(player_positions[player_turn])
        print(f"Player {player_turn + 1} is now on square {player_positions[player_turn]}")

        if player_positions[player_turn] == 100:
            print(f"Player {player_turn + 1} wins!")
            break

        if roll != 6:
            player_turn = 1 - player_turn  # Switch turn if the roll is not 6


if __name__ == "__main__":
    game_choice = input("Enter 'cluedo' to play Cluedo or 'snakes' to play Snakes and Ladders: ").strip().lower()
    
    if game_choice == 'cluedo':
        hidden_character, hidden_weapon, hidden_room = setup_game()
        mode = input("Enter 'play' to play the game or 'watch' to watch the simulation: ").strip().lower()
        
        if mode == 'play':
            play_cluedo(hidden_character, hidden_weapon, hidden_room)
        elif mode == 'watch':
            watch_cluedo(hidden_character, hidden_weapon, hidden_room)
        else:
            print("Invalid mode selected.")
    
    elif game_choice == 'snakes':
        play_snakes_and_ladders()
    
    else:
        print("Invalid game choice. Please enter 'cluedo' or 'snakes'.")
