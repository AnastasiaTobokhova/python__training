def print_board(board):
    """Функция для отображения игрового поля."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, player):
    """Функция для проверки победы игрока."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
        [0, 4, 8], [2, 4, 6]  # Диагонали
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def is_board_full(board):
    """Функция для проверки, заполнено ли поле."""
    return all(cell in ['X', 'O'] for cell in board)


def get_player_move(board):
    """Функция для получения корректного ввода от игрока."""
    while True:
        try:
            move = int(input("Введите номер клетки (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Неверный номер клетки. Попробуйте снова.")
            elif board[move] != ' ':
                print("Эта клетка уже занята. Попробуйте снова.")
            else:
                return move
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 9.")


def play_game():
    """Основная функция для игры."""
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Игрок {current_player}'s ход:")

        move = get_player_move(board)
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} выиграл!")
            break

        if is_board_full(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()
