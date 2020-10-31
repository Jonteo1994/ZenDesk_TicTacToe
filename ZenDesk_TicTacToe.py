def validateUserChoice(playerName, turn, boardSize,board):                           #used to check that the user has selected a valid cell
    while True:
        try:
            userInput = int(input(playerName + " please select a cell to enter '" + turn + "' :")) #Get user input as an integer
            row = userInput // boardSize                                            #Get the respective board row
            col = userInput % boardSize - 1                                         #Get the respective board column
            if col == -1:
                row = row - 1                                                       #Wrap around to previous row to get the correct cell
                col = boardSize-1
            if userInput == boardSize**2:                                           #For edge case where the largest cell is selected
                row = boardSize - 1
                col = boardSize - 1
                
            if (userInput <= 0 or userInput > boardSize**2 or
                not type(board[row][col]) is int):                                  #User cell selection must be greater than 0 and less than board size squared
                raise ValueError("User selection not within limit or cell occupied")#Row/Col cannot be greater than board size and must be larger than 0
        except ValueError:
            print("Invalid Input! Please select a valid unoccupied cell between 1 and " + str(boardSize**2))
        else:
            board[row][col] = turn                                                  #Assigns the current turn "X" or "O" to the selected valid cell
            return row,col                                                          #Returns the selected row and columns
            break

def initBoard():
    while True:
        try:                                                                                                            #User input validation to ensure board is >3x3 and input is an integer
            boardSize = int(input("Enter desired board size (N): "))
            if not type(boardSize) is int or boardSize < 3:
                raise ValueError("Only Integers and board sizes greater than 3 are allowed")
        except ValueError:
            print("Invalid Input! Please enter a valid number >= 3")
        else:
            boardW = int(boardSize)
            boardH = int(boardSize)
            boardMatrix =  [[int(boardSize*row + col + 1) for col in range(boardW)] for row in range(boardH)]           #Build 2D array and populate with cell coordinates
            printBoard(boardSize, boardMatrix)                                                                          #Displays the board after initialization
            return boardSize, boardMatrix                                                              
            break
        
def printBoard(size, boardMatrix):                                                                                      #Used to print the board and separators
    for x in range(size):
        print(boardMatrix[x])
        print("————"*size)

def scanGrid(r,c,r1,c1,r2,c2,r3,c3, board, ptag):
    #In this function we are scanning a grid around the most recently selected cell and comparing it against 16 possible win combinations
    win = False        #Initialize win state to false
    cell_r1 = r + r1   #Get scannable cell row for cell 1
    cell_r2 = r + r2   #Get scannable cell row for cell 2
    cell_r3 = r + r3   #Get scannable cell row for cell 3
    cell_c1 = c + c1   #Get scannable cell col for cell 1
    cell_c2 = c + c2   #Get scannable cell col for cell 2
    cell_c3 = c + c3   #Get scannable cell col for cell 3
    
    #This is to prevent edge cases where the scanned cell coordinate will equal to -1 which results in wrapping around to the last column/row
    if(cell_r1 >= 0 and cell_r2 >= 0 and cell_r3 >= 0 and cell_c1 >= 0 and cell_c2 >= 0  and cell_c3>= 0):
        #If all selected coordinates are 0 or greater then we test against the selected combination
        if (board[cell_r1][cell_c1] == ptag and board[cell_r2][cell_c2] == ptag and board[cell_r3][cell_c3] == ptag): win = True
        
    return win

def checkWin(row, col, board, ptag, w):
    #Determine win conditions based on a 3x3 grid centered around most recently chosen cell
    gameWon = False                 #Initialize game win state to false unless it passes winning conditions below
    for x in range(16):             #Total of 16 win combinations represented by "x" stored in 2D array "w"
        try:
            gameWon = scanGrid(row,col,w[x][0],w[x][1],w[x][2],w[x][3],w[x][4],w[x][5],board,ptag) #Scan each combination until a win is found
        except IndexError:          #We use this to skip the win selection when the index is out as it will not be a winning combination
            pass
        else:
            if gameWon == True: break

    return gameWon      #Returns true if any of the above conditions are fufilled indicating at 3 symbols in a row have been done

def buildWinCond():
    #Build list containing total of 16 combinations winninable in a 3x3 grid
    winCond = [[0 for x in range(6)] for y in range(0)]     #Initialize 2D array
    winCond.append([-1,-1,-1,0,-1,1])           #Horizontal 1
    winCond.append([0,-1,0,0,0,1])              #Horizontal 2
    winCond.append([1,-1,1,0,1,1])              #Horizontal 3
    winCond.append([0,-2,0,-1,0,0])             #Horizontal Left
    winCond.append([0,0,0,1,0,2])               #Horizontal Right
    
    winCond.append([-1,-1,0,-1,1,-1])           #Vertical 1
    winCond.append([-1,0,0,0,1,0])              #Vertical 2
    winCond.append([-1,1,0,1,1,1])              #Vertical 3
    winCond.append([-2,0,-1,0,0,0])             #Vertical Top
    winCond.append([0,0,1,0,2,0])               #Vertical Bottom
    
    winCond.append([-1,-1,0,0,1,1])             #Diagonal 1
    winCond.append([-1,1,0,0,1,-1])             #Diagonal 2
    winCond.append([-2,-2,-1,-1,0,0])           #Diagonal Top Left
    winCond.append([-2,2,-1,1,0,0])             #Diagonal Top Right
    winCond.append([2,-2,1,-1,0,0])             #Diagonal Bottom Left
    winCond.append([2,2,1,1,0,0])               #Diagonal Bottom Right
    return winCond

def main():
    while True: #Used to control the game restarting
        print("----------Welcome to TicTacToe ZenDesk----------")
        print("\nThere will be 2 players in this game Player 'X' and Player 'O'.\nPlayer 'X' will go first followed by player 'O'\n")
        print("The first player to get 3 of their symbols in a row will win")
        print("The game will be a draw if both players run out of turns")
        
        playerNameX = str(input("Player X please input your name: "))
        playerNameY = str(input("Player O please input your name: "))
        
        boardInfo = initBoard()                 #Initialize the board details
        boardSize = boardInfo[0]                #Get the selected size of the board
        board = boardInfo[1]                    #Get the 2x2 matrix representing the board
        
        winConditionList = buildWinCond()       #Build the winnable combinations for 3x3 grid
        
        #User Turns
        turnCount = 0                           #Initialize start of the turns
        for turnCount in range(boardSize**2):   #There will be at max only the board size squared number of turns if this is reached with no winner then it is a draw
            if (turnCount%2) == 0:              #Player X will be on even turns/ Player O will be on odd turns
                ptag = "X"
                userBoardInput = validateUserChoice(playerNameX,ptag,boardSize,board)  #Returns the selected row/coordinate from player after validation
            else:
                ptag = "O"
                userBoardInput = validateUserChoice(playerNameY,ptag,boardSize,board)
            printBoard(boardSize,board)
            row = userBoardInput[0]             #Get the most recent selected cell row
            col = userBoardInput[1]             #Get the most recent selected cell column
            
        #Win Conditions
            if (checkWin(row,col,board,ptag, winConditionList) == True):             #Check the win conditions in a grid around the selected cell
                print("Player '"+ ptag + "' has won!")
                break
            else:
                if (turnCount == boardSize**2-1): print("It's a draw!")             #Game will be drawed when there are no more turns left
                
        while True:                                                                 #Controls game restart mechanism, player has to enter Y/N to decide to exit or restart the game
            restartGame = input("Game has ended, would you like to restart? (Y/N) :")
            if(restartGame == "N" or restartGame == "n"):
                input("Thank you for playing, press enter to exit.")
                return
            elif(restartGame == "Y" or restartGame == "y"):
                print("Game is restarting!\n")
                break
            else:
                print("Please enter either Y or N")

#============Main Flow===========  
main()                  #Call main flow