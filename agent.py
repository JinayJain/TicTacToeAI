from tictactoe import TicTacToe

class GameBot():

    def __init__(self, player):
        self.score = [None] * (3 ** 9 + 1)
        self.turn = player

    def get_move(self, state):
        # print(state.get_hash())
        self.minimax(state, self.turn)
        bestmove = -1
        bestscore = 0

        for i in range(9):
            if state.is_valid(i):
                # print("i:",i)
                # print("hash:",TicTacToe.next_state(state, self.turn, i).get_hash())
                tmp = self.score[TicTacToe.next_state(state, self.turn, i).get_hash()]
                # print(tmp)
                if tmp >= bestscore:
                    bestmove = i
                    bestscore = tmp

        return bestmove


    
    def minimax(self, state, player):
        if self.score[state.get_hash()] is not None:
            return self.score[state.get_hash()]


        gamehash = state.get_hash()
        score = self.score[gamehash]


        if state.get_winner() == -1:

            is_max = (player == self.turn)

            for i in range(9):
                if state.is_valid(i):
                    value = self.minimax(TicTacToe.next_state(state, player, i), 2 if player is 1 else 1)

                    if score is None:
                        score = value

                    if is_max:
                        score = max(score, value)
                    else:
                        score = min(score, value)

            self.score[gamehash] = score
            # print("HASHED:",gamehash)
            # print("SCORE:",score)
            return score

        elif state.get_winner() == 0:
            # print("HASHED:",gamehash)
            # print("DRAW!")
            self.score[gamehash] = 0
            return 0
        elif state.get_winner() == self.turn:
            # print("HASHED:",gamehash)
            # print("I WON!")
            self.score[gamehash] = 1
            return 1
        else:
            # print("HASHED:",gamehash)
            # print("I LOST!")
            self.score[gamehash] = -1
            return -1

        

