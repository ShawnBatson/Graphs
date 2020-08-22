class Stack():  # bring in the stack. ANSWER IS FARTHEST AWAY. STACK TO BE USED
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


# in ancestor, 0 is the parent, 1 is the child. The child will be the current in the earliest_ancestor function.
def parents(kid, ancestor):
    parent_box = []  # box
    for person in ancestor:  # loop over parents at the 0, check to see if parameter is the current kid
        if person[1] == kid:
            # if the person at index 1 is the kid, add the parent to the parent_box
            # find any and all parents of the child.
            parent_box.append(person[0])
    return parent_box  # return the box with the parents of said child in it.

# create a normal DFT


def earliest_ancestor(ancestors, starting_node):
    stack_box = Stack()  # stack box
    visited_vert = set()  # visited vertices
    stack_box.push(starting_node)  # push the first starting_node to begin
    parent_box = []  # parent box is back.

    while stack_box.size() > 0:  # while the stack_box is greater than 0
        current = stack_box.pop()   # set the current to the popped value

        if current not in visited_vert:  # if current is not in visited vert
            # add it.  This is a normal dft up to here.
            visited_vert.add(current)

            # chec to see if current has any parents, if so, return them via helper function.
            parent_tally = parents(current, ancestors)

            if parent_tally:  # if there are parents in that parent_tally
                parent_box = parent_tally  # set the parent box to the parent tally

                for parent in parent_box:  # for the parents in parent_box
                    stack_box.push(parent)  # push them to the stack box

        # add base case (this has to be after the while loop otherwise it throws immediately.)
        if len(parent_box) == 0:
            return -1
    # the minimum of the parent_box is the farthest from the starting node
    oldest_ancestor = min(parent_box)
    return oldest_ancestor  # return it
