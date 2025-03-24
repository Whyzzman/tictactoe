def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

board = [[" "]*3 for _ in range(3)]
current_player = "X"

for _ in range(9):
    print_board(board)
    row, col = map(int, input(f"Гравець {current_player}, введіть рядок і стовпець (0-2): ").split())
    if board[row][col] == " ":
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Гравець {current_player} переміг!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Ця клітинка вже зайнята, спробуйте ще раз!")
else:
    print("Нічия!")
