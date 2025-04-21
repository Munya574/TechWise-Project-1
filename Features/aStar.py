import heapq

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic cost from node to goal
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.f < other.f

def a_star(start, end, grid):
    open_list = []
    closed_list = []
    heapq.heappush(open_list, (start.f, start))

    while open_list:
        current_node = heapq.heappop(open_list)[1]
        closed_list.append(current_node)

        if current_node == end:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        neighbors = get_neighbors(current_node, grid)
        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + 1  # Assuming uniform cost
            neighbor.h = abs(neighbor.x - end.x) + abs(neighbor.y - end.y)  # Manhattan distance
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                heapq.heappush(open_list, (neighbor.f, neighbor))

    return None  # No path found

def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node[1] and neighbor.g > node[1].g:
            return False
    return True

def get_neighbors(node, grid):
    neighbors = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares (up, down, left, right)
        node_position = (node.x + new_position[0], node.y + new_position[1])

        if node_position[0] > len(grid) - 1 or node_position[0] < 0 or node_position[1] > len(grid[len(grid)-1]) - 1 or node_position[1] < 0:
            continue

        if grid[node_position[0]][node_position[1]] != 0:  # Check if walkable
            continue

        new_node = Node(node_position[0], node_position[1], node)
        neighbors.append(new_node)

    return neighbors
