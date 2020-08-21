# Given two words (begin_word and end_word), and a dictionary's word list,
# return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None
f = open('lecture/words.txt', 'r')
words = f.read().split("\n")
f.close()
# Put our words in a set for O(1) lookup
word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    neighbors = set()
    # a neighbor for a word is any word thats different by one letter
    # and is inside word_list
    string_word = list(word)
    for i in range(len(string_word)):
        # swap each character with a character from the letters list
        for letter in letters:
            new_word = list(string_word)
            # place new letter at current position in the word
            new_word[i] = letter
            # convert the word back to a string
            new_word_string = "".join(new_word)
            # check if its a real word
            if new_word_string != word and new_word_string in word_set:
                neighbors.add(new_word_string)
    return neighbors


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


def find_word_path(begin_word, end_word):
    # do BFS
    # create a queue
    queue = Queue()
    # create a visited set
    visited = set()
    # add start word to Queue (like a path)
    queue.enqueue([begin_word])
    # while queue not empty
    while queue.size() > 0:
        # pop current word off queue
        current_path = queue.dequeue()
        current_word = current_path[-1]
        # if word has not been visited:
        if current_word not in visited:
            # is current word the end word? If yes return path
            if current_word == end_word:
                return current_path
            # add current word to visited set
            visited.add(current_word)
            # add neighbors of current word to queue (like a path)
            for neighbor_word in get_neighbors(current_word):
                # make a copy
                new_path = list(current_path)
                new_path.append(neighbor_word)
                queue.enqueue(new_path)


print(find_word_path('ants', 'diet'))
print(find_word_path('plane', 'stove'))
print(find_word_path('lambda', 'google'))
