print("=== Snake & Ladder Game ===")

import random

START_POSITION = 0
player_position = START_POSITION

print(f"Game started. Player is at position: {player_position}")

dice = random.randint(1, 6)
print(f"player rolled and dice and got : {dice}")

option = random.randint(0, 2)

if option == 0:
    print("Option 1: No Play")
elif option == 1:
    print("Option: Ladder goes forward")
    player_position += dice
elif option ==2:
    print("Option : Sanke bitten and moves back")
    player_position -= dice
    
print(f"Player current position: {player_position}")