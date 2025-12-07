print("=== Snake & Ladder Game ===")

import random

START_POSITION = 0
WINNING_POSITION = 100
player_position = START_POSITION
dice_cnt = 0

print(f"Game started. Player is at position: {player_position}")

while player_position != WINNING_POSITION:
    dice = random.randint(1, 6)
    dice_cnt += 1
    print(f"player rolled and dice and got : {dice}")

    option = random.randint(0, 2)

    if option == 0:
        print("Option 1: No Play")
        
    elif option == 1:
        print("Option: Ladder goes forward")
        new_pos = player_position + dice
        if new_pos > WINNING_POSITION:
            print("Move goes beyond 100. cant move froward")
        else:
            player_position = new_pos  
            
    elif option ==2:
        print("Option : Sanke bitten and moves back")
        player_position -= dice
        
    if player_position < 0: 
        player_position = 0
        
    print(f"Player current position: {player_position}")

print(f"Player reached {player_position}. \nTotal dice rolled to win the game: {dice_cnt} ")