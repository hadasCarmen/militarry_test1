from utils.deck import *


def create_player(name="AI")-> dict:
    dict_player={}

    if name=="AI":
        dict_player["player2"]="AI"    
    else:
        dict_player["player1"]=name
    dict_player["list of cards"]=[]
    dict_player["won_pile"]=[]
    return dict_player


def  init_game() -> dict:
    player1=create_player("AI")
    player2=create_player("elazar")
    deck_game=create_deck()
    shuffle(deck_game)
    mone=0
    for card in deck_game:
        if mone<26:
            player1["list of cards"].append(card)
            mone+=1
        else:
            player2["list of cards"].append(card)
    return {"deck":deck_game,"player_1":player1,"player_2":player2}
        


    


def play_round(player_1: dict, player_2: dict)-> None:
    # game=init_game() # game = deck,player1,player2
    # # for i in range(26):
    card1=player_1["list of cards"]
    card2=player_2["list of cards"]
    won_pile1=player_1["won_pile"]
    won_pile2=player_2["won_pile"]
        
    if card1[0]["value"]>card2[0]["value"]:
        won_pile1.append(card1[0])
        won_pile1.append(card2[0])
    elif card1[0]["value"]>card2[0]["value"]:
        won_pile2.append(card1[0])
        won_pile2.append(card2[0])
    del card1[0]
    del card2[0]
    return
