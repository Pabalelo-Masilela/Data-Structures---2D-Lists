'''Created a function that takes a grid of # and -, where each hash (#),
represents a mine and each dash (-) represents a mine-free spot.
Return a grid, where each dash is replaced by a digit,
indicating the number of mines immediately adjacent to the spot i.e. 
(horizontally, vertically, and diagonally).'''

def minesweeper(minesweeper_array):
    rows = len(minesweeper_array) 
    columns = len(minesweeper_array[0])
    
    #validate input array
    for row in minesweeper_array:
        for entry in row:
            if entry not in ('-', '#'):
                print("Invalid input. The array should only contain '-' or '#' characters.")
                return

    for row in range(rows):
        for column in range(columns):
            if minesweeper_array[row][column] == "-":
                counter = 0
                for row_adjacent in range(-1, 2):
                    for column_adjacent in range(-1, 2):
                        # Check adjacent cells within bounds
                        if 0 <= row + row_adjacent < rows and 0 <= column + column_adjacent < columns:
                            if minesweeper_array[row + row_adjacent][column + column_adjacent] == "#":
                                counter += 1  # Increment the counter for each adjacent mine
                # Update the cell with the count of adjacent mines
                minesweeper_array[row][column] = str(counter)

    # Print the resulting Minesweeper array
    for row in minesweeper_array:
        print(" ".join(row))
# Testing created function
array = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]]

minesweeper(array)