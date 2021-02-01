import chess
import chess.pgn

KASPAROV_GAMES_DB = "Utils/Games/Kasparov.pgn"

def get_games_winner_kasparov():
    kasparov_database_file = open(KASPAROV_GAMES_DB)

    games_winner_kasparov = []
    games_exist_kasparov = True

    while games_exist_kasparov:
        game = chess.pgn.read_game(kasparov_database_file)
        
        if game is None:
            games_exist_kasparov = False
        else:
            if game.headers['Result'] != '*':
                result_splitted = game.headers['Result'].split("-")
            
                if game.headers['Black'].find("Kasparov") != -1 and result_splitted[1] == '1':
                    games_winner_kasparov.append(game)

                if game.headers['White'].find("Kasparov") != -1 and result_splitted[0] == '1':
                    games_winner_kasparov.append(game)

    return games_winner_kasparov


def get_board_and_best_move(game):
    """
    Get from game the board before turn Kasparov and the best move.
    """
    next_games = list(game.mainline_moves())
    size_next_games = len(next_games)
    game_executed = size_next_games // 2

    if game.headers['Black'].find("Kasparov") != -1: 
        if game_executed % 2 == 0: game_executed -= 1
        
    if game.headers['White'].find("Kasparov") != -1: 
        if game_executed % 2 == 1: game_executed -= 1

    new_board = chess.Board()

    for i in range(game_executed):
        new_board.push(next_games[i])

    aux_board = new_board.copy()

    best_move = aux_board.san(next_games[game_executed])

    return new_board, best_move


if __name__ == "__main__":  
    games_winner_kasparov = get_games_winner_kasparov()
    board, best_move = get_board_and_best_move(games_winner_kasparov[0])
    print(board, best_move)