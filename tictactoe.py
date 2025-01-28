
Board_size = 3
empty = " "
player_x = "X"
player_o = "O"
board = [[empty for _ in range(Board_size)] for _ in range(Board_size)]
current_player = player_x

def display_board():
    for row in board:
        print("|".join(row))
        print("-"*(Board_size*2-1))

def is_valid_move(row, col):
    return 0 <= row< Board_size and 0<= col < Board_size and board[row][col] == empty

def make_move(row, col, player):
    if is_valid_move(row, col):
        board[row][col]=player
        return True
    return False

def check_win(player):
    return (
            any(all(cell == player for cell in row) for row in board) or 
            any(all(board[r][c] == player for r in range(Board_size)) for c in range (Board_size)) or
            all(board[i][i] ==player for i in range(Board_size)) or
            all(board[i][Board_size -i -1]== player for i in range(Board_size))
    )
def is_draw():
    return all(board[row][col] != empty for row in range(Board_size) for col in range(Board_size))

def play_game():
    global current_player
    while True:
        display_board()
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if make_move(row, col, current_player):
            if check_win(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break
            elif is_draw():
                display_board()
                print("It's a draw!")
                break
            current_player = player_o if current_player == player_x else player_x
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()

