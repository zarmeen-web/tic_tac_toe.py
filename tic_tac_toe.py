"""
Tic Tac Toe — Player vs Computer (AI)
======================================
The computer uses the Minimax algorithm to play perfectly.
It will never lose — try to get a draw!

How to run:
    python tic_tac_toe.py

Skills demonstrated:
    - 2D board logic with lists
    - Recursive algorithms 
    - Functions and clean code structure
    - Terminal-based user interaction
"""


# ──────────────────────────────────────────
# Board helpers
# ──────────────────────────────────────────

def create_board():
    """Return an empty 3x3 board (list of 9 strings)."""
    return [" " for _ in range(9)]


def print_board(board):
    """Print the board in a readable grid format."""
    print()
    for row in range(3):
        cells = board[row * 3: row * 3 + 3]
        print(f"  {cells[0]} | {cells[1]} | {cells[2]} ")
        if row < 2:
            print("  ---------")
    print()


def print_board_with_numbers():
    """Show position numbers so the player knows where to move."""
    print()
    print("  Position numbers:")
    for row in range(3):
        nums = [str(row * 3 + col + 1) for col in range(3)]
        print(f"  {nums[0]} | {nums[1]} | {nums[2]} ")
        if row < 2:
            print("  ---------")
    print()


def check_winner(board, player):
    """Return True if the given player has won."""
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6],              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combos)


def is_draw(board):
    """Return True if the board is full and no one has won."""
    return " " not in board


def get_available_moves(board):
    """Return a list of empty cell indices."""
    return [i for i, cell in enumerate(board) if cell == " "]


# ──────────────────────────────────────────
# Minimax AI
# ──────────────────────────────────────────

def minimax(board, is_maximizing):
    """
    Minimax algorithm — the AI thinks ahead through every
    possible game outcome and picks the best move.

    Returns a score:
      +1  → Computer (O) wins
      -1  → Player (X) wins
       0  → Draw
    """
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    moves = get_available_moves(board)

    if is_maximizing:
        best = -float("inf")
        for move in moves:
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best = max(best, score)
        return best
    else:
        best = float("inf")
        for move in moves:
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            best = min(best, score)
        return best


def get_best_move(board):
    """Return the index of the best move for the computer (O)."""
    best_score = -float("inf")
    best_move = None

    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# ──────────────────────────────────────────
# Player input
# ──────────────────────────────────────────

def get_player_move(board):
    """Ask the player for a valid move and return the board index."""
    while True:
        try:
            move = int(input("  Your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("  Please enter a number between 1 and 9.")
            elif board[move] != " ":
                print("  That spot is already taken! Try another.")
            else:
                return move
        except ValueError:
            print("  Invalid input. Enter a number between 1 and 9.")


# ──────────────────────────────────────────
# Main game loop
# ──────────────────────────────────────────

def play_game():
    """Run one full game between the player and the computer."""
    board = create_board()

    print("\n  ┌─────────────────────────┐")
    print("  │      TIC TAC TOE        │")
    print("  │   You (X) vs opponent(O)     │")
    print("  └─────────────────────────┘")
    print_board_with_numbers()
    print("  Tip: The opponent plays perfectly — aim for a draw!\n")

    for turn in range(9):
        print_board(board)

        if turn % 2 == 0:
            # Player's turn (X)
            print("  Your turn (X):")
            move = get_player_move(board)
            board[move] = "X"

            if check_winner(board, "X"):
                print_board(board)
                print("  🎉 You win! (How?! The intelligent computer opponent must have had a bug...)\n")
                return "X"
        else:
            # Computer's turn (O)
            print("  Computer is thinking...")
            move = get_best_move(board)
            board[move] = "O"
            print(f"  Computer played position {move + 1}.")

            if check_winner(board, "O"):
                print_board(board)
                print("  🤖 Computer wins! Better luck next time.\n")
                return "O"

    print_board(board)
    print("  🤝 It's a draw! Well played.\n")
    return "Draw"


def main():
    """Entry point — keeps score across multiple rounds."""
    scores = {"X": 0, "O": 0, "Draw": 0}

    while True:
        result = play_game()
        scores[result] += 1

        print(f"  Score → You: {scores['X']}  |  opponent: {scores['O']}  |  Draws: {scores['Draw']}")
        print()

        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! 👋\n")
            break


if __name__ == "__main__":
    main()
