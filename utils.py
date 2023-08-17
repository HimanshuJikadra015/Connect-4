class Helper:
    @staticmethod
    def initialize_table():
        n = 7
        m = 8
        table = [[" "] * m for i in range(n)]
        return table


    @staticmethod
    def print_table(table):
       # print the table.
        for i in range(8):
            print(" "+str(i+1),end="")
        print(" ")

        for i in range(7):
            for j in range(8):
                print("|" + table[i][j],end="")
            print("|")
        
        for i in range(8):
            print(" "+str(i+1),end="")
        print(" ")
    

    @staticmethod
    def valid_column_number(table,col):
        # to check if the entered column number is valid.
        col = str(col)
        if col.isnumeric()==False:
            return False

        col = int(col)
        if col <= 0 or col>8:
            return False
        
        if table[0][col-1]!=" ":
            return False
        
        return True


    @staticmethod
    def perform_move(table,col,isRed):
        col = col - 1
        for i in (6,5,4,3,2,1,0):
            if table[i][col]==" ":
                table[i][col] = "R" if (isRed) else "B"
                return i


    @staticmethod
    def no_more_moves(table):
        for col in range(8):
            if table[0][col]==" ":
                return False
        return True


    @staticmethod
    def is_winner(table,isRed):
        check = "R" if isRed else "B"
        for i in range(7):
            count = 0
            for j in range(8):
                if table[i][j]==check:
                    count = count+1
                    if count==4:
                        return True
                else:
                    count = 0
        
        for j in range(8):
            count = 0
            for i in range(7):
                if table[i][j]==check:
                    count = count+1
                    if count==4:
                        return True
                else:
                    count = 0
        
        for i in range(4):
            for j in range(5):
                if table[i][j]==check and table[i+1][j+1]==check and table[i+2][j+2]==check and table[i+3][j+3]==check:
                    return True

        for i in range(4):
            for j in range(3,8):
                if table[i][j]==check and table[i+1][j-1]==check and table[i+2][j-2]==check and table[i+3][j-3]==check:
                    return True
        return False

