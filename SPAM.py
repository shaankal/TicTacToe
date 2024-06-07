import random

# Function to print the Tic Tac Toe board
def print_board(board):
    print("  0   1   2")
    for idx, row in enumerate(board):
        print(idx, " | ".join(row))
        if idx < 2:
            print("  ---+---+---")

# Function to check for a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Function for the player's move
def player_move(board):
    while True:
        try:
            move = input("Enter your move (row and column) or 'q' to quit: ").strip().lower()
            if move == 'q':
                return False
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("This cell is already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2 separated by a space, or 'q' to quit.")
    return True

# Function for the computer's move
def computer_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    move = random.choice(available_moves)
    board[move[0]][move[1]] = "O"

# Main game function
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! To place a move, put a number in from 0 - 2, insert a space (to get the space, click alpha -> 0), then add the next number. Ex: 1 2 represents row 1, column 2.")

    while True:
        print_board(board)
        
        if not player_move(board):
            print("Thank you for playing! Goodbye!")
            break

        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win! To play again, use the arrows on the calculator to find the play_game function, then run it again!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        computer_move(board)
        
        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins! Better luck next time. To play again, use the arrows on the calculator to find the play_game function, then run it again!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie! To play again, use the arrows on the calculator to find the play_game function, then run it again!")
            break

if __name__ == "__main__":
    play_game()
