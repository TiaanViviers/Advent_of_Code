import sys

def create_graph(grid):
    """Creates a graph representation of the grid and identifies the start position."""
    G = {}
    Y = len(grid)
    X = len(grid[0]) if Y > 0 else 0
    sy, sx = 0, 0

    # Define pipe connections and direction offsets
    pipe_connections = {
        'F': ['south', 'east'],
        '|': ['north', 'south'],
        '-': ['east', 'west'],
        'L': ['north', 'east'],
        'J': ['north', 'west'],
        '7': ['south', 'west'],
    }
    direction_offsets = {
        'north': (-1, 0),
        'south': (1, 0),
        'east': (0, 1),
        'west': (0, -1),
    }

    for y in range(Y):
        for x in range(X):
            c = grid[y][x]
            if c == '.':
                continue

            G.setdefault((y, x), set())

            if c in pipe_connections:
                # Add connections based on pipe type
                for direction in pipe_connections[c]:
                    dy, dx = direction_offsets[direction]
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        G[(y, x)].add((ny, nx))
            elif c == 'S':
                # Handle the starting position 'S'
                parts = set()
                if y > 0 and grid[y - 1][x] in 'F|7':
                    parts.add((y - 1, x))
                if y < Y - 1 and grid[y + 1][x] in '|LJ':
                    parts.add((y + 1, x))
                if x > 0 and grid[y][x - 1] in '-LF':
                    parts.add((y, x - 1))
                if x < X - 1 and grid[y][x + 1] in '-J7':
                    parts.add((y, x + 1))
                G[(y, x)].update(parts)
                sy, sx = y, x

                # Update 'S'
                connected_directions = []
                if (y - 1, x) in parts:
                    connected_directions.append('north')
                if (y + 1, x) in parts:
                    connected_directions.append('south')
                if (y, x - 1) in parts:
                    connected_directions.append('west')
                if (y, x + 1) in parts:
                    connected_directions.append('east')

                if 'north' in connected_directions:
                    if 'south' in connected_directions:
                        grid[y][x] = '|'
                    elif 'east' in connected_directions:
                        grid[y][x] = 'L'
                    elif 'west' in connected_directions:
                        grid[y][x] = 'J'
                elif 'south' in connected_directions:
                    if 'east' in connected_directions:
                        grid[y][x] = 'F'
                    elif 'west' in connected_directions:
                        grid[y][x] = '7'
                elif 'east' in connected_directions and 'west' in connected_directions:
                    grid[y][x] = '-'
            else:
                pass
    return G, (sy, sx), grid


def dfs_loop_tiles(G, start_pos):
    """Performs a depth-first search to identify all tiles in the main loop."""
    seen = set()
    stack = [start_pos]
    while stack:
        y, x = stack.pop()
        if (y, x) in seen:
            continue
        seen.add((y, x))
        for neighbor in G.get((y, x), set()):
            if neighbor not in seen:
                stack.append(neighbor)
    return seen


def count_enclosed_tiles(grid, loop_tiles):
    """Counts the number of tiles enclosed by the loop."""
    Y = len(grid)
    X = len(grid[0]) if Y > 0 else 0
    enclosed_tiles = 0

    for y in range(Y):
        inside = False
        for x in range(X):
            c = grid[y][x]
            if (y, x) in loop_tiles and c in 'L|J':
                inside = not inside
            if inside and (y, x) not in loop_tiles:
                enclosed_tiles += 1
    return enclosed_tiles


def main():
    with open(sys.argv[1], 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]
    
    G, start_pos, grid = create_graph(grid)
    loop_tiles = dfs_loop_tiles(G, start_pos)
    enclosed_tiles = count_enclosed_tiles(grid, loop_tiles)
    print(f"number of enclosed tiles: {enclosed_tiles}")


if __name__ == '__main__':
    main()
