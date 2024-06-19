class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid  # 9x9 grid representing the Sudoku puzzle
        self.size = 9     # size of the Sudoku grid
    
    def solve(self):
        # Find an empty cell (cell with 0)
        empty_cell = self.find_empty()
        
        # If no empty cells left, puzzle is solved
        if not empty_cell:
            return True
        
        row, col = empty_cell
        
        # Try numbers 1-9
        for num in range(1, 10):
            # Check if num is valid in this position
            if self.is_valid(row, col, num):
                # Place the number
                self.grid[row][col] = num
                
                # Recursively attempt to solve the rest of the puzzle
                if self.solve():
                    return True
                
                # Backtrack
                self.grid[row][col] = 0
        
        # No valid number found, backtrack
        return False
    
    def find_empty(self):
        # Find the next empty cell in the grid
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 0:
                    return (row, col)
        return None
    
    def is_valid(self, row, col, num):
        # Check if placing num in row, col is valid
        
        # Check row
        if num in self.grid[row]:
            return False
        
        # Check column
        for r in range(self.size):
            if self.grid[r][col] == num:
                return False
        
        # Check box (3x3 subgrid)
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for r in range(box_row_start, box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                if self.grid[r][c] == num:
                    return False
        
        return True
    
    def print_grid(self):
        # Print the Sudoku grid
        for row in self.grid:
            print(row)

import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = tk.StringVar()
                entry = tk.Entry(self.root, textvariable=self.grid[i][j], width=3, font=('Arial', 18))
                entry.grid(row=i, column=j)
        
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, columnspan=9)
    
    def solve_sudoku(self):
        # Get the current grid values
        sudoku_grid = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.grid[i][j].get()
                if value.isdigit() and 1 <= int(value) <= 9:
                    sudoku_grid[i][j] = int(value)
                else:
                    messagebox.showerror("Error", "Invalid Sudoku grid input.")
                    return
        
        # Solve the Sudoku puzzle
        solver = SudokuSolver(sudoku_grid)
        if solver.solve():
            # Update the GUI with the solved Sudoku grid
            for i in range(9):
                for j in range(9):
                    self.grid[i][j].set(sudoku_grid[i][j])
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

# Example usage without GUI
if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solver = SudokuSolver(sudoku_grid)
    solver.solve()
    solver.print_grid()

# Example usage with GUI
root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()
