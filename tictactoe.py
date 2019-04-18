class TicTacToe():

    def __init__(self, hashval=0, turn=1):
        self.gamehash = hashval
        self.turn = turn

    def display(self):
        board = self.get_game()

        for i in range(3):
            for j in range(3):
                char = "-"
                if board[i][j] == 1:
                    char = "X"
                elif board[i][j] == 2:
                    char = "O"
                
                print(char + " ", end='')
            
            print()

    def get_hash(self):
        return self.gamehash
    
    def get_game(self):
        board = [[None] * 3 for _ in range(3)]

        tmphash = self.gamehash
        for i in range(9):
            board[i // 3][i % 3] = int(tmphash % 3)

            tmphash /= 3
        
        return board

    @staticmethod
    def to_hash(game):
        hashval = 0
        place = 1

        for i in range(9):
            hashval += place * game[i // 3][i % 3]
            place *= 3
        
        return hashval

    def is_valid(self, move):
        row = move // 3
        col = move % 3
        game = self.get_game()
        return game[row][col] == 0
    
    @staticmethod
    def next_state(state, player, move):
        row = move // 3
        col = move % 3

        game = state.get_game()

        if game[row][col] != 0:
            return -1
        
        game[row][col] = player

        return TicTacToe(TicTacToe.to_hash(game), 2 if player is 1 else 1)

    def get_winner(self):
        board = self.get_game()

        # rows
        for i in range(3):
            if board[i][0] is 0: continue
            
            has_winner = True

            for j in range(3):
                if board[i][j] != board[i][0]: 
                    has_winner = False
                    break
            
            if has_winner:
                return board[i][0]
        
        # cols
        for j in range(3):
            if board[0][j] is 0: continue
            
            has_winner = True

            for i in range(3):
                if board[i][j] != board[0][j]:
                    has_winner = False 
                    break
            
            if has_winner:
                return board[0][j]

        if board[1][1] is 0: return -1 
        
        # downward diagonal
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[1][1]
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return board[1][1]

        counter = 0 # draw

        for i in range(3):
            for j in range(3):
                counter += board[i][j] != 0

        if counter is 9: 
            return 0

        return -1

        
                




    


