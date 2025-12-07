print("=== Snake & Ladder Game ===")

import random

START_POSITION = 0
player_position = START_POSITION

print(f"Game started. Player is at position: {player_position}")

dice = random.randint(1, 6)
print(f"player rolled and dice and got : {dice}")