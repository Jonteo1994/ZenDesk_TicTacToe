# ZenDesk_TicTacToe
This program allows up to 2 players to play the classic game of TicTacToe on a square board of up to NxN sizes
Win conditions will still be 3 symbols in a row regardless of board size

# How to run ZenDesk TicTacToe
Navigate to ../dist and run "ZenDesk_TicTacToe.exe"

# Game Rules
1. Players will be presented with instructions on how the game is played and asked to enter their names
2. Players will be asked for the desired square board size
3. Players 'X' and 'O' will then take turns to place their respective symbols in the cells
  a. Players must select a cell that is unoccupied and within the board
4. The game ends when either player manages to get 3 cells in a row(horizontally/vertically/diagonally) with their symbol
  a. If there are no cells left and neither player has won the game is determined to be a draw
5. Players are then given an option to either restart or end the game.

# How it works
The tictactoe "Board" is generated in a 2D list and populated with numbers corresponding to their respective cells
An example of a 6x6 board is shown below.

     0    1    2     3   4    5
 --------------------------------
0  | 1	| 2  | 3  |  4 | 5  | 6  |
1  | 13	| 14 | 15 | 16 | 17 | 18 | 
2  | 25	| 26 | 27 | 28 | 29 | 30 |
3  | 37	| 38 | 39 | 40 | 41 | 42 | 
4  | 49	| 50 | 51 | 52 | 53 | 54 |
5  | 61	| 62 | 63 | 64 | 65 | 66 |

Whenever a user inputs a symbol into a cell, the program checks within 2 cells in 8 cardinal directions and compares it against a generated list of 16 possible combinations
This methodology ensures that regardless of the board size, computational time will be the same for each winning condition check allowing the program to be highly scalable.
When a winning combination is detected, the program ends and displays the winner.
Players are then presented with an option to either restart the game or end the program.
