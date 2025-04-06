import random
import time

class TicTacToe:
    def __init__(self):
        """Initialize the game board and starting variables."""
        # 3x3 board represented as a list: 0-8 positions
        # None = empty, 'X' = player, 'O' = AI
        self.board = [None] * 9
        self.current_player = None  # 'X' for player, 'O' for AI
        self.winner = None
        self.game_over = False

    #  GAME SETUP
    def setup_game(self):
        print("Welcome to Tic Tac Toe!")
        print("You are X and the AI is O")

        choice = input("Do you want to go first? (y/n): ").lower()
        if choice == 'y':
            self.current_player = 'X'  # Player goes first
            print("You go first!")
        else:
            self.current_player = 'O'  # AI goes first
            print("AI goes first!")

        self.play_game()

    def display_board(self):
        print("\nCurrent Board:")
        for i in range(0, 9, 3):
            print(f" {self.board[i] or ' '} | {self.board[i + 1] or ' '} | {self.board[i + 2] or ' '} ")
            if i < 6:
                print("-----------")
        print()

    def play_game(self):
        while not self.game_over:
            self.display_board()

            if self.current_player == 'X':
                self.get_player_move()
            else:
                self.get_ai_move()

            # Check if the game is over
            if self.check_winner():
                self.display_board()
                if self.winner:
                    print(f"{self.winner} wins!")
                else:
                    print("It's a tie!")
                self.game_over = True

            self.current_player = 'O' if self.current_player == 'X' else 'X'

    #  PLAYER MOVE HANDLING
    def get_player_move(self):
        """Get and validate the player's move."""
        valid_move = False
        while not valid_move:
            try:
                position = int(input("Enter your move (0-8): "))
                if 0 <= position <= 8 and self.board[position] is None:
                    self.board[position] = 'X'
                    valid_move = True
                else:
                    print("Invalid move. Position already taken or out of range.")
            except ValueError:
                print("Please enter a number between 0 and 8.")

    #  AI MOVE DETERMINATION
    def get_ai_move(self):
        print("AI is thinking...")
        time.sleep(3)

        # Use the minimax algorithm to find the best move
        best_score = float('-inf')
        best_move = None

        # For each available move, calculate its minimax score
        for i in range(9):
            if self.board[i] is None:
                self.board[i] = 'O'  # Try this move
                score = self.minimax(self.board, 0, False)  # AI is maximizing
                self.board[i] = None  # Undo the move

                # Update best move if this move has a better score
                if score > best_score:
                    best_score = score
                    best_move = i

        # Make the best move
        self.board[best_move] = 'O'
        print(f"AI chooses position {best_move}")

    def minimax(self, board, depth, is_maximizing):
        """
        Minimax algorithm implementation.

        Args:
            board: Current board state
            depth: Current depth in the game tree
            is_maximizing: Whether current player is maximizing (AI) or minimizing (player)

        Returns:
            The best score from the current position
        """
        # Check terminal states
        if self.check_for_winner('O'):
            return 10 - depth
        elif self.check_for_winner('X'):
            return depth - 10
        elif None not in board:
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] is None:
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = None
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] is None:
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = None
                    best_score = min(score, best_score)
            return best_score

    # WIN CONDITION CHECKING

    def check_for_winner(self, player):
        # Define all possible winning combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in win_combinations:
            if all(self.board[pos] == player for pos in combo):
                return True
        return False

    def check_winner(self):
        # Check if X won
        if self.check_for_winner('X'):
            self.winner = 'X'
            return True

        # Check if O won
        if self.check_for_winner('O'):
            self.winner = 'O'
            return True

        # Check for a tie
        if None not in self.board:
            return True

        return False

# Main execution
if __name__ == "__main__":
    game = TicTacToe()
    game.setup_game()
