print("=== Snake & Ladder Game ===")

import random
START_POSITION = 0
WINNING_POSITION = 100
current_player = 0

positions = [0,0]
dice_cnt = [0,0]


def play_turn(player_position):
    dice = random.randint(1, 6)
    option = random.randint(0, 2)
    print(f"Player rolled a dice and got: {dice}")
    
    if option == 0:
        print("Option 1: No Play")
        return player_position
    elif option == 1:
        print("Option: Ladder goes forward")
        new_pos = player_position + dice
        if new_pos > WINNING_POSITION:
            print("Move goes beyond 100. Can't move forward")
            return player_position
        else:
            return new_pos
    elif option == 2:
        print("Option: Snake goes backward")
        new_pos = player_position - dice
        if new_pos < START_POSITION:
            print("Move goes below 0. Resetting to start position")
            return 0
        else:
            return new_pos
        

print(f"Game started. Player 1 at position: {positions[0]}")
print(f"Game started. Player 2 at position: {positions[1]}")

while True:
    positions[current_player] = play_turn(positions[current_player])
    dice_cnt[current_player] += 1
    
    if (positions[current_player] == WINNING_POSITION):
        break
    current_player = 1 - current_player
    
print("\n===== GAME OVER =====")
print(f" Player {current_player} WINS!")
print(f"Player 1 total dice rolls: {dice_cnt[0]}, position :{positions[0]}")
print(f"Player 2 total dice rolls:{dice_cnt[1]}, position :  {positions[1]}")    