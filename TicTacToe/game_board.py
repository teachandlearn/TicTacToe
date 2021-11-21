class GameBoard:
    
    def __init__(self, player_one = 'Player One', player_two = 'Player Two'):
        self.gameboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player_one = player_one
        self.player_two = player_two
        self.winner = ""
        self.game_continue = True
    
    #def get_player(self, player_num):
        #if player_num == 1:
        #    return self.player_one
        #else:
        #    return self.player_two
    
    def player_one_move(self):
        # insert prompt for user
        player_one_move = int(input(self.player_one + ", what is your move? Pick any unoccupied space by typing the number."))
        self.gameboard[player_one_move - 1] = "X"
    
    def player_two_move(self):
        # insert prompt for user
        player_two_move = int(input(self.player_two + ", what is your move? Pick any unoccupied space by typing the number."))
        self.gameboard[player_two_move - 1] = "O"
    
    def print_board(self):
        print(str(self.gameboard[0]) + " | " + str(self.gameboard[1]) + " | " + str(self.gameboard[2]))
        print('---------')
        print(str(self.gameboard[3]) + " | " + str(self.gameboard[4]) + " | " + str(self.gameboard[5]))
        print('---------')
        print(str(self.gameboard[6]) + " | " + str(self.gameboard[7]) + " | " + str(self.gameboard[8]))
    
    def check_for_winner(self):
        # conditions to win
        ## three horizontal are matching (3 cases)
        
        if self.gameboard[0] == self.gameboard[1] and self.gameboard[1] == self.gameboard[2]:
            if self.gameboard[0] == 'X':
                print("Congratulations, " + self.player_one)
                print("You won horizontally!")
                self.winner = self.player_one
            else:
                print("Congratulations, " + self.player_two)
                print("You won horizontally!")
                self.winner = self.player_two

            self.game_continue = False #ends game

        elif self.gameboard[3] == self.gameboard[4] and self.gameboard[3] == self.gameboard[5]:
            if self.gameboard[3] == 'X':
                print("Congratulations, " + self.player_one)
                print("You won horizontally!")
                self.winner = self.player_one
            else:
                print("Congratulations, " + self.player_two)
                print("You won horizontally!")
                self.winner = self.player_two

            self.game_continue = False #ends game

        elif self.gameboard[6] == self.gameboard[7] and self.gameboard[6] == self.gameboard[8]:
            if self.gameboard[6] == 'X':
                print("Congratulations, " + self.player_one)
                print("You won horizontally!")
                self.winner = self.player_one
            else:
                print("Congratulations, " + self.player_two)
                print("You won horizontally!")
                self.winner = self.player_two

            self.game_continue = False #ends game  

        ## three vertical are matching (3 cases)
        
        if self.gameboard[0] == self.gameboard[3] and self.gameboard[3] == self.gameboard[6]:
            if self.gameboard[0] == 'X':
                print("Congratulations, " + self.player_one)
                print("You won vertically!")
                self.winner = self.player_one
            else:
                print("Congratulations, " + self.player_two)
                print("You won vertically!")
                self.winner = self.player_two

            self.game_continue = False #ends game
        
        elif self.gameboard[1] == self.gameboard[4] and self.gameboard[4] == self.gameboard[7]:
            if self.gameboard[1] == 'X':
                print("Congratulations, " + self.player_one)
                print("You won vertically!")
                self.winner = self.player_one
            else:
                print("Congratulations, " + self.player_two)
                print("You won vertically!")
                self.winner = self.player_two

            self.game_continue = False #ends game
        
        elif self.gameboard[2] == self.gameboard[5] and self.gameboard[5] == self.gameboard[8]:
            if self.gameboard[2] == 'X':
                print("Congratulations, " + self.player_one)
                print("You won vertically!")
                self.winner = self.player_one
            else:
                print("Congratulations, " + self.player_two)
                print("You won vertically!")
                self.winner = self.player_two

            self.game_continue = False #ends game
           
        
        ## three diagonal are matching (2 cases)
        ### top left to bottom right
        if self.gameboard[0] == self.gameboard[4] and self.gameboard[0] == self.gameboard[8]:
            if self.gameboard[0] == 'X':
                print("Congratulations, " + self.player_one)
                print("You won diagonally!")
                self.winner = self.player_one
            else:
                print("Congratulations, " + self.player_two)
                print("You won diagonally!")
                self.winner = self.player_two
            
            self.game_continue = False #ends game
        
        ### top right to bottom left
        if self.gameboard[2] == self.gameboard[4] and self.gameboard[2] == self.gameboard[6]:
            if self.gameboard[2] == 'X':
                print("Congratulations, " + self.player_one)
                print("You won on diagonally!")
                self.winner = self.player_one
            else:
                print("Congratulations, " + self.player_two)
                print("You won on diagonally!")
                self.winner = self.player_one

            self.game_continue = False #ends game
    
    def board_is_full(self):
        board_count = 0
        for item in self.gameboard:
            if item == 'X' or item =='O':
                board_count += 1
        
        if board_count == 8:
            # Call the method for game over here
            print("Board is full...")
            return True
        else:
            print("Keep playing!")
            return False
            