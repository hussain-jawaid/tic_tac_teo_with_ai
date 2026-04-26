class TicTacTeo:
    def __init__(self):
        """The game class. Initializes the game board and sets the marks for the human and AI players."""
        self.human_mark = None
        self.ai_mark = None
        self.total_moves = 0
        self.humnan_turn = True
        self.difficulty_level = None
        # Initialize the game board.
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # Set the difficulty level.
        self.set_difficulty_level()
        # Take user input to set the marks for both players.
        self.set_marks()
        # Make the human's first move.
        self.human_move()
    
    def set_difficulty_level(self):
        while True:
            try:
                level = input("Choose difficulty level (Enter: Easy, Medium, or Hard): ").strip().lower()
                if level not in {"easy", "medium", "hard"}:
                    raise ValueError("Invalid difficulty level. Choose 'Easy', 'Medium', or 'Hard'.")
                break
            except ValueError as e:
                print(f"Invalid input: {e} Please try again.")
        self.difficulty_level = 1 if level == "easy" else 2 if level == "medium" else 3

        print(f"\nDifficulty Level is {level.upper()}")

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
        print(f"You are {self.human_mark} and the AI is {self.ai_mark}")

        self.display_board()

    def display_board(self):
        print("\nCurrent Board:")
        for row in self.board:
            print(
                " | ".join(
                    self.human_mark if cell == 3 else self.ai_mark if cell == 5 else "-"
                    for cell in row
                )
            )
            print("-" * 9)

    def human_move(self):
        while True:
            try:
                move = input("Enter your move (row and column from 0-2, e.g., '1 2'): ")
                row, col = map(int, move.split())
                if row not in {0, 1, 2} or col not in {0, 1, 2}:
                    raise ValueError("Row and column must be between 0 and 2.")
                self.make_move(row, col, self.human_mark)
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

    def ai_move(self):
        while True:
            try:
                row, col = (self.get_ai_move_v1() if self.difficulty_level == 1 else self.get_ai_move_v2() if self.difficulty_level == 2 else self.get_ai_move_v3())  # Choose AI move method based on difficulty
                print(f"\nAI move: {row}, {col}")
                self.make_move(row, col, self.ai_mark)
                break
            except ValueError as e:
                print(f"AI move error: {e} Retrying...")

    def get_ai_move_v1(self):
        # Selects the first available empty cell on the board for the AI's move
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == 0:
                    return i, j
    
    def get_ai_move_v2(self):
        pass
    
    def get_ai_move_v3(self):
        pass

    def make_move(self, row, col, mark):
        if self.board[row][col] != 0:
            raise ValueError("Cell is already occupied. Choose another cell.")
        self.board[row][col] = 3 if mark == self.human_mark else 5
        self.total_moves += 1
        self.display_board()

        # Check for a winner after the move.
        if self.total_moves >= 5:  # Minimum moves required to have a winner.
            if self.check_winner():
                return
        # Switch turns.
        self.humnan_turn = not self.humnan_turn
        self.human_move() if self.humnan_turn else self.ai_move()

    def check_winner(self):
        # Check for a winner in the rows.
        for row in self.board:
            if sum(row) == 9:
                print("Human wins!")
                return True
            elif sum(row) == 15:
                print("AI wins!")
                return True
        # Check for a winner in the columns.
        for col in range(3):
            if sum(self.board[row][col] for row in range(3)) == 9:
                print("Human wins!")
                return True
            elif sum(self.board[row][col] for row in range(3)) == 15:
                print("AI wins!")
                return True

        # Check for a winner in the diagonals.
        # Primary diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 3:
            print("You wins!")
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 5:
            print("AI wins!")
            return True
        # Secondary diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 3:
            print("You wins!")
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 5:
            print("AI wins!")
            return True

        # Check for a tie.
        if self.total_moves == 9:
            print("Tie!")
            return True

        return False


if __name__ == "__main__":
    game = TicTacTeo()
