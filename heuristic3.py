# Heuristic-3 is strongest opponent.
# It plays very well even if depthlimit is 1.

# We check what is the longest line of red or black stones we can make in current table scenario.
# Notice we are considering the utility of next move.

"""

For example consider the table:
| | | | | | | | |
| | | | | | | | |
|R|B| | | | | | |
|R|B| | | | | |B|
|R|R|R|B|B| | |R|
|B|B|B|R|R|R| |R|
|B|R|B|B|B|R| |R|

Here, we consider the slots represented by letter 'X'.
| | | | | | | | |
|X|X| | | | | | |
|R|B| | | | | |X|
|R|B|X|X|X| | |B|
|R|R|R|B|B|X| |R|
|B|B|B|R|R|R| |R|
|B|R|B|B|B|R|X|R|

We compute the length of the largest line we can make if we place
R or B into these X slots. We then compute balance accordingly.


We use 30^max_len
It is solely depends on my observation.
10 --> playing without very much attention. 
50 --> playing too safe.
30 --> fine.

"""

class Heuristic3:
    @staticmethod
    def evaluate(table):
        balance = 0
        for col in range(8):
            if table[0][col]!=" ":
                continue

            row = 0
            while row+1<7 and table[row+1][col]==" ":
                row = row + 1
            #print("R:"+str(Heuristic3.getmax_profit(table,row,col,"R")))
            balance = balance + Heuristic3.getmax_profit(table,row,col,"R")
            #print("B:"+str(-1 * Heuristic3.getmax_profit(table,row,col,"B")))
            balance = balance - Heuristic3.getmax_profit(table,row,col,"B")
        return balance
    

    @staticmethod
    def getmax_profit(table,i,j,color):
        return 30**(max(
            min(4,Heuristic3.count_right_increasing_diagonal(table,i,j,color)+Heuristic3.count_left_increasing_diagonal(table,i,j,color)),
            min(4,Heuristic3.count_right_decreasing_diagonal(table,i,j,color)+Heuristic3.count_left_decreasing_diagonal(table,i,j,color)),
            min(4,Heuristic3.count_below(table,i,j,color)),
            min(4,Heuristic3.cout_right_horizontal(table,i,j,color)+Heuristic3.count_left_horizontal(table,i,j,color))
        )+1)


    """
       *
      *
     *
    o
    """
    @staticmethod
    def count_right_increasing_diagonal(table,i,j,color):
        if i-1>=0 and j+1<8 and table[i-1][j+1]==color:
            if i-2>=0 and j+2<8 and table[i-2][j+2]==color:
                if i-3>=0 and j+3<8 and table[i-3][j+3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0


    """
    o
     *
      *
       *
    """
    @staticmethod
    def count_right_decreasing_diagonal(table,i,j,color):
        if i+1<7 and j+1<8 and table[i+1][j+1]==color:
            if i+2<7 and j+2<8 and table[i+2][j+2]==color:
                if i+3<7 and j+3<8 and table[i+3][j+3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    
    
    """
       o
      *
     *
    *
    """
    @staticmethod
    def count_left_increasing_diagonal(table,i,j,color):
        if i+1<7 and j-1>=0 and table[i+1][j-1]==color:
            if i+2<7 and j-2>=0 and table[i+2][j-2]==color:
                if i+3<7 and j-3>=0 and table[i+3][j-3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    

    """
    *
     *
      *
       o
    """
    @staticmethod
    def count_left_decreasing_diagonal(table,i,j,color):
        if i-1>=0 and j-1>=0 and table[i-1][j-1]==color:
            if i-2>=0 and j-2>=0 and table[i-2][j-2]==color:
                if i-3>=0 and j-3>=0 and table[i-3][j-3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0


    @staticmethod
    def cout_right_horizontal(table,i,j,color):
        if j+1<8 and table[i][j+1]==color:
            if j+2<8 and table[i][j+2]==color:
                if j+3<8 and table[i][j+3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    

    @staticmethod
    def count_left_horizontal(table,i,j,color):
        if j-1>=0 and table[i][j-1]==color:
            if j-2>=0 and table[i][j-2]==color:
                if j-3>=0 and table[i][j-3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    

    @staticmethod
    def count_below(table,i,j,color):
        if i+1<7 and table[i+1][j]==color:
            if i+2<7 and table[i+2][j]==color:
                if i+3<7 and table[i+3][j]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
