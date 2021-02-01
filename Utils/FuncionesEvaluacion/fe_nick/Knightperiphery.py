import re

from .MatrixFenBoard import MatrixFenBoard

class BorderBoard:
  def __init__(self, matrix, level=0):
    self.matrix = matrix
    self.level = level
    self.borders = self.create()

  def create(self):
    borders = []
    A = self.matrix
    level = self.level
    len_border = len(A[0])
    bt = A[level] 
    bb = A[-level-1]
    bl = "".join([i[level] for i in A])
    br = "".join([i[-level-1] for i in A])
    borders = [bt, bb, bl, br]
    borders = [b[level : len_border - level] for b in borders]
    return self._join(borders)
  
  def _join(self, borders):
    new_borders = [borders[0], borders[1], borders[2][1:-1], borders[3][1:-1]]
    return "".join(new_borders)



def Knightperiphery(mfb, color="w", level=0):
  """
  Recibe la matriz del board y color [w: white, b: black]
  Retorna la cantidad de caballos que se encuentran en los extremos
  """
  symbol = "N" if color == "w" else "n"
  num_horses = 0
  borderBoard = BorderBoard(mfb.matrix, level)
  num_horses = len(re.findall(symbol, borderBoard.borders))
  return num_horses

def KnightperipherysAllLevels(mfb, color="w"):
    kinghtperipherys = []
    for i in range(0, 4):
        kinghtperipherys.append(Knightperiphery(mfb, color, i))
    return kinghtperipherys    
