import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

def create_grid(canvas):
    cells = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        row_cell = []
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="Pink", outline="black")
            row_cell.append(rect)
        cells.append(row_cell)
    return cells

def erase(event):
    x, y = event.x, event.y
    row = y // CELL_SIZE
    col = x // CELL_SIZE

    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        canvas.itemconfig(grid[row][col], fill="Red")

def main():
    global canvas, grid

    root = tk.Tk()
    root.title("Grid Erase Canvas")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="Red")
    canvas.bind("<B1-Motion>", erase)  # Mouse drag with left button
    canvas.pack()

    grid = create_grid(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
