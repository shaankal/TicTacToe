
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
   
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
   
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])
    
def player_move(board):
    while True:
        try:
            move = input("Enter your move (row and column): ")
            row, col = int(move[0]), int(move[1])
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("This cell is already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2.")

def computer_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                return

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        # Player's move
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # Computer's move
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
