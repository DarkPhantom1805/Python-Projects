import random

HAND = {
    "R" : 1, 
    "P" : 2, 
    "S" : 3
}

print("Welcome to Rock Paper Scissors. Enter 'E' at any time to Exit game.")

def check_winner(players):
    p1, p2 = players

    if p1 == 1:
        if p2 == 1:
            return "Draw"
        elif p2 == 2:
            return "2"
        elif p2 == 3:
            return "1"
    elif p1 == 2:
        if p2 == 1:
            return "1"
        elif p2 == 2:
            return "Draw"
        elif p2 == 3:
            return "2"

    elif p1 == 3:
        if p2 == 1:
            return "2"
        elif p2 == 2:
            return "1"
        elif p2 == 3:
            return "Draw"

def single_player():
    player_hand = input("""Rock, Paper or Scissors?
    'R' for Rock
    'P' for Paper
    'S' for Scissors
    :""").upper()

    player_hand = HAND.get(player_hand)
    ai_hand = random.randint(1, 3)

    return player_hand, ai_hand

def multiplayer():
    player1_hand = input("""Player 1. Rock, Paper or Scissors?
    'R' for Rock
    'P' for Paper
    'S' for Scissors
    :""").upper()

    player2_hand = input("""Player2. Rock, Paper or Scissors?
    'R' for Rock
    'P' for Paper
    'S' for Scissors
    :""").upper()
    
    player1_hand = HAND.get(player1_hand)
    player2_hand = HAND.get(player2_hand)

    return player1_hand, player2_hand

def select_mode():
    mode = input("Enter 'S' for Single Player, 'M' for Multiplayer: ").lower()
    return mode

def main():
    mode = select_mode()

    while mode != 'e':

        if mode == 's':
            winner = check_winner(single_player())
            
            if winner == "Draw":
                print("Game drawed with the computer!!")
            elif int(winner) == 1:
                print("Player 1 Won!!")
            elif int(winner) == 2:
                print("Computer Won!!")

        elif mode == 'm':
            winner= check_winner(multiplayer())
            
            if winner == "Draw":
                print("Game drawed between the players!!")
            elif int(winner) == 1:
                print("Player 1 Won!!")
            elif int(winner) == 2:
                print("Player 2 Won!!")
        
        else:
            print("Incorrect Option! Please try again")

        main()

if __name__ == "__main__":
    main()