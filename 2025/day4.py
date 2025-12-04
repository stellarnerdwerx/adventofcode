from itertools import product

def count_tp(grid):
    """adapted from 2024 prob4 solution"""
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]
    
    def is_valid(x, y):
        return 0<=x<rows and 0<=y<cols

    def count_adj(x, y):
        """how many @ symbols are adjacent to position"""
        count = 0
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if is_valid(nx,ny) and grid[nx][ny]=='@':
                count+= 1
        return count
    
    def access_rolls():
        """find all rolls with less than 4 adjacent @ symbols"""
        access = []
        for x, y in product(range(rows), range(cols)):
            if grid[x][y]=='@':
                adj = count_adj(x, y)
                if adj<4:
                    access.append((x, y))
        return access
    
    return len(access_rolls())

with open("four.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

result = count_tp(grid)
print(result) #part1

def count_tp_recursive(grid):
    """adapted from 2024 prob4 solution"""
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]
    
    def is_valid(x, y):
        return 0<=x<rows and 0<=y<cols

    def count_adj(x, y):
        """how many @ symbols are adjacent to position"""
        count = 0
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if is_valid(nx,ny) and grid[nx][ny]=='@':
                count+= 1
        return count
    
    def access_rolls():
        """find all rolls with less than 4 adjacent @ symbols"""
        access = []
        for x, y in product(range(rows), range(cols)):
            if grid[x][y]=='@':
                adj = count_adj(x, y)
                if adj<4:
                    access.append((x, y))
        return access

  # <-- new addition for part 2 starts here -->
    remove = 0
    access = access_rolls()
    
    #keep removing
    if access:
        for x, y in access:
            grid[x][y] = 'x' #update
        
        remove = len(access)
        remove += count_tp_recursive(grid)
    
    return remove

with open("four.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

result = count_tp_recursive(grid)
print(result) #part2
