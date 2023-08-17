# Himanshu Jikadra
# CSE 3rd Year, ITNU.
# Project Title: Connect 4 game using Min-Max Algorithm in game theory.

from utils import Helper
from heuristic1 import Heuristic1
from heuristic2 import Heuristic2
from heuristic3 import Heuristic3
import time

INF = 1000
MININF = -1000

# Our heuristic functions.
# h1 is novice (noob), h2 is apprentice (intermediate), h3 is expert (pro).
def h1(table):
    return Heuristic1.evaluate(table)

def h2(table):
    return Heuristic2.evaluate(table)

def h3(table):
    return Heuristic3.evaluate(table)


# Minimax algorithm with Alpha Beta prunnning

# ALGORITHM IS THAT WE GO TO THE DEEPEST NODE BY CONSIDERING DEPTH LIMIT.
# AT THIS LEVEL, WE EVALUATE THE HEURISTIC VALUES OF THE STATES, 
# WE ONLY PERFORM THESE EVALUATIONS ON DEPTH LIMIT LEVEL. 
# THEN APPLYING ALPHA BETA PRUNNING BY USING THESE EVALUATION VALUES.

# RED --> MAXIMIZER & PLAYS FIRST.
# BLACK --> MINIMIZER & PLAYS SECOND.

# implementation of min-max algorithm.
def minimax(table,depth,depthlim,isRed,alpha,beta,heuristic_type):
    if depth == depthlim:
        if heuristic_type==1:
            return h1(table)
        elif heuristic_type==2:
            return h2(table)
        else:
            return h3(table)

    if isRed: # Red is playing so maximize profit.
        bestVal = MININF
        bestplay = -1 # Best column.
        for column in range(1,9):
            if table[0][column-1]!=" ":
                continue
            row = Helper.perform_move(table,column,isRed)
            if Helper.is_winner(table,isRed):
                bestVal = INF
                bestplay = column
                table[row][column-1] = " "
                break
            value = minimax(table,depth+1,depthlim,False,alpha,beta,heuristic_type)
            table[row][column-1] = " "
            #bestVal = max(bestVal, value)
            if bestVal <= value:
                bestplay = column
                bestVal = value
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        if depth==0:
            Helper.perform_move(table,bestplay,isRed)
        return bestVal
    
    else: # Red is playing so minimize red's profit.
        bestVal = INF
        bestplay = -1 # Best column.
        for column in range(1,9):
            if table[0][column-1]!=" ":
                continue
            row = Helper.perform_move(table,column,isRed)
            if Helper.is_winner(table,isRed):
                bestVal = MININF
                bestplay = column
                table[row][column-1] = " "
                break
            value = minimax(table,depth+1,depthlim,True,alpha,beta,heuristic_type)
            table[row][column-1] = " "
            #bestVal = min(bestVal, value)
            if bestVal >= value:
                bestplay = column
                bestVal = value
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        if depth==0:
            Helper.perform_move(table,bestplay,isRed)
        return bestVal

# function for ai move.
def get_AI_move(table,isRed,depthlim,heuristic_type):
    # call minimax function and print table.
    Helper.print_table(table)
    print("AI is thinking...")
    minimax(table,0,depthlim,isRed,MININF,INF,heuristic_type)
    print("\n\n\n\n\n\n\n\n")
    
# function for human move.
def get_human_move(table,isRed):
    while True:
        # column number the human wants to play.
        Helper.print_table(table)
        if isRed:
            print("Red will play.")
        else:
            print("Black will play.")
        col = input("Enter the column number you want to place.\n")

        if Helper.valid_column_number(table,col)==False:
            print("\n\n\n\n\n\n\n\n")
            print("Invalid move! Please try again.")
            continue
        col = int(col)

        Helper.perform_move(table,col,isRed)
        return
            
# for human vs human game.
def human_human():
    table = Helper.initialize_table()
    # call get_human_move() function turn by turn.
    for turn in range(56):
        print("\n\n\n\n\n\n\n\n")
        if turn%2==0:
            get_human_move(table,True)
            if Helper.is_winner(table,True):
                print("\n\n\n\n\n\n\n\n")
                Helper.print_table(table)
                print("RED WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
        else:
            get_human_move(table,False)
            if Helper.is_winner(table,False):
                print("\n\n\n\n\n\n\n\n")
                Helper.print_table(table)
                print("BLACK WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
    
    print("\n\n\n\n\n\n\n\n")
    Helper.print_table(table)
    print("DRAW!!!",end="")
    ch = input(" Enter anything to start a new game.\n")
        

# for human vs ai game.
def human_ai():
    print("\n\n\n\n\n\n\n\n")
    color = 0
    # ask color human wants to play.
    while color == 0:
        print("1. Red")
        print("2. Black")
        ch = input("Enter index of your color.\n")
        match ch:
            case "1":
                color = 1
            case "2":
                color = 2
            case _:
                print("\n\n\n\n\n\n\n\n")
                "Invalid input. Please try again."
                continue

    print("\n\n\n\n\n\n\n\n")
    heuristic_type = 0
    # ask difficulty of heuristic function.
    while heuristic_type == 0:
        print("1. Novice")
        print("2. Apprentice")
        print("3. Expert")
        ch = input("Enter the heuristic type for AI.\n")
        match ch:
            case "1":
                heuristic_type = 1
            case "2":
                heuristic_type = 2
            case "3":
                heuristic_type = 3
            case _:
                print("\n\n\n\n\n\n\n\n")
                "Invalid input. Please try again."
                continue
    
    print("\n\n\n\n\n\n\n\n")
    depthlim = 0
    # ask the depth limit for AI.
    # more depth limit more powerful move.
    while depthlim == 0:
        print("1 to 3: Novice")
        print("4 to 6: Apprentice")
        print("7 to 9: Expert")
        ch = input("Enter the depth level for AI.\n")
        if ch in ("1","2","3","4","5","6","7","8","9"):
            depthlim = int(ch)
        else:
            print("\n\n\n\n\n\n\n\n")
            "Invalid input. Please try again."

    # call get_human_move() and get_AI_move() functions turn by turn.
    table = Helper.initialize_table()
    for turn in range(56):
        print("\n\n\n\n\n\n\n\n")
        if turn%2==0:
            if color==1:
                get_human_move(table,True)
            else:
                get_AI_move(table,True,depthlim,heuristic_type)

            if Helper.is_winner(table,True):
                print("\n\n\n\n\n\n\n\n")
                Helper.print_table(table)
                print("RED WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
        else:
            if color==2:
                get_human_move(table,False)
            else:
                get_AI_move(table,False,depthlim,heuristic_type)

            if Helper.is_winner(table,False):
                print("\n\n\n\n\n\n\n\n")
                Helper.print_table(table)
                print("BLACK WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
    
    print("\n\n\n\n\n\n\n\n")
    Helper.print_table(table)
    print("DRAW!!!",end="")
    ch = input(" Enter anything to start a new game.\n")

# for ai vs ai game.
def ai_ai():

    # ask depth limit and heuristic function types for each AI.
    print("\n\n\n\n\n\n\n\n")
    heuristic_type_red = 0
    while heuristic_type_red == 0:
        print("1. Novice")
        print("2. Apprentice")
        print("3. Expert")
        ch = input("Enter the heuristic type for Red AI.\n")
        match ch:
            case "1":
                heuristic_type_red = 1
            case "2":
                heuristic_type_red = 2
            case "3":
                heuristic_type_red = 3
            case _:
                print("\n\n\n\n\n\n\n\n")
                "Invalid input. Please try again."
                continue
    
    print("\n\n\n\n\n\n\n\n")
    depthlim_red = 0
    while depthlim_red == 0:
        print("1 to 3: Novice")
        print("4 to 6: Apprentice")
        print("7 to 9: Expert")
        ch = input("Enter the depth level for Red AI.\n")
        if ch in ("1","2","3","4","5","6","7","8","9"):
            depthlim_red = int(ch)
        else:
            print("\n\n\n\n\n\n\n\n")
            "Invalid input. Please try again."

    print("\n\n\n\n\n\n\n\n")
    heuristic_type_black = 0
    while heuristic_type_black == 0:
        print("1. Novice")
        print("2. Apprentice")
        print("3. Expert")
        ch = input("Enter the heuristic type for Black AI.\n")
        match ch:
            case "1":
                heuristic_type_black = 1
            case "2":
                heuristic_type_black = 2
            case "3":
                heuristic_type_black = 3
            case _:
                print("\n\n\n\n\n\n\n\n")
                "Invalid input. Please try again."
                continue
    
    print("\n\n\n\n\n\n\n\n")
    depthlim_black = 0
    while depthlim_black == 0:
        print("1 to 3: Novice")
        print("4 to 6: Apprentice")
        print("7 to 9: Expert")
        ch = input("Enter the depth level for Black AI.\n")
        if ch in ("1","2","3","4","5","6","7","8","9"):
            depthlim_black = int(ch)
        else:
            print("\n\n\n\n\n\n\n\n")
            "Invalid input. Please try again."

    # both ai plays turn by turn.
    table = Helper.initialize_table()
    for turn in range(56):
        print("\n\n\n\n\n\n\n\n")
        if turn%2==0:
            get_AI_move(table,True,depthlim_red,heuristic_type_red)
            if Helper.is_winner(table,True):
                print("\n\n\n\n\n\n\n\n")
                Helper.print_table(table)
                print("RED WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
            print("Red AI is played.")
        else:
            get_AI_move(table,False,depthlim_black,heuristic_type_black)
            if Helper.is_winner(table,False):
                print("\n\n\n\n\n\n\n\n")
                Helper.print_table(table)
                print("BLACK WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
            print("Black AI is played.")
        Helper.print_table(table)
        time.sleep(1)
    
    print("\n\n\n\n\n\n\n\n")
    Helper.print_table(table)
    print("DRAW!!!",end="")
    ch = input(" Enter anything to start a new game.\n")


# function for initializing game.
def start():
    # printing out the menu to ask game type.
    print("\n\n\n\n\n\n\n\n")
    while True:
        print("**********************")
        print("*                    *")
        print("*    CONNECT FOUR    *")
        print("*                    *")
        print("**********************\n")
        print("1. Human vs Human")
        print("2. Human vs AI")
        print("3. AI vs AI\n")
        ch = input("Enter the index you want to play.\n")

        match ch:
            case "1":
                human_human()
                print("\n\n\n\n\n\n\n\n")
            case "2":
                human_ai()
                print("\n\n\n\n\n\n\n\n")
            case "3":
                ai_ai()
                print("\n\n\n\n\n\n\n\n")
            case _:
                print("\n\n\n\n\n\n\n\n")
                print("Invalid input. Please only enter the index of the game.")

# start the game.
start()
table = []

Helper.print_table(table)
minimax(table,0,1,True,MININF,INF,1)
print("Result:")
Helper.print_table(table)