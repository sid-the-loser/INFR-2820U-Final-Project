class TrieNode: # Trie data structure definition starts here
    def __init__(self):
        self.children = [None] * 26 # multiplied by 26 because there are 26 characters in the english alphabet
        self.is_end_of_word = False # flag that checks if the current node is a complete word or not

def insert(root: TrieNode, key: str) -> None: # function that is used for inserting words into trie
    key = key.lower() # we only want the key we're inserting for to be in lowercase to avoid ASCII value issues
                      # eg: ord("A") => 65
                      #     ord("a") => 97
                      #     where, `ord()` function returns the ASCII value of the character that's passed through it.

    node = root # this variable keeps track of the current node

    for char in key: # iterated through the string in key
        i = ord(char) - 97 # 97 is the ASCII value of "a"

        if node.children[i] is None: # checks if that child node doesn't exist (i.e., is it null)
            node.children[i] = TrieNode() # assigns a new node as the child to that node

        node = node.children[i] # moves the pointer of the trie to the next pre-existing or newly created node

    node.is_end_of_word = True # last node that was inserted is deemed as the end of a word

def loose_search(root: TrieNode, key: str) -> list[str]: # a search algorithm that helps search for similar patterns in
                                                         # tries
    pass # will be added soon