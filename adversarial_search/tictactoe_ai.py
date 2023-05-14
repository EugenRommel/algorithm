from minimax import find_best_move
from board import Board, Move
from tictactoe import TTTBoard

board: Board = TTTBoard()


def get_player_move() -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input("Enter a legal square (0-8):"))
        player_move = Move(play)
    return player_move


if __name__ == "__main__":
    print(board)
    while True:
        human_move: Move = get_player_move()
        board = board.move(human_move)
        print(board)
        if board.is_win:
            print("Human wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
        computer_move: Move = find_best_move(board)
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
