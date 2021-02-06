import re

from .Knightperiphery import KnightperipherysAllLevels
from .MatrixFenBoard import MatrixFenBoard
from .Pawn import getAllMetricsPawnsBoard

def getTurnOppositeBoard(board):
    fen = board.fen()
    color = re.findall('\s[bw]\s',fen)[0].replace(' ','')
    color = 'w' if color=='b' else 'b'
    return color 

def get_all_fun_eval_n(board):
    mfb = MatrixFenBoard(board)
    color = getTurnOppositeBoard(board)
    metrics_kps = KnightperipherysAllLevels(mfb, color)
    metrics_pawn = getAllMetricsPawnsBoard(mfb, color)
    scores = metrics_kps + metrics_pawn
    return scores