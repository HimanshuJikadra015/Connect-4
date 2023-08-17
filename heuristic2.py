# Heuristic-2 is moderate opponent.

#In heuristic3 we were peforming computations on empty slots with largest row values, i.e., the next moves.

# But here, we consider all slots.
# Working of Heuristic-2:
# If there are many R stones close to each other than it is good.
# If there are many B stones close to each other than it is bad.

# We count Rs and Bs adjacent to each other.
# At the end subtract values and return.

class Heuristic2:
    @staticmethod
    def evaluate(table):
        redadj = 0
        blackadj = 0
        for row in range(7):
            for col in range(8):
                if table[row][col]=="R":
                    redadj = redadj + Heuristic2.count_adjacents(table,row,col,"R")
                elif table[row][col]=="B":
                    blackadj = blackadj + Heuristic2.count_adjacents(table,row,col,"B")
        return redadj-blackadj
    

    @staticmethod
    def count_adjacents(table,i,j,color):
        return (
            Heuristic2.count_right_increasing_diagonal(table,i,j,color)+
            Heuristic2.count_left_increasing_diagonal(table,i,j,color)+
            Heuristic2.count_right_decreasing_diagonal(table,i,j,color)+
            Heuristic2.count_left_decreasing_diagonal(table,i,j,color)+
            Heuristic2.count_below(table,i,j,color)+
            Heuristic2.cout_right_horizontal(table,i,j,color)+
            Heuristic2.count_left_horizontal(table,i,j,color)
        )

    @staticmethod
    def count_right_increasing_diagonal(table,i,j,color):
        if i-1>=0 and j+1<8 and table[i-1][j+1]==color:
            return 1
        else:
            return 0

    @staticmethod
    def count_right_decreasing_diagonal(table,i,j,color):
        if i+1<7 and j+1<8 and table[i+1][j+1]==color:
            return 1
        else:
            return 0

    @staticmethod
    def count_left_increasing_diagonal(table,i,j,color):
        if i+1<7 and j-1>=0 and table[i+1][j-1]==color:
            return 1
        else:
            return 0

    @staticmethod
    def count_left_decreasing_diagonal(table,i,j,color):
        if i-1>=0 and j-1>=0 and table[i-1][j-1]==color:
            return 1
        else:
            return 0


    @staticmethod
    def cout_right_horizontal(table,i,j,color):
        if j+1<8 and table[i][j+1]==color:
            return 1
        else:
            return 0
    
    @staticmethod
    def count_left_horizontal(table,i,j,color):
        if j-1>=0 and table[i][j-1]==color:
            return 1
        else:
            return 0
    
    @staticmethod
    def count_below(table,i,j,color):
        if i+1<7 and table[i+1][j]==color:
            return 1
        else:
            return 0