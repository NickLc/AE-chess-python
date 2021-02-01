import re
from .MatrixFenBoard import MatrixFenBoard

class Position:
  def __init__(self):
    pass
  
  def get_pos_tuple(self, pos_str):
    pos = pos_str 
    row_board = int(pos[1])
    row_matrix = 8 - row_board
    column_board = pos[0]
    column_matrix = ord(column_board) - ord('a')
    return row_matrix, column_matrix
  
  def get_pos_str(self, pos_tuple):
    pos = pos_tuple
    row_matrix = pos[0]
    row_board = str(8 - row_matrix)
    column_matrix = pos[1]
    column_board = chr(column_matrix + ord('a'))
    return column_board+row_board

  def intoLimit(self, i):
    return True if i>=0 and i<8 else False

  def intoBoard(self, pos_tuple):
    r,c = pos_tuple
    return self.intoLimit(r) and self.intoLimit(c)


class Piece:
  def __init__(self, mfb, pos_str):
    self.mfb = mfb
    self.pos_str = pos_str

  def get_pos_tuple(self):
    return Position().get_pos_tuple(self.pos_str)

  def get_letter(self):
    r,c = self.get_pos_tuple()
    return self.mfb.matrix[r][c]

  def get_color(self):
    letter = self.get_letter()
    color = 'w' if letter.isupper() else 'b' 
    return color

  def get_letter_opposite(self):
    letter = self.get_letter()
    return letter.lower() if letter.isupper() else letter.upper()

  def get_pieces_partner(self):
    color = self.get_color()
    partners = 'rnbqkp' if color=='b' else 'RNBQKP'
    return partners
  
  def get_pieces_enemy(self):
    color = self.get_color()
    enemys = 'RNBQKP' if color=='b' else 'rnbqkp'
    return enemys

  def get_neighbors(self):
    Pos = Position()
    row, col = self.get_pos_tuple()
    posIsNotMid = lambda r,c: True if not (r==0 and c==0) else False

    neighbors = ''
    for r in range(-1,2):
      for c in range(-1,2):
        pr, pc = row+r, col+c
        if Pos.intoBoard((pr,pc)) and posIsNotMid(r,c):
          neighbors += self.mfb.getPiece((pr, pc))
    return neighbors


class Pawn(Piece):
  def __init__(self, mfb, pos_str):
    Piece.__init__(self, mfb, pos_str)
    self.ispawn = self.checkPawn()
    self.isPassPawn = 0

  def checkPawn(self):
    letter = self.get_letter()
    if letter == 'P' or letter == 'p':
      return True
    else:
      #print(f'Err: The piece {letter} is not a pawn')
      return False

  def isoPawn(self):
    if self.ispawn:
      partners = self.get_pieces_partner()
      neighbors = self.get_neighbors()
      neighbors_partner = re.findall(f'[{partners}]', neighbors)
      return 1 if len(neighbors_partner) != 0 else 0 
    else:
      return 0
  
  def doublePawn(self):
    if self.ispawn:
      r,c = self.get_pos_tuple()
      letter = self.get_letter()
      partnersInColum = "".join([row[c] for i, row in enumerate(self.mfb.matrix) if r != i])
      pawn_partnersInColumn = re.findall(f'[{letter}]', partnersInColum)
      return 1 if len(pawn_partnersInColumn) != 0 else 0 
    else:
      return 0

  def passPawn(self):
    if self.ispawn:
      Pos = Position()
      row,col = self.get_pos_tuple()
      letter_opposite = self.get_letter_opposite()
      color = self.get_color()
      range_row_toward = range(row) if color=='w' else range(row+1,8) 
      range_col_toward = range(col-1, col+2)
      piecesToward = ''
      for r in range_row_toward:
        for c in range_col_toward:
          if Pos.intoBoard((r,c)):
            piecesToward += self.mfb.getPiece((r,c))

      pawnEnemyToward = re.findall(f'[{letter_opposite}]', piecesToward)
      value_return = 1 if len(pawnEnemyToward) != 0 else 0 
      self.isPassPawn = value_return
      return value_return
    else:
      return 0
    
  def rookbhdPassPawn(self):
    if self.ispawn:  
      if self.isPassPawn:
        row,col = self.get_pos_tuple()
        color = self.get_color()
        range_row_backward = range(row) if color=='b' else range(row+1,8)
        letter_rook = 'r' if color=='b' else 'R'
        c = col
        piecesBackward = ''
        for r in range_row_backward:
            piecesBackward += self.mfb.getPiece((r,c))
        
        rookBackward = re.findall(f'[{letter_rook}]', piecesBackward)
        return 1 if len(rookBackward) != 0 else 0  
      else:
        #print('Err, pawn is not a passPawn')
        return 0

    else:
      return 0 

  def backwardPawn(self):
    if self.ispawn:  
      Pos = Position()
      row,col = self.get_pos_tuple()
      letter = self.get_letter()
      color = self.get_color()
      pos_row_toward = row-1 if color=='w' else row+1
      pos_tuple = (pos_row_toward, col)
      pieceToward = ''
      if Pos.intoBoard(pos_tuple):
        pieceToward = self.mfb.getPiece(pos_tuple)

      pawnPartnerToward = re.findall(f'[{letter}]', pieceToward)
      return 1 if len(pawnPartnerToward) != 0 else 0
    else:
      return 0 

  def rankPassedPawn(self):
    if self.ispawn:  
      if self.isPassPawn:
        return int(self.pos_str[1])
      else:
        #print('Err, pawn is not a passPawn')
        return 0
    else:
      return 0 

  def blockedPawn(self):
    if self.ispawn:  
      if self.pos_str[0] == 'e' or self.pos_str[0] == 'd':
        Pos = Position()
        row,col = self.get_pos_tuple()

        pieceEmpty = ' '
        color = self.get_color()
        pos_row_toward = row-1 if color=='w' else row+1
        pos_tuple = (pos_row_toward, col)
        pieceToward = ''
        if Pos.intoBoard(pos_tuple):
          pieceToward = self.mfb.getPiece(pos_tuple)

        pieceEmptyToward = re.findall(f'[{pieceEmpty}]', pieceToward)
        return 1 if len(pieceEmptyToward) != 0 else 0
      else:
        return 0
    else:
      return 0 

  def blockedPassedPawn(self):
    if self.ispawn:  
      Pos = Position()
      row,col = self.get_pos_tuple()
      piecesEnemy = self.get_pieces_enemy()
      color = self.get_color()
      pos_row_toward = row-1 if color=='w' else row+1
      pos_tuple = (pos_row_toward, col)
      pieceToward = ''
      if Pos.intoBoard(pos_tuple):
        pieceToward = self.mfb.getPiece(pos_tuple)

      pieceEnemyToward = re.findall(f'[{piecesEnemy}]', pieceToward)
      return 1 if len(pieceEnemyToward) != 0 else 0
    else:
      return 0 

def getAllPositionPawn(mfb, color):
    piece = 'p' if color == 'b' else 'P'
    position = Position()
    posAllPawn = []
    for row in range(8):
      for col in range(8):
        if mfb.matrix[row][col] == piece:
          posAllPawn.append(position.get_pos_str((row,col)))
    
    return posAllPawn

def getAllMetricsPawn(pawn):
  metricsPawns = [
    pawn.isoPawn(),
    pawn.doublePawn(),
    pawn.passPawn(),
    pawn.rookbhdPassPawn(),
    pawn.backwardPawn(),
    pawn.rankPassedPawn(),
    pawn.blockedPawn(),
    pawn.blockedPassedPawn()
  ]
  return metricsPawns

def getAllMetricsPawnsBoard(mfb, color):
  pos_pawns = getAllPositionPawn(mfb, color)
  metrics_pawns = [getAllMetricsPawn(Pawn(mfb, pos)) for pos in pos_pawns]
  metrics = []
  for i in range(len(metrics_pawns[0])):
    sum_metric = 0 
    for j in range(len(metrics_pawns)):
      sum_metric += metrics_pawns[j][i]
    metrics.append(sum_metric)
  return metrics
