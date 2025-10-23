import random
def create_card(rank:str,suite:str)-> dict:

    
    dict_ranks={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    value=dict_ranks[rank]
    dict_card={"rank":rank,"suite":suite,"value":value}


    return dict_card



def compare_cards(p1_card:dict, p2_card:dict)-> str:
    if (p1_card["value"]>p2_card["value"]):
        return "p1"
    elif(p1_card["value"]<p2_card["value"]):
        return "p2"
    else:
        return "war"


def create_deck() -> list[dict]:
    dict_ranks={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    suites=["h","c","d","s"]
    deck=[]
    for card in dict_ranks.keys():
        for suite in suites:
           deck.append(create_card(card,suite))

    return deck







def shuffle(deck:list[dict]):
    for i in range(1000):
        card1=random.randint(0,51)
        card2=random.randint(0,51)
        deck[card1],deck[card2]=deck[card2],deck[card1]

    return deck

