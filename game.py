def print_board(board):
    for row in board:
    print("Board Layout:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        print("-" * 5)
        if i < 2:
            print("-" * 5)
    print("Instructions: Input the numbers with a space (e.g., '1 2' for row 1, column 2), to get the space, use Alpha -> 0")

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

@@ -68,5 +71,15 @@ def play_game():
            print("It's a tie!")
            break

    while True:
        quit_game = input("Do you want to quit the game? (yes/no): ").lower()
        if quit_game in ['yes', 'y']:
            print("Thank you for playing! Goodbye!")
            break
        elif quit_game in ['no', 'n']:
            play_game()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()
