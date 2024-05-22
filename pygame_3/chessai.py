from asyncio.windows_events import NULL
from tokenize import Whitespace
from types import NoneType
import chess
import pygame

tables = {
    "p": [
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [5, 5, 5, 5, 5, 5, 5, 5], 
    [1, 1, 2, 3, 3, 2, 1, 1], 
    [0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5], 
    [0, 0, 0, 2, 2, 0, 0, 0], 
    [0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5], 
    [0.5, 1, 1, -2, -2, 1, 1, 0.5], 
    [0, 0, 0, 0, 0, 0, 0, 0]],
    "n": [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0], 
    [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0], 
    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0], 
    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0], 
    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0], 
    [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0], 
    [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0], 
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]], 
    "b": [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0], 
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], 
    [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0], 
    [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0], 
    [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0], 
    [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0], 
    [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0], 
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]], 
    "r": [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5], 
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5], 
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5], 
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5], 
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5], 
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5], 
    [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]],
    "q": [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0], 
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], 
    [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0], 
    [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5], 
    [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5], 
    [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0], 
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], 
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]],
    "k": [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0], 
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0], 
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0], 
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0], 
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0], 
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0], 
    [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0], 
    [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]]
}

pieces = {
    "p": 10,
    "n": 30, 
    "b": 30, 
    "r": 50,
    "q": 90,
    "k": 0
}


squarePosition = []

#evaluates the board
def evaluate(board):
    score = 0
    for row in range(8):
        for col in range(8):
            square_index = row*8+col
            squarePosition.append(square_index)
            square = chess.SQUARES[square_index]
                #tells all the info of the specific square
            piece = board.piece_at(square)
                #gets the piece of that square

            if piece != None:
                piece_symbol = piece.symbol().lower()
                    #each pieces symbol without unicode is just letters
                
                if piece.color:
                    score += pieces[piece_symbol]
                    score += tables[piece_symbol][row][col]
                else:
                    score -= pieces[piece_symbol]
                    score -= tables[piece_symbol][row][col]

    return score

#transition table
transitionTable = {

}

#if there is a capture move evaluate the position again, it's basically quiescence search
def quiesce(alpha, beta, board, limit, isMaximizing):
    #transition table, stores the evaluation of a position in the "transitionTable" and uses the evaluation score if the position shows up again
    if limit == 3:
        if isMaximizing:
            fen = board.fen()
            if transitionTable.get(fen, 0) == 0:
                stand_pat = evaluate(board)
                transitionTable[fen] = stand_pat
            else:
                stand_pat = transitionTable.get(fen)
            if stand_pat >= beta:
                return beta
            alpha = max(alpha, stand_pat)
            return alpha
        else:
            fen = board.fen()
            if transitionTable.get(fen, 0) == 0:
                stand_pat = evaluate(board)
                transitionTable[fen] = stand_pat
            else:
                stand_pat = transitionTable.get(fen)
            if stand_pat <= alpha:
                return alpha
            beta = min(beta, stand_pat)
            return beta
    
    newOrder = moveorder(board)

    if isMaximizing:
        fen = board.fen()
        if transitionTable.get(fen, 0) == 0:
            stand_pat = evaluate(board)
            transitionTable[fen] = stand_pat
        else:
            stand_pat = transitionTable.get(fen)
        if stand_pat >= beta:
            return beta
        alpha = max(alpha, stand_pat)
        for move in newOrder:
            if board.is_capture(move):
                board.push(move)
                score = quiesce(alpha, beta, board, limit + 1, False)
                board.pop()
                if score >= beta:
                    return beta
                alpha = max(alpha, score)
        return alpha

    else:
        fen = board.fen()
        if transitionTable.get(fen, 0) == 0:
            stand_pat = evaluate(board)
            transitionTable[fen] = stand_pat
        else:
            stand_pat = transitionTable.get(fen)
        if stand_pat <= alpha:
            return alpha
        beta = min(beta, stand_pat)
        for move in newOrder:
            if board.is_capture(move):
                board.push(move)
                score = quiesce(alpha, beta, board, limit + 1, True)
                board.pop()
                if score <= alpha:
                    return alpha
                beta = min(beta, score)
        return beta



#orders moves so alpha beta pruning is more efficient, it organizes based on capture moves and promotions
def moveorder(board):
    score = 0
    cdict = {}
    for move in board.legal_moves:
        if board.is_capture(move):
            #finds the data from the square and target square
            try:
                pieceFrom = board.piece_at(move.from_square)
                pieceTo = board.piece_at(move.to_square)
                piece_symbol_fr = pieceFrom.symbol().lower()
                piece_symbol_to = pieceTo.symbol().lower()
                score += pieces[piece_symbol_to] - pieces[piece_symbol_fr]
                cdict[move] = score
                score = 0
            #en passant cause the target square to have not piece on the target square
            except:
                score = 1
                cdict[move] = score
                score = 0
        elif move.promotion:
            piece_symbol_pr = board.uci(move)
                #turns the move into a string
            movepr = board.parse_uci(piece_symbol_pr)
                #needs to be convert from string to move to work
            score += pieces[piece_symbol_pr.lower()[-1]] - 10
                #gets last character "[-1]" of string which is what piece it promotes to
            cdict[movepr] = score
            score = 0
        else:
            cdict[move] = score
    sort = dict(sorted(cdict.items(), key=lambda x:x[1], reverse = True))
        #sorts the dict by value
    new_move_order = list(sort.keys())
        #turns the dict to a list but only using the keys
    return new_move_order



def minimax(board, depth, isMaximizing, maxDepth, alpha, beta):
        #board, 1, False/True, 2

    #this checks for the current state
    if board.is_checkmate():
        if board.turn:
            return -99999999999999999999
        else: 
            return 999999999999999999999
    elif board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition():
        return 0
    
    #gives the score of the position
    elif depth == maxDepth:
        #evaluates the board as many time until the give maxDepth
        limit = 0
        return quiesce(alpha, beta, board, limit, isMaximizing)
    
    newOrder = moveorder(board)
    
    #2 bots fighting each other 
    if isMaximizing:
        bestScore = -99999999
        for move in newOrder:
            move = board.san(move)
            board.push_san(move)
            score = minimax(board, depth+1, False, maxDepth, alpha, beta)
                #calls the function, depth is being added 1 until it is equal to maxDepth where it is then given a score
            board.pop()
            #sets the bestScore
            if score > bestScore:
                bestScore = score
            #alpha beta pruning
            alpha = max(alpha, score)
            if beta <= alpha: 
                break
        return bestScore
    else:
        bestScore = 99999999
        for move in newOrder:
            move = board.san(move)
            board.push_san(move)
            score = minimax(board, depth+1, True, maxDepth, alpha, beta)
            board.pop()
            if score < bestScore:
                bestScore = score
            beta = min(beta, score)
            if beta <= alpha: 
                break
        return bestScore

def comMove(board, maxDepth, isMaximizing, alpha, beta):
    #board, 2, True/False
    
    if isMaximizing:
        #True which mean white
        bestScore = -99999999
            #this is low because we want the best score possible, it will be set to this whenever it's white's move.
        for move in board.legal_moves:
            move = board.san(move)
                #converts uci to san
            board.push_san(move)
                #makes the move
            score = minimax(board, 1, False, maxDepth, alpha, beta)
                #board, 1, False, 2
            board.pop()
                #undos move
            
            #for every move it will see the score and if that score is better than bestScore it will set it as the bestScore, but can change if there is a better move. It will do this until it finds the bestmove.
            if score > bestScore:
                bestScore = score 
                bestMove = move
    
    else:
        bestScore = 99999999
        for move in board.legal_moves:
            move = board.san(move)
                #converts uci to san
            board.push_san(move)
            score = minimax(board, 1, True, maxDepth, alpha, beta)
            board.pop()
            if score < bestScore:
                bestScore = score 
                bestMove = move

    return bestMove



    