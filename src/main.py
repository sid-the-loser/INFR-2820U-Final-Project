# Code by: Sidharth Suresh

# This file is supposed to be run on its own but can also be renamed and used as a library is needed.

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

# THIS FUNCTION IS NOT A PART OF THIS PROJECT! THIS FUNCTION WAS IMPLEMENTED JUST FOR TESTING PURPOSES!
def search(root: TrieNode, key: str) -> bool: #list[str]: # a search algorithm that helps search for the exact pattern
    # of words in a trie
    node = root

    for char in key:
        i = ord(char) - 97

        if node.children[i] is None:
            return False

        node = node.children[i]

    return node.is_end_of_word

def loose_search(root: TrieNode, key: str) -> list[str]:
    pass

if __name__ == "__main__":
    root_node = TrieNode()

    while True:
        ch = int(input("1.Insert\n2.Search\n\nEnter your choice here (1 or 2): "))
        print()

        if ch == 1:
            value = input("Enter the word to add to the autocomplete: ")
            insert(root_node, value)
            print(f"\"{value}\" added to autocomplete data.")

        elif ch == 2:
            pass

        else:
            print(f"{ch} is not an option, please try 1 or 2")

        print()