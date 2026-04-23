class TicTacTeo:
    def __init__(self):
        """The game class. Initializes the game board and sets the marks for the human and AI players."""
        self.human_mark = None
        self.ai_mark = None
        self.total_moves = 0
        # Initialize the game board.
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
            ]

        # Take user input to set the marks for both players.
        self.set_marks()
    
    def set_marks(self):
        while True:
            try:
                choice = input("Choose Your Mark ('x' or 'o'): ").strip().lower()
                if choice not in {"x", "o"}:
                    raise ValueError("Invalid mark. Choose 'x' or 'o'.")
                break
            except ValueError as e:
                print(f"Invalid input: {e} Please try again.")

        self.human_mark = choice
        self.ai_mark = "o" if choice == "x" else "x"

        self.display_board()
    
    def display_board(self):
        print("\nCurrent Board:")
        for row in self.board:
            print(" | ".join(str(cell) for cell in row))
            print("-" * 9)
    
    def player_move(self):
        while True:
            try:
                move = input("Enter your move (row and column from 0-2, e.g., '1 2'): ")
                row, col = map(int, move.split())
                if row not in {0, 1, 2} or col not in {0, 1, 2}:
                    raise ValueError("Row and column must be between 0 and 2.")
                self.make_move(row, col, self.human_mark)
                break
            except ValueError as e:
                print(f"Invalid input: {e} Please try again.")
    
    def ai_move(self):
        while True:
            row, col = self.get_ai_move()
            if self.board[row][col] == 0:
                self.make_move(row, col, self.ai_mark)
                break
    
    def make_move(self, row, col, mark):
        if self.board[row][col] != 0:
            raise ValueError("Cell is already occupied. Choose another cell.")
        self.board[row][col] = mark
        self.total_moves += 1
        self.display_board()

        # Check for a winner after the move.
        if self.total_moves >= 5:  # Minimum moves required to have a winner.
            self.check_winner()

    def check_winner(self):
        pass

if __name__ == "__main__":
    game = TicTacTeo()