class Node: # Trenary Search Tree definition starts here
    def __init__(self, char: str):
        self.char = char # the character stored in this node
        self.is_end_of_word = False # is this node the end of a word
        self.left = None # left children (smaller than self.char)
        self.middle = None # middle children (equals to self.char)
        self.right = None # right children (greater than self.char)


def insert(root: Node, key: str):
    if root is None:
        root = Node(key[0])

    if key[0] < root.char:
        root.left = insert(root.left, key)

    elif key[0] > root.char:
        root.right = insert(root.right, key)

    else:
        if len(key) > 1:
            root.middle = insert(root.middle, key[1:])

        else:
            root.is_end_of_word = True

    return root

def search(root: Node, key: str) -> bool:
	if root is None:
		return False
		
	if key[0] < root.char:
		return search(root.left, key)
		
	elif key[0] > root.char:
		return search(root.right, key)
	
	else:
		if len(key) > 1:
			return search(root.middle, key[1:])
			
		else:
			return root.is_end_of_word
		

def autocomplete(root: Node, key: str) -> None:
	if root is None:
		return False
    

if __name__ == "__main__": # if the program is being run as its own file (i.e., not as a library or module)
    root_node = Node("")
 
    while True:
        ch = int(input("1.Insert\n2.Search\n\nEnter your choice here (1 or 2): "))
        print()
 
        if ch == 1:
            value = input("Enter the word to add to the autocomplete: ")
            insert(root_node, value)
            print(f"\"{value}\" added to autocomplete data.")
 
        elif ch == 2:
            value = input("Enter the word to autocomplete: ")
            print(search(root_node, value))
 
        else:
            print(f"{ch} is not an option, please try 1 or 2")
 
        print()

