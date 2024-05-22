import chess
import random
openings = open ("D:\Code Folder\Python\PythonCodePractice\pygame_3\openings.txt", "r")
openings = openings.readlines()
Nf3openings = open ("Nf3openings.txt", "a")

def listToString(s): 
    
    str1 = " " 
    
    return (str1.join(s))

for line in openings:
    happy = line.split()
    happy.append("\n")
    if happy[0] == "Nf3":
        cool = listToString(happy)
        Nf3openings.write(cool)


def test():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3] 
    inc = 3
    print(list1[0:inc])
    if list1[inc] == list2[inc]:
        print("yes")
    else:
        print("no")

board = chess.Board()

pieces = {
    "p": 10,
    "n": 30, 
    "b": 30, 
    "r": 50,
    "q": 90,
    "k": 0
}

def moveorder(board):
    board.push_san("e4")
    print(board.fen())
    print(board)
    score = 0
    cdict = {}
    for move in board.legal_moves:
        if board.is_capture(move):
            #en passant cause the target square had no piece
            try:
                pieceFrom = board.piece_at(move.from_square)
                pieceTo = board.piece_at(move.to_square)
                piece_symbol_fr = pieceFrom.symbol().lower()
                piece_symbol_to = pieceTo.symbol().lower()
                score += pieces[piece_symbol_to] - pieces[piece_symbol_fr]
                cdict[move] = score
                score = 0
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
    new_move_order = list(sort.keys())
    return new_move_order

#if there is a capture move evaluate the position again, it's basically quiescence search
def quiesce(alpha, beta, board):
    fen = board.fen()
    if transitionTable.get(fen, 0) == 0:
        score = evaluate(board)
        transitionTable[fen] = score
    else:
        score = transitionTable.get(fen, 0)
    if score >= beta:
        return beta
    alpha = max(alpha, score)
    newOrder = moveorder(board)
    for move in newOrder:
        if board.is_capture(move):
            board.push(move)
            score = -quiesce(-beta, -alpha, board)
            board.pop()
            if score >= beta:
                return beta
            alpha = max(alpha, score)
    return alpha

def organizeList(list):
    newList = []
    for com in list:
        newList.insert(0, com)
    return newList

print(moveorder(board))
















    
    

