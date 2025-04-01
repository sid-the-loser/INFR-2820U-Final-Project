class TrieNode: # Trie data structure definition starts here
    def __init__(self):
        self.children = [None] * 26 # multiplied by 26 because there are 26 characters in the english alphabet
        self.is_end_of_word = False # flag that checks if the current node is a complete word or not

def insert(root: TrieNode, key: str) -> None: # function that is used for inserting words into trie
    key = key.lower() # we only want the key we're inserting for to be in lowercase to avoid ASCII value issues
                      # eg: ord("A") => 65
                      #     ord("a") => 97
                      #     where, `ord()` function returns the ASCII value of the character that's passed through it

    node = root # this variable keeps track of the current node

    for char in key: # iterated through the string in key
        i = ord(char) - 97 # 97 is the ASCII value of "a"

        if node.children[i] is None: # checks if that child node doesn't exist (i.e., is it null)
            node.children[i] = TrieNode() # assigns a new node as the child to that node

        node = node.children[i] # moves the pointer of the trie to the next pre-existing or newly created node

    node.is_end_of_word = True # last node that was inserted is deemed as the end of a word

def autocomplete(root: TrieNode, key: str): # function to check if the word even exists in the trie, if it does
											# exist then using that prefix/key provided, print out the rest of 
											# the branches.
	node = root # this variable keeps track of the current node

	for char in key: # iterated through the string in key
		i = ord(char) - 97

		if node.children[i] is None: # checks if that child node doesn't exist (i.e., is it null)
			print("No such word found in the treap!") # prints out an error message and stops the function
			return

		node = node.children[i] # moves the pointer of the trie to the next pre-existing or newly created node

	if node.is_end_of_word: # is the node the end of the word then print a "," at the end
		print(key, end=", ")

	print_all_branches(node, key) # the function that traverses through all the given nodes children
								  # and prints them out

	print() # new line because the other function doesn't provide any new line once it's done traversing

def print_all_branches(root: TrieNode, prefix: str): # printing all the children using the given prefix
    if root.is_end_of_word: # if the node is the end of a word, then print the prefix and ","
        print(prefix, end=", ")

    for i in range(26): # traverses through all the children of the node and recurses this function if the node exists
        if root.children[i] is not None:
            print_all_branches(root.children[i], prefix+chr(i+97))

if __name__ == "__main__": # if the program is being run as its own file (i.e., not as a library or module)
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

        else:
            print(f"{ch} is not an option, please try 1 or 2")

        print()
