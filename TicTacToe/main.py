# game page
from game_board import GameBoard

#get player names
player_one = input("Player One, you will be X. What is your name?")
player_two = input("Player Two, you will be O. What is your name?")

#create game
new_gameboard = GameBoard(player_one, player_two)
new_gameboard.print_board()

# game control loop
while new_gameboard.game_continue:
    
    # X moves
    new_gameboard.player_one_move()
    new_gameboard.print_board()
    new_gameboard.check_for_winner()
    print("")
    print("")
    print("")

    if new_gameboard.winner == new_gameboard.player_one:
        new_gameboard.game_continue = False
        break

    # Check to see if the board is full
    if new_gameboard.board_is_full():
        print("Cat's Game!")
        new_gameboard.game_continue = False
        break

    # O moves
    new_gameboard.player_two_move()
    new_gameboard.print_board()
    new_gameboard.check_for_winner()
    print("")
    print("")
    print("")

    if new_gameboard.winner == new_gameboard.player_two:
        new_gameboard.game_continue = False
        break
       
    
    
# print the winner! 
print("_______________________________________")
print("")
print("Congratulations! You are the winnner, " + new_gameboard.winner + '!')
print("_______________________________________")


