import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] 

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("-" * 9)

    def available_moves(self):
        return [i for i, mark in enumerate(self.board) if mark == ' ']

    def make_move(self, position, player):
        self.board[position] = player

    def is_winner(self, player):
        for i in range(0, 9, 3):
            if all(self.board[i + j] == player for j in range(3)):
                return True
            if all(self.board[i + j] == player for j in range(0, 7, 3)):
                return True

        if all(self.board[i] == player for i in range(0, 9, 4)) or all(self.board[i] == player for i in range(2, 7, 2)):
            return True

        return False

    def is_full(self):
        return ' ' not in self.board

    def game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()


class AIPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game):
        if self.symbol == 'X':
            _, move = self.maximize(game)
        else:
            _, move = self.minimize(game)
        return move

    def maximize(self, game, alpha=float('-inf'), beta=float('inf')):
        if game.game_over():
            return self.evaluate(game)

        max_eval = float('-inf')
        best_move = None

        for move in game.available_moves():
            game.make_move(move, self.symbol)
            eval, _ = self.minimize(game, alpha, beta)
            game.make_move(move, ' ') 
            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, max_eval)
            if alpha >= beta:
                break

        return max_eval, best_move

    def minimize(self, game, alpha=float('-inf'), beta=float('inf')):
        if game.game_over():
            return self.evaluate(game)

        min_eval = float('inf')
        best_move = None

        for move in game.available_moves():
            game.make_move(move, 'O' if self.symbol == 'X' else 'X')
            eval, _ = self.maximize(game, alpha, beta)
            game.make_move(move, ' ') 

            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, min_eval)
            if beta <= alpha:
                break

        return min_eval, best_move

    def evaluate(self, game):
        if game.is_winner(self.symbol):
            return 1
        elif game.is_winner('O' if self.symbol == 'X' else 'X'):
            return -1
        else:
            return 0


def human_player_move(game):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in game.available_moves():
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")


def play_game():
    game = TicTacToe()
    human_symbol = input("Choose your symbol (X or O): ").upper()
    ai_symbol = 'X' if human_symbol == 'O' else 'O'
    
    if ai_symbol == 'X':
        print("AI goes first:")
        ai = AIPlayer(ai_symbol)
        ai_move = ai.get_move(game)
        game.make_move(ai_move, ai_symbol)
        game.print_board()

    while not game.game_over():
        # Human player's move
        human_move = human_player_move(game)
        game.make_move(human_move, human_symbol)
        game.print_board()

        if game.game_over():
            break

        ai = AIPlayer(ai_symbol)
        ai_move = ai.get_move(game)
        game.make_move(ai_move, ai_symbol)
        print("AI's move:")
        game.print_board()

    if game.is_winner(human_symbol):
        print("Congratulations! You win!")
    elif game.is_winner(ai_symbol):
        print("AI wins. Better luck next time!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()