from tictactoe import TicTacToe
from agent import GameBot

game = TicTacToe()

bot_turn = 2
player_turn = 1 if bot_turn is 2 else 2

bot = GameBot(player=bot_turn)

turn = 1
game.display()

while game.get_winner() == -1:
    print("----------")
    if turn == bot_turn:
        game = TicTacToe.next_state(game, bot_turn, bot.get_move(game))
    else:
        row = int(input("Row: "))
        col = int(input("Column: "))
        print("----------")

        game = TicTacToe.next_state(game, player_turn, row * 3 + col)

    turn = 1 if turn is 2 else 2
    game.display()

if game.get_winner() is 0:
    print("The game was a draw!")
else:
    print("Player {} wins!".format(game.get_winner()))
