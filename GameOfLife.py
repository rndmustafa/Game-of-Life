def main():
    row = int(input("How many rows? "))
    col = int(input("How many columns? "))
    grid = create_grid(row, col)
    draw_grid(grid, row, col)

    grid = user_input(grid)
    draw_grid(grid, row, col)

    nex = input("hit enter for next generation: ")
    while nex == "":
        grid = turn(grid, row, col)
        draw_grid(grid, row, col)
        nex = input("n for next generation: ")
    

    

def create_grid(row, col):
    grid = []
    for i in range (0, row):
        grid.append([])
        for j in range(0, col):
            grid[i].append(0)
    
    return grid

def draw_grid(grid, row, col):
    for i in range(0, row):
        for j in range(0, col):
            print (grid[i][j], end = " ")
        print()
    print()

def user_input(grid):
    print("Place cells in this format: Row Column. For example: 2 1")
    print("When finished placing cells, just hit enter.")
    place = "null"
    while place != "":
        place = input("Place cell: ")
        if place != "":
            place = place.split()
            row = int(place[0])
            col = int(place[1])
            grid[row-1][col-1] = 1

    return grid

def turn(grid, row, col):
    new_grid = create_grid(row, col)
    near = [(-1, -1), ( 0, -1), ( 1, -1), (-1,  0), ( 1,  0),
                  (-1,  1), ( 0,  1), ( 1,  1)]

    for i in range(0, row):
        for j in range(0, col):
            neighbor = 0
            for nx, ny in near:
                try:
                    if grid[i+nx][j+ny] == 1:
                        neighbor += 1
                except IndexError:
                    continue
            if grid[i][j] == 0 and neighbor == 3:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and neighbor <= 1:
                new_grid[i][j] = 0
            elif grid[i][j] == 1 and neighbor >= 4:
                new_grid[i][j] = 0
            elif grid[i][j] == 1 and (neighbor == 2 or neighbor == 3):
                new_grid[i][j] = 1

    return new_grid

main()
