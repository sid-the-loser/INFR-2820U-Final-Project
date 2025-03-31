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

def autocomplete(root: TrieNode, key: str):
    node = root

    prefix = ""

    for char in key:
        i = ord(char) - 97

        if node.children[i] is None:
            print("No such word found in the treap!")
            return

        prefix += char

        node = node.children[i]

    if node.is_end_of_word:
        print(prefix, end=", ")

    print_all_branches(node, key)

    print()

def print_all_branches(root: TrieNode, prefix: str):
    if root.is_end_of_word:
        print(prefix, end=", ")

    children_len = len(root.children)

    for i in range(children_len):
        if root.children[i] is not None:
            print_all_branches(root.children[i], prefix+chr(i+97))

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
            value = input("Enter the word to autocomplete: ")
            autocomplete(root_node, value)
            # print(search(root_node, value))

        else:
            print(f"{ch} is not an option, please try 1 or 2")

        print()