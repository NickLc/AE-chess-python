import chess
from .fe_nick.getAllFunEval import get_all_fun_eval_n
from .fe_victor.getAllFunEval import get_all_fun_eval_v
from .fe_carlos.getAllFunEval import get_all_fun_eval_c

def get_all_fun_eval(board):
    scores = get_all_fun_eval_v(board)
    scores += get_all_fun_eval_n(board)
    scores += get_all_fun_eval_c(board)
    return scores
