import chess
import numpy as np
from Utils.FuncionesEvaluacion.fun_eval import get_all_fun_eval
from Utils.Games.games_Kasparov import get_games_winner_kasparov

class Middle_Game():

    def __init__(self, game, individual):
        self.game = game
        self.individual = individual
        self.next_moves = []
        self.board, self.best_move = self.get_board_and_best_move()
        self.next_boards = self.get_next_boards()
        self.scores = self.get_scores()
        self.best_moves_individual = self.get_best_moves_individual()

    def get_board_and_best_move(self):
        """
        Get from game the board before turn Kasparov and the best move.
        """
        next_games = list(self.game.mainline_moves())
        size_next_games = len(next_games)
        game_executed = size_next_games // 2

        if self.game.headers['Black'].find("Kasparov") != -1: 
            if game_executed % 2 == 0: game_executed -= 1
            
        if self.game.headers['White'].find("Kasparov") != -1: 
            if game_executed % 2 == 1: game_executed -= 1

        new_board = chess.Board()

        for i in range(game_executed):
            new_board.push(next_games[i])

        aux_board = new_board.copy()

        best_move = aux_board.san(next_games[game_executed])

        return new_board, best_move

    def get_next_boards(self):

        next_boards = []
        for move in self.board.legal_moves:
            next_move = self.board.san(move)
            self.next_moves.append(next_move)
            aux_board = self.board.copy()
            aux_board.push_san(next_move)
            next_boards.append(aux_board)
        
        return next_boards
    
    def get_scores(self):
        scores = []
        for board in self.next_boards:
            fun_eval = get_all_fun_eval(board)
            score = np.array(fun_eval) @ np.array(individual)
            scores.append(score)
        return scores

    def get_best_moves_individual(self):
        arr_scores = np.array(self.scores)
        index_max = list(np.where(arr_scores == arr_scores.max())[0]) 
        best_moves_individual = [self.next_moves[i] for i in index_max]
        print(f'best_moves_individual: {best_moves_individual}')
        print(f'best move Kasparov: {self.best_move}')
        return best_moves_individual
        

if __name__ == "__main__": 
    games_winner_kasparov = get_games_winner_kasparov()
    individual = list(np.random.randint(10, size=33))
    middle_game = Middle_Game(games_winner_kasparov[0], individual)