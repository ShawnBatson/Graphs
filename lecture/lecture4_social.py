import random


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


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        # maps ID's to user Objects (lookup table for User Objects given IDs)
        self.users = {}
        # Adjacency List
        # Maps user_id's to a list of other users (who are their friends)
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # generate all possible friendships
        # avoid duplicate friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, len(self.users.keys())):  # CHANGED
                # user_id == user_id_2 cannot ha ppen
                # if friendship between user_id and user_id_2 already exists,
                #   don't add friendship between user_2 and user
                possible_friendships.append((user_id, friend_id))

        # Randomly select X friendships
        # shuffle the array and pick X elements from the front of it.
        # the formula for X is num_users * avg_friendships // 2  (friendship goes 2 ways)
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_friends(self, user_id):  # make somethign to get neighbors (friends)
        # it's already done above, just set it
        user_friends = self.friendships[user_id]
        return user_friends  # return the result

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # create a queue
        queue = Queue()
        # create a set of visited prevoius seen vertices
        visited = {}  # Note that this is a dictionary, not a set
        # add first user id to the queue AS A PATH
        queue.enqueue([user_id])
        # While the queue is not empty
        while queue.size() > 0:
            current_path = queue.dequeue()
            # dequeue a current path
            # get the current vertex from end of path
            current_vertex = current_path[-1]
            if current_vertex not in visited:
                # add vertex to visited set
                visited[current_vertex] = current_path
                # also add the path that brought us to this vertex
                # i.e. add a key and value to the visited dictionary
                # the key is the current vertex, and the value is the path
                # queue up all neighbors as paths
                for neighbor in self.friendships[current_vertex]:
                    # make a new copy of the current path
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

        return visited


# answers to part 3 questions beneath:
'''
1. You would have to call the add friendship function 500 times. Because the mathematics for it is number of users * avg friends // 2, because you do not need to count the reverse of (1, 2), which is (2, 1) because it is implied in (1, 2).

2. I am seeing 99% With my code, I am getting an average of 6 degrees of separation with 1000 users and 5 friends. With testing, I am getting 5-7 average degrees of separation.


Stretch Question:

1.  This isn't necessarily surprising.  The randomization causes an order to the chaos. Real life would be much more structured, including variables such as having in common: work, hobbies, interests, etc, and because of this, I would not expect it in real life.  The actual average degrees of separation, according to multiple articles, and specifically facebooks testing group, is 3.57 degrees of separation within clusters, spanning millions of people.  This in itself is a bit surprising, because the clusters are expansive.  You could essentially improve it by adding clusters of variables that show reasons for the connection being made, and removing some of the randomness.

Source: https://research.fb.com/blog/2016/02/three-and-a-half-degrees-of-separation/

'''


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(5, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
