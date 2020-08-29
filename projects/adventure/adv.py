from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue():  # bring in a Queue
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


class Stack():  # bring in a stack
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
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

####################################################


# create a function that has the reversal of all diretions, so you can create a backwards pathway.
def goBack(dir):
    if dir == 'n':
        opposite = 's'
    elif dir == 's':
        opposite = 'n'
    elif dir == 'e':
        opposite = 'w'
    elif dir == 'w':
        opposite = 'e'
    return opposite


# make a random chooser for first room

def choose_room_randomly(self):  # create a random room generator.
    ran = random.randrange(0, 4)
    if ran == 0:
        dir = "n"
    elif ran == 1:
        dir = "s"
    elif ran == 2:
        dir = "w"
    elif ran == 3:
        dir = "e"
    return dir

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


traversal_path = []

################################################################


traversal_graph = {}  # set my "traversal graph"
visited = set()  # set a visited set
visited.add(player.current_room)  # add the payers room to the visited set
# create a return path option:
return_path = Stack()
# create a stack in case we need to go backward at a dead end
reverse = False  # set a boolean for a case.

for i in range(len(room_graph)):
    traversal_graph[i] = {'n': '?', 's': '?', 'e': '?',
                          'w': '?'}  # set the new graph to blank "?'s"


def check_exits(exits):
    global reverse  # boolean will help here. ### HAD to set it to global,
    room = player.current_room.name.split(" ")  # split the room name
    index = int(room[1])  # create an index..postion in column
    pathways = []  # create a valid directions pathways list

    for ex in exits:  # for all the exits in parameter
        if traversal_graph[index][ex] == "?":  # if any are "?"
            pathways.append(ex)  # append that to the valid diretions
    # TIER 1
    if len(pathways) == 0:  # If the valid directions length is 0, go back
        reverse = True
        return return_path.pop()  # move in the return path diretion until you find a ?
    # TIER 1
    if reverse:  # if you are reversing
        for path in pathways:  # for the path in diretions TIER 2
            if path:  # if there is a valid direction (?), go that way TIER 3
                reverse = False  # continue on new path, set the boolean to false
                return path  # return the path and keep going
            else:  # TIER 3
                reverse = True  # otherwise set reverse to true and move backwards
                return return_path.pop()  # head back through the return path.

    else:  # TIER 1
        if len(traversal_path) != 0:  # if the length of the path is not 0, TIER 2
            if player.current_room not in visited:  # and room is not in visited, TIER 3
                for path in pathways:  # for the valid paths TIER 4
                    # TIER 5
                    if traversal_graph[index][path] != goBack(traversal_path[-1]):
                        reverse = False
                        return path
            else:  # if the current room is in visited rooms, go back TIER 3
                reverse = True
                return return_path.pop()  # head back
        else:  # TIER 2
            for path in pathways:  # TIER 3
                reverse = False
                return path


# def lets_go(room):

#     split_room = previous_room.name.spit(" ")
#     previous_index = int(split_room[1])

#     current_split = room.name.split(" ")
#     current_index = int(current_split[1])

#     previous_direction = traversal_path[-1]

#     traversal_graph[previous_index][previous_direction] = room
#     traversal_graph[current_index][goBack(
#         previous_direction)] = previous_room

#     if previous_room not in visited:
#         visited.add(previous_room)
#     while len(visited_rooms) != len(room_graph):
#         current = player.current_room
#         split_r = current.name.split(' ')
#         index = int(split_r[1])

#         current_exits = current.get_neighboring_rooms()
#         valid_move = check(current_exits)

#         if valid_move is not None:
#             traversal_path.append(valid_move)

#             if not return_path:
#                 return_path.append(goBack(valid_move))

#             previous_room = current

#             player.travel(valid_move)

#             lets_go(player.current)


def lets_go(room):
    if previous_room not in visited:  # if the previous room is not in visited
        visited.add(previous_room)  # add it to visited
    # grab the integer part of the prev room name
    # split the name of the previous room
    split_room = previous_room.name.split(' ')
    previous_index = int(split_room[1])  # set that to previous index

    # grab the int part of the curren room name
    current_split = room.name.split(' ')  # split the name of the current room
    current_index = int(current_split[1])  # set that to current index
    # add last visited room's ('traversal_path' last entry) dir to traversal 'graph' as current_room
    recent_direction = traversal_path[-1]

    # connect the 2 rooms together
    # add current path to traversal_graph
    traversal_graph[previous_index][recent_direction] = room
    # add the reversed path to traversal_graph
    traversal_graph[current_index][goBack(recent_direction)] = previous_room


# while the length of visited is not the length of the graph (finished)
while len(visited) != len(room_graph):
    current_room = player.current_room  # current room is player.current_room

    # grab the integer in the room name
    # split the room name again to get index
    split_room = current_room.name.split(' ')
    ind = int(split_room[1])  # set it to ind

    current_exits = current_room.get_exits()  # get all the exits for current room

    # moving
    travel_direction = check_exits(current_exits)  # set the travel directions
    if travel_direction is not None:  # as long as it's not none

        # add to traversal_path
        # append that direction to the path
        traversal_path.append(travel_direction)

        if not reverse:  # as long as you're not reversing
            # go back to the nearest room that has a ? exit
            return_path.push(goBack(travel_direction))

        previous_room = current_room  # set the previous room to the current room
        # MOVE
        player.travel(travel_direction)
        # visit next room
        lets_go(player.current_room)  # recurse

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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
