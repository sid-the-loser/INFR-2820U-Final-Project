class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end_of_word = False