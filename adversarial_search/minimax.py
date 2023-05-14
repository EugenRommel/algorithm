from board import Board, Piece, Move


def minimax(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8):
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)
    if maximizing:
        best_val: float = float("-inf")
        for move in board.legal_moves:
            result: float = minimax(board.move(move), False, original_player, max_depth - 1)
            best_val = max(result, best_val)
        return best_val
    else:
        worst_val: float = float("inf")
        for move in board.legal_moves:
            result: float = minimax(board.move(move), True, original_player, max_depth - 1)
            worst_val = min(result, worst_val)
        return worst_val


def alphabeta(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8,
              alpha: float = float("-inf"), beta: float = float("inf")) -> float:
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)

    if maximizing:
        for move in board.legal_moves:
            result: float = alphabeta(board.move(move), False, original_player, max_depth - 1,
                                      alpha, beta)
            alpha = max(result, alpha)
            if beta <= alpha:
                break
        return alpha
    else:
        for move in board.legal_moves:
            result: float = alphabeta(board.move(move), True, original_player, max_depth - 1,
                                      alpha, beta)
            beta = min(result, beta)
            if beta <= alpha:
                break
        return beta


def find_best_move(board: Board, max_depth: int = 8) -> Move:
    best_val: float = float("-inf")
    best_move: Move = Move(-1)
    for move in board.legal_moves:
        result: float = alphabeta(board.move(move), False, board.turn, max_depth)
        if result > best_val:
            best_val = result
            best_move = move
    return best_move
