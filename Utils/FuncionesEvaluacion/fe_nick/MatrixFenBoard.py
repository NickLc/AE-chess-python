class MatrixFenBoard:
  def __init__(self, board):
    self.matrix = self.createMatrix(board) 

  def createMatrix(self, board):
    fen = board.fen()
    fen_split = fen.split(" ")[0].split("/")
    fen_matrix = []
    for fen_row in fen_split:
      new_fen_row = ''
      for i in fen_row:
        try:
          new_fen_row += ' '*int(i)
        except:
          new_fen_row += i
      fen_matrix.append(new_fen_row)
    return fen_matrix

  def getPiece(self, pos_tuple):
    r,c = pos_tuple
    return self.matrix[r][c]