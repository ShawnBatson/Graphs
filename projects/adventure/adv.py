from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


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


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

################################################################

traversal_graph = {}  # set my "traversal graph"

for i in range(len(room_graph)):  # fill the graph exits with question marks
    traversal_graph[i] == {'n': '?', 's': '?', 'w': '?', 'e': '?'}

# create a function to help with going backwards


def back_direction(direction):
    backward = ""
    if direction == "n":
        backward == "s"
    elif direction == "s":
        backward == "n"
    elif direction == "e":
        backward == "w"
    elif direction == "w":
        backward == "e"
    return backward


# create a return path option:
return_path = []
go_back = Stack()  # create a stack in case we need to go backward at a dead end
# crate a get_neighboring_rooms function


def get_neighboring_rooms(self):  # get the neighboring rooms
    # return the rooms neighboring rooms.
    return self.room.get_exits()

# get neighboring room valid exits


# def get_unchecked_exits_for_current_room(self, exits):
#     # make a new box for valid exits, for path exploration
#     valid_pathways = []
#     total_exits = self.get_neighboring_rooms()  # set all the exits
#     # loop through the exits and see which are ?
#     for ex in total_exits:
#         if ex == "?":
#             valid_pathways.append(ex)
#     return valid_pathways

    # define character movement


def dft_player_movement(self, starting_room):
    stack = Stack()
    stack.push(starting_room)
    visited = set()

    while stack.size() > 0:
        current_room = stack.pop()

        if current_room not in visited:
            print(current_room)
            visited.add(current_room)

            for neighbor in self.get_neighboring_rooms(current_room):
                stack.push(neighbor)

# define searchign for new rooms


def bfs_search_unexplored(self, starting_room, destination_room):
    queue = Queue()
    visited = set()
    queue.enqueue([starting_room])
    while queue.size() > 0:
        current_path = queue.dequeue()

        path = current_path[-1]

        if path is destination_room:
            return current_path

        if path not in visited:
            visited.add(path)

            for neighbor in self.get_neighboring_rooms(path):
                copy_path = current_path.copy()
                copy_path.append(neighbor)
                queue.enqueue(copy_path)

# make a random chooser for first room


def choose_room_randomly(self):
    ran = random.randrange(0, 3)
    if ran == 0:
        dir = "n"
    elif ran == 1:
        dir = "s"
    elif ran == 2:
        dir = "w"
    elif ran == 3:
        dir = "e"
    return dir


def check(exits):
    go_back = False
    room = player.current_room.name.split(" ")
    index = int(room[1])
    valid_directions = []

    for exit in exits:
        if traversal_graph[index][exit] == "?":
            valid_directions.append(exit)

    if len(valid_directions) == 0:
        go_back = True
        return return_path.pop()

    if go_back:
        for path in valid_directions:
            if path:
                go_back = False
                return path
            else:
                go_back = True
                return return_path.pop()

    else:
        if len(traversal_path) != 0:
            if player.current_room not in visited_rooms:
                for path in valid_directions:
                    if traversal_graph[index][path] != back_direction(traversal_path[-1]):
                        go_back = False
                        return path
            else:
                go_back = True
                return return_path.pop()
        else:
            for path in valid_directions:
                go_back = False
                return path


def lets_go(room):
    pass


################################################################
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
