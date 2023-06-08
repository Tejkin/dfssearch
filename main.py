from pyamaze import maze, COLOR, agent

def main():
    maze_size = 7
    maze = initMaze(maze_size)
    final_agent = initAgent(maze)
    dfs_agent = agent(maze, footprints = True, filled = True, color = COLOR.green, goal = (0, 0))
    path, dfs_path = dfs(maze)
    maze.tracePath({dfs_agent:dfs_path})
    maze.tracePath({final_agent:path})
    maze.run()

def dfs(m):
    """
    Performs depth-first search (DFS) on a given maze.

    Args:
        m (Maze): The maze object containing the maze map.

    Returns:
        - final_path (dict): A dictionary representing the final path found during DFS.
                                Each key represents a cell, and its value represents the previous cell in the path.
        - visited (list): A list of cells that were visited during DFS.

    """
    start = (m.rows, m.cols)
    visited = [start]
    frontier = [start]
    dfs_path = {}
    all_cells = [start]
    maze_size = m.rows * m.cols
    
    while True:
        current = frontier.pop()
        if len(all_cells) == maze_size:
            break
        for direction in "NSEW":
            if m.maze_map[current][direction]:
                if direction == 'N':
                    child = (current[0] - 1, current[1])
                elif direction == 'S':
                    child = (current[0] + 1, current[1])
                elif direction == 'E':
                    child = (current[0], current[1] + 1)
                elif direction == 'W':
                    child = (current[0], current[1] - 1)
                if child in visited:
                    continue
                visited.append(child)
                frontier.append(child)
                if child not in all_cells:
                    all_cells.append(child)
                dfs_path[child] = current
    final_path = {}
    cell = (1, 1)
    while cell != start:
        final_path[dfs_path[cell]] = cell
        cell = dfs_path[cell]
    return final_path, visited
                
def initMaze(size):
    """
    Initialises maze with user input as size

    Args:
        size (int): The size of the maze (number of rows and columns).

    Returns:
        Maze: A maze object initialized with the given size.
    """

    m = maze(size, size)
    m.CreateMaze()
    return m

def initAgent(m):
    """
    Initialises agent to move in maze

    Parameters:
        m (maze): The maze object containing the maze map.
        
    Returns:
        a (agent): The agent object containing the agent that traverses the maze map.
    """
    a = agent(m, shape = 'arrow', footprints = True, filled = True, color = COLOR.red)
    return a

if __name__ == '__main__':
    main()