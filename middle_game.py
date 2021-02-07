import chess
import numpy as np
import pandas as pd

def get_fitness_individual(df_fun_eval_turn, best_move, individual):
    good_decisions_taken = 0

    scores = []
    for i in range(len(df_fun_eval_turn)):

        fun_eval = list(df_fun_eval_turn.iloc[i, 1].split(','))
        fun_eval = [int(i) for i in fun_eval]
        score = np.array(fun_eval) @ np.array(individual)
        scores.append(score)

    arr_scores = np.array(scores)
    index_max = list(np.where(arr_scores == arr_scores.max())[0]) 
    next_moves = df_fun_eval_turn.iloc[:,3].values
    best_moves_individual = next_moves[index_max]

    if best_move in best_moves_individual:
        return 1

    else:
        return 0
    """
    try:
        index = best_moves_individual.index(best_move)
        return 1
    except:
        return 0
    """ 
       
def get_best_move(df_games, id_partida):
    return df_games.iloc[id_partida, 1]

def get_df_fun_eval_partida(df_fun_eval, id_partida):
    return df_fun_eval.query('id_partida == @id_partida')

if __name__ == "__main__": 
    df_fun_eval = pd.read_csv('Utils/Data/jugadas_fun_eval.csv', ',', index_col=0)
    df_games = pd.read_csv('Utils/Data/resumen_jugadas.csv', ',', index_col=0)
    id_partida = 4
    
    best_move = get_best_move(df_games, id_partida)
    df_fun_eval_turn = get_df_fun_eval_partida(df_fun_eval, id_partida)
    individual = np.random.randint(10,size=33)

    fitness = get_fitness_individual(df_fun_eval_turn, best_move, individual)
    print("Fitness: ",fitness)
