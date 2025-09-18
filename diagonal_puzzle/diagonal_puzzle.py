# !/usr/bin/env python3

import config

def can_place_slash(board, row, col):
    # Check the top cell
    if row > 0 and board[row - 1][col] == 2:
        return False
    # Check the top right cell
    if row > 0 and col < len(board[0]) - 1 and board[row - 1][col + 1] == 1:
        return False
    # Check the left cell
    if col > 0 and board[row][col - 1] == 2:
        return False
    return True

def can_place_backslash(board, row, col):
    # Check the top left cell
    if row > 0 and col > 0 and board[row - 1][col - 1] == 2:
        return False
    # Check the top cell
    if row > 0 and board[row - 1][col] == 1:
        return False
    # Check the left cell
    if col > 0 and board[row][col - 1] == 1:
        return False
    return True

def extend(board, row, col, solutions, target_count):
    if row >= len(board):
        count = sum(r.count(1) + r.count(2) for r in board)
        
        if count == target_count:
            solutions.append([r[:] for r in board])
        return

    next_row, next_col = (row, col + 1) if col + 1 < len(board[0]) else (row + 1, 0)
    
    if can_place_slash(board, row, col):
        # Treat / as 1
        board[row][col] = 1
        extend(board, next_row, next_col, solutions,  target_count)
        board[row][col] = -1

    if can_place_backslash(board, row, col):
        # Treat \ as 2
        board[row][col] = 2
        extend(board, next_row, next_col, solutions, target_count)
        board[row][col] = -1

    # Treat empty as 0
    board[row][col] = 0
    extend(board, next_row, next_col, solutions, target_count)
    board[row][col] = -1

def print_solutions(solutions):
    if not solutions:
        print("No solutions found.")
        return

    print(f"Found {len(solutions)} solutions.")
    for solution in solutions:
        print(solution)
        for row in solution:
            print(''.join('/' if cell == 1 else '\\' if cell == 2 else ' ' if cell == 0 else '?' for cell in row))
        print("-" * len(solution[0]) * 2)

if __name__ == "__main__":
    board_length = config.BOARD_LENGTH
    target_count = config.TARGET_COUNT
    board = [[-1 for _ in range(board_length)] for _ in range(board_length)]
    solutions = []
    print("Starting back-tracking process.")
    extend(board, 0, 0, solutions, target_count)

    print_solutions(solutions)
