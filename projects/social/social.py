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
            for friend_id in range(user_id + 1, self.last_id + 1):
                # user_id == user_id_2 cannot happen
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

        visited = {}  # Note that this is a dictionary, not a set
        box = Queue()  # create a standard BFT
        # ENQUEUE THE LIST OBJECT TO ITERATE OVER (ARRAY)
        box.enqueue([user_id])
        chain = []  # make a list of paths
        while box.size() > 0:
            current_path = box.dequeue()
            current_user = current_path[-1]

            if current_user not in visited:  # if current user is not in visited
                # print(current_path)
                # visited at current user is the current path
                visited[current_user] = current_path

                # for the frien in get friends
                for friend in self.get_friends(current_user):
                    copy_path = current_path.copy()  # make a copy
                    # append the friend to copied path
                    copy_path.append(friend)
                    # append to the chain length of the copy path
                    chain.append(len(copy_path))
                    box.enqueue(copy_path)  # enqueue the copied path

        # get the avg degrees of separation
        print('avg degrees of separation:', sum(chain)/len(chain))

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
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
