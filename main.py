
from game_logic.game import *


if __name__ == "__main__":
    game=init_game() # game = deck,player1,player2
    player_1=game["player_1"]
    player_2=game["player_2"]
    for i in range(26):
        play_round(player_1,player_2)
    

    if len(player_1["won_pile"])>len(player_2["won_pile"]):
        print("player1 won")
    elif len(player_1["won_pile"])<len(player_2["won_pile"]):
        print("player2 won")
    else:
        print("tie")
    