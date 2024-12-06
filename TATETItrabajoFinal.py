import random

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Función para verificar si hay un ganador
def check_win(board, player):
    # Verificar filas, columnas y diagonales
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Función para verificar si hay un empate
def check_draw(board):
    return all([cell != " " for row in board for cell in row])

# Función para obtener el movimiento del jugador
def get_player_move(board):
    while True:
        try:
            move = int(input("Ingrese su movimiento (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move // 3][move % 3] != " ":
                raise ValueError
            return move // 3, move % 3
        except ValueError:
            print("Movimiento inválido. Inténtelo de nuevo.")

# Función para obtener el movimiento de la computadora
def get_computer_move(board):
    while True:
        move = random.randint(0, 8)
        if board[move // 3][move % 3] == " ":
            return move // 3, move % 3

# Función principal para jugar
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # El jugador es X, la compu es O

    while True:
        print_board(board)
        if current_player == "X":
            row, col = get_player_move(board)
        else:
            row, col = get_computer_move(board)
        
        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"¡{current_player} ha ganado!")
            break
        elif check_draw(board):
            print_board(board)
            print("¡Es un empate!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()