from queue import PriorityQueue

class State:
    # Each state is one room in the 4x4 maze
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Makes printing look like (x,y)
    def __str__(self):
        return f"({self.x},{self.y})"

    # Two states are equal if they have the same coordinates
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Allows states to be stored in sets and used as dictionary keys
        return hash((self.x, self.y))

START = State(0, 3)  
GOAL  = State(3, 0)  

# Goal test function
def is_goal(state: State):
    return state == GOAL

# Heuristic function: Manhattan distance
def heuristic(state: State):
    return abs(state.x - GOAL.x) + abs(state.y - GOAL.y)

# Each key (x,y) shows which neighboring rooms can be entered directly
OPEN_DOORS = {
    (0,3): [(1,3)],
    (1,3): [(0,3), (2,3)],
    (2,3): [(1,3), (2,2), (3,3)],
    (3,3): [(2,3), (3,2)],

    (0,2): [(1,2), (0,1)],
    (1,2): [(0,2), (2,2)],
    (2,2): [(1,2), (2,3)],  
    (3,2): [(3,3)],

    
    (0,1): [(1,1), (0,2), (0,0)],
    (1,1): [(0,1), (2,1)],
    (2,1): [(1,1), (3,1)],
    (3,1): [(2,1), (3,0)],


    (0,0): [(0,1)],
    (1,0): [(2,0)],
    (2,0): [(1,0), (3,0)],
    (3,0): [(2,0), (3,1)], 
}


# Each key (x,y) shows which neighboring rooms can be entered directly
def expand(s):
    successors = []
    for (nx, ny) in OPEN_DOORS[(s.x, s.y)]:
        successors.append(State(nx, ny))
    return successors


def A_star(start: State):
    pq = PriorityQueue()
     #tie-breaker for sorting items with same f and g values
    unique_id = 0 

    # keeps track of explored rooms
    visited = set()

    # Add the start state to the queue
    pq.put((heuristic(start), 0, unique_id, start, [start]))
    unique_id += 1

    while not pq.empty():
        # get the lowest-cost item
        f, cost, _, state, path = pq.get()

        # Skip if we’ve already visited this room
        if state in visited:
            continue
        visited.add(state)

        if is_goal(state):
            return path

        # Go through all possible next rooms
        for succ in expand(state):
            if succ in visited:
                continue
            new_cost = cost + 1
            pq.put((new_cost + heuristic(succ), new_cost, unique_id, succ, path + [succ]))
            unique_id += 1

    # If goal is unreachable
    return []

# Print the final path
def print_path(path: list[State]):
    """Print the path from start to goal in a readable format."""
    if not path:
        print("No path found.")
        return

    print("Optimal path:")
    print(" → ".join(f"({p.x},{p.y})" for p in path))
    print(f"Number of steps: {len(path) - 1}")

# Run the program
if __name__ == "__main__":
    START = State(0,3)
    GOAL  = State(3,0)

    path = A_star(START)
    print_path(path)

