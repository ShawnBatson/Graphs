# We have two semi-new topics to cover today: One is connected components, which are closely related to DFT and BFT. Please watch the video below:
# * Connected Components: https://www.youtube.com/watch?v=zGW6XTkeEFU
# The second is randomness, or more accurately pseudorandomness. Computerized random number generation is very similar to the hashing algorithms we explored last sprint. Please look over the following documentation on randomness and shuffling:
# * Randomness: https://github.com/LambdaSchool/Graphs/tree/master/objectives/randomness
# Once you've reviewed the precourse material, take a look at this island_counting problem which we will be going over in today's guided project:
# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# island_counter(islands) # returns 4

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

# CONNECTED COMPONENTS

# make sure to have visited from below, here.


def get_neighbors(row, col, island_matrix):
    neighbors = []
    # check the neighbor above row col
    if row > 0 and island_matrix[row - 1][col] == 1:
        neighbors.append((row - 1, col))

    # check below
    if row < len(island_matrix) - 1 and island_matrix[row + 1][col] == 1:
        neighbors.append((row + 1, col))
    # check left
    if col > 0 and island_matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
    # check right
    if col < len(island_matrix[row]) - 1 and island_matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1))
    return neighbors


def dft(starting_row, starting_col, island_matrix, visited):
    # create an empty stack
    stack = Stack()
    # push the starting row and col onto the stack
    stack.push((starting_row, starting_col))
    # while the stack is not empty:
    while stack.size() > 0:
        # pop the current row and column off the stack
        current_row_col = stack.pop()
        row = current_row_col[0]
        col = current_row_col[1]
        # if current row and col not visited
        if visited[row][col] is False:
            visited[row][col] = True
            # set the current row and col as visited:
            for neighbor in get_neighbors(row, col, island_matrix):
                stack.push(neighbor)
            # get the neighbor rows and columns
                # push them onto the stack.


def island_counter(island_matrix):
    # keep track of all visited vertices
    visited_matrix = []
    for i in range(len(island_matrix)):
        visited_matrix.append([False] * len(island_matrix[0]))
    island_count = 0
    # walk through each cell of the matrix.
    for row in range(len(island_matrix)):
        for col in range(len(island_matrix[row])):
            # if island_matrix[row][col] = 1 and not in visited:
            if island_matrix[row][col] == 1 and visited_matrix[row][col] is False:
                # traverse the connected component (graph)
                #  DFT starting at the current cell.
                dft(row, col, island_matrix, visited_matrix)
            # Once done DFT, tha tmeans we have found a new island.
            # Increment some island_count value +=1
                island_count += 1
    return island_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# visited_islands = [[0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0]]

print(island_counter(islands))
