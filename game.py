def print_board(board):
    print("Board Layout:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print("Instructions: Input the numbers as shown (e.g., '12' for row 1, column 2)")

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

    while True:
        quit_game = input("Do you want to quit the game? (yes/no): ").lower()
        if quit_game in ['yes', 'y']:
            print("Thank you for playing! Goodbye!")
            break
        elif quit_game in ['no', 'n']:
            play_game()
        else
