def main():
    row = int(input("How many rows? "))
    col = int(input("How many columns? "))
    grid = create_grid(row, col)
    draw_grid(grid, row, col)

    grid = user_input(grid)
    draw_grid(grid, row, col)

    nex = input("n for next generation: ")
    while nex == "n":
        grid = turn(grid, row, col)
        draw_grid(grid, row, col)
        nex = input("n for next generation: ")

    

def create_grid(row, col):
    grid = {}
    for x in range(1, row+1):
        for y in range(1, col+1):
            grid[(x, y)] = 0
    
    
    return grid

def draw_grid(grid, row, col):
    for x in range(1, row+1):
        for y in range(1, col+1):
            print (grid[(x, y)], end = " ")
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
            grid[(row, col)] = 1

    return grid

def turn(grid, row, col):
    new_grid = create_grid(row, col)
    near = [(-1, -1), ( 0, -1), ( 1, -1), (-1,  0), ( 1,  0),
                  (-1,  1), ( 0,  1), ( 1,  1)]

    for x in range(1, row+1):
        for y in range(1, col+1):
            neighbor = 0
            for nx, ny in near:
                try:
                    if grid[(x+nx, y+ny)] == 1:
                        neighbor += 1
                except KeyError:
                    continue
            if grid[(x, y)] == 0 and neighbor == 3:
                new_grid[(x, y)] = 1
            elif grid[(x, y)] == 1 and neighbor <= 1:
                new_grid[(x, y)] = 0
            elif grid[(x, y)] == 1 and neighbor >= 4:
                new_grid[(x, y)] = 0
            elif grid[(x, y)] == 1 and (neighbor == 2 or neighbor == 3):
                new_grid[(x, y)] = 1

    return new_grid

main()
