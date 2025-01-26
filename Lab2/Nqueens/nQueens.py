import tkinter as tk
from tkinter import ttk

class NQueensVisualizer:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.solve()
        self.display_solutions()

    def solve(self):
        """Find all solutions to the N-Queens problem using backtracking."""
        def is_safe(board, row, col):
            # Check this column
            for i in range(row):
                if board[i] == col:
                    return False
            # Check upper left diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i] == j:
                    return False
            # Check upper right diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, self.n)):
                if board[i] == j:
                    return False
            return True

        def backtrack(board, row):
            if row == self.n:
                self.solutions.append(board[:])
                return
            for col in range(self.n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)
                    board[row] = -1  # Reset

        board = [-1] * self.n  # Initialize the board
        backtrack(board, 0)

    def draw_board(self, canvas, solution, x_offset, y_offset, tile_size):
        """Draw a chessboard with the given solution at a specified offset."""
        for i in range(self.n):
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "black"
                canvas.create_rectangle(
                    x_offset + j * tile_size,
                    y_offset + i * tile_size,
                    x_offset + (j + 1) * tile_size,
                    y_offset + (i + 1) * tile_size,
                    fill=color,
                )
        # Place queens
        for row, col in enumerate(solution):
            x_center = x_offset + col * tile_size + tile_size // 2
            y_center = y_offset + row * tile_size + tile_size // 2
            radius = tile_size // 4
            canvas.create_oval(
                x_center - radius,
                y_center - radius,
                x_center + radius,
                y_center + radius,
                fill="red",
            )

    def display_solutions(self):
        """Create a single scrollable window to display all solutions in a grid."""
        root = tk.Tk()
        root.title(f"{self.n}-Queens Solutions: {len(self.solutions)} total")

        # Scrollable frame setup
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Enable scrolling with mouse wheel
        def on_mouse_wheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")

        root.bind("<MouseWheel>", on_mouse_wheel)  # Windows and MacOS
        root.bind("<Shift-MouseWheel>", lambda e: canvas.xview_scroll(-1 * (e.delta // 120), "units"))  # Horizontal scrolling
        root.bind("<Up>", lambda e: canvas.yview_scroll(-1, "units"))  # Scroll up with arrow keys
        root.bind("<Down>", lambda e: canvas.yview_scroll(1, "units"))  # Scroll down with arrow keys

        # Configuration
        tile_size = (85*5)/N  # Size of each tile
        solutions_per_row = 4  # Max solutions per row
        board_size = tile_size * self.n
        padding = 40  # Space between boards

        for idx, solution in enumerate(self.solutions):
            row = idx // solutions_per_row
            col = idx % solutions_per_row
            x_offset = col * (board_size + padding)
            y_offset = row * (board_size + padding)

            # Create a frame for each solution
            frame = ttk.Frame(scrollable_frame)
            frame.grid(row=row, column=col, padx=padding // 2, pady=padding // 2)

            # Add a label showing the solution number and the actual solution
            label = ttk.Label(frame, text=f"Solution {idx + 1}: {solution}", anchor="center")
            label.pack()

            # Create a canvas for the chessboard
            board_canvas = tk.Canvas(
                frame, width=board_size, height=board_size, bg="white"
            )
            board_canvas.pack()
            self.draw_board(board_canvas, solution, 0, 0, tile_size)

        root.mainloop()


# Run the visualizer for N-Queens
if __name__ == "__main__":
    N = 8  # Change this value for different board sizes
    N= int(input("Enter the board size: "))
    NQueensVisualizer(N)
