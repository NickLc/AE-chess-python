import chess
from score import score

# Initial values of Aplha and Beta  
MAX, MIN = 1000, -1000 
  
# Returns optimal value for current player  
#(Initially called for root and maximizer)  
def minimax(depth, nodeIndex, maximizingPlayer, boards, alpha, beta):  
   
    # Terminating condition. i.e  
    # leaf node is reached  
    if depth == 3:  
        return score(boards[nodeIndex])  
  
    if maximizingPlayer:  
       
        best = MIN 
  
        # Recur for left and right children  
        for i in range(0, 2):  
              
            val = minimax(depth + 1, nodeIndex * 2 + i,  
                          False, boards, alpha, beta)  
            best = max(best, val)  
            alpha = max(alpha, best)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
           
        return best  
       
    else: 
        best = MAX 
  
        # Recur for left and  
        # right children  
        for i in range(0, 2):  
           
            val = minimax(depth + 1, nodeIndex * 2 + i,  
                            True, boards, alpha, beta)  
            best = min(best, val)  
            beta = min(beta, best)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
           
        return best  
       
# Driver Code  
if __name__ == "__main__":  
   
    board = chess.Board("r1bqkb1r/pp1p1Qpp/p1n2n2/4p3/2B1P3/2PP4/2PP1PPP/RNB1K1NR b KQkq - 0 4")
    boards = [3, 1, 6, 9, 1, 2, 0, -1]   

    print("The optimal value is :", minimax(0, 0, True, boards, MIN, MAX))  
      
