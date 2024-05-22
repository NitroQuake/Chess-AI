try:
    import chess
    import pygame
except:
    import pip

    pip.main(["install", "pygame"])
    pip.main(["install", "python-chess"])

    import chess
    import pygame
        #a failsafe to import chess and pygame

import random
import chessai

board = chess.Board()

# board.push_uci("e2e4")
# board.push_san("e5")

# san = e4, Nf3
# uci = e2e4, g1f3

p_color = True  # True = white / False = black
alpha = -99999999
beta = 99999999
depth = 3

openings = open ("openings.txt", "r")
openings = openings.readlines()
newOpenings = [] 
moveList = []
inc = 0

while not board.is_game_over():
    if board.turn == p_color:
        move = input("\nEnter a move: ")
        if move == ".":
            moveList.clear()
            inc = 0
            quit("\n\033[91mForcefully Closed Application\033[95m uwu\033[0m\n")
        try:
            moveList.append(move)
            board.push_san(move)
            print("")
            print(board.unicode())
            print("")
        except:
            print("\nIllegal move\n")
    else:
        if p_color == False:
            move = chessai.comMove(board, depth, True, alpha, beta)
                #white
        else:
            #checks opening book 
            if inc == 0:
                inc += 1
            else:
                inc += 2
            for line in openings:
                oMoveList = line.split()
                if oMoveList[0:inc] == moveList[0:inc]:
                    #if inc = 1 then "[0:inc]" looks at the first move"
                    newOpenings.append(oMoveList)
            if not newOpenings == []:
                selectedOpening = random.choice(newOpenings)
                newOpenings.clear()
                move = selectedOpening[inc]
                    #if inc = 1 then "[inc]" looks at the second move"
                moveList.append(move)
            else: 
                move = chessai.comMove(board, depth, False, alpha, beta)  
            #black
            print(move)
            print("")
            board.push_san(move)
            print(board.unicode())
                # Make the AI move

if board.is_game_over():
   if board.is_checkmate():
        if not p_color:
            print("White Wins")
        elif p_color:
            print("Black Wins")
        else: 
            print("Draw")

# move = "f2f4"
# move = board.parse_uci(move)
# board.push_san(move)