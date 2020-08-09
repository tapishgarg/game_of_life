# Let's play Game of Life

import os
import random
import time
import sys
import argparse

# Clears the console using system command
def clear_console():
    if sys.platform.startswith("dar"):
        os.system("clear")
    elif sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")
    else:
        print("Unable to clear console")


# Creates a random 2D Matrix that contains 1s and 0s to represent the cells in Conway's Game of Life.
def create_grid(rows, cols):
    grid = []
    for row in range(rows):
        grid_rows = []
        for col in range(cols):
            if random.randint(0,3) == 0:
                grid_rows = grid_rows + [1]
            else:
                grid_rows = grid_rows + [0]
        grid = grid + [grid_rows]
    return grid


# Prints the Game of Life grid to console
def grid_print(rows, cols, grid, gen):
    clear_console()
    output = ""

    output = "Generation {0} ('.' = Dead and 'X' = Alive)\n\r".format(gen)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                output = output + '. '
            else :
                output = output + 'X '
        output = output + "\n\r"
    print(output)


# Counts the number of live cells surrounding a center cell at grid[row][col]
def get_live_neighbours(row, col, rows, cols, grid):
    
    # Checking the neighbours of particlur cell
    life_cell_sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i == 0 and j == 0):
                life_cell_sum = life_cell_sum + grid[((row + i) % rows)][((col + j) % cols)]
    return life_cell_sum


# Analyzes the current generation of the grid and determines what cells live and die in the next generation 
# of the grid.
def create_next_grid(rows, cols, grid, next_grid):
    for row in range(rows):
        for col in range(cols):

            # Cell die due to underpopulation or overpopulation
            live_neighbours = get_live_neighbours(row, col, rows, cols, grid)
            if live_neighbours < 2 or live_neighbours > 3:
                next_grid[row][col] = 0 

            # If cell is dead and surrounded by 3 alive cells, it makes to next generation (reproduction)
            elif live_neighbours == 3 and grid[row][col] == 0:
                next_grid[row][col] == 1

            # If a live cell is surrounded by 2 or 3 live cells then it makes to next generation
            else :
                next_grid[row][col] = grid[row][col]


# Checks whether current grid is same as to next grid
def update_grid(rows, cols, grid, next_grid):
    for row in range(rows):
        for col in range(cols):
            if not grid[row][col] == next_grid[row][col]:
                return True
    return False


# Get input value under given range
def integer_value(value, low, high):
    while True:
        try:
            value = int(input(value))
        except ValueError:
            print("Input is invalid, choose interger")
        if value < low or value > high:
            print("Input is out of range, choose between (5,100)")
        else:
            break
    return value


# Asks for inputs like number of rows, number of columns and number of generations and print grid for every
# generation
def start_game():
    # Clean the console before starting the program
    clear_console()

    rows = integer_value("Enter number of rows : ", 5, 100 )
    cols = integer_value("Enter number of columns : ", 5, 100)

    generations = integer_value("Number of generations : ", 1, 1000)

    # Initializing current and next generation grid 
    current_generation = create_grid(rows,cols)
    next_generation = create_grid(rows,cols)

    gen = 1
    for gen in range(1,generations+1):
        if not update_grid(rows, cols, current_generation, next_generation):
            break
        grid_print(rows, cols, current_generation, gen)
        create_next_grid(rows, cols, current_generation, next_generation)
        time.sleep(1/2.0)
        current_generation, next_generation = next_generation, current_generation

    grid_print(rows, cols, current_generation, gen)


# Run the main program
if __name__ == "__main__":
    start_game()