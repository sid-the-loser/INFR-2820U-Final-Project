class Node: # Ternary Search Tree definition starts here
	def __init__(self, char: str):
		self.char = char # the character stored in this node
		self.is_end_of_word = False # is this node the end of a word
		self.left = None # left children (smaller than self.char)
		self.middle = None # middle children (equals to self.char)
		self.right = None # right children (greater than self.char)


def insert(root: Node, key: str) -> Node:
	if root is None:
		root = Node(key[0])

	elif root.char == "":
		root.char = key[0]

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

def exists(root: Node, key: str):
	if root is None:
		return None

	if key[0] < root.char:
		return exists(root.left, key)

	elif key[0] > root.char:
		return exists(root.right, key)

	else:
		if len(key) > 1:
			return exists(root.middle, key[1:])

		else:
			return root

def print_all_branches(root: Node, prefix: str) -> None:
	if root is None:
		return

	if root.is_end_of_word:
		print(prefix+root.char, end=", ")

	print_all_branches(root.middle, prefix+root.char)
	print_all_branches(root.left, prefix)
	print_all_branches(root.right, prefix)

def autocomplete(root: Node, key: str) -> None:
	node = exists(root, key)
	if node:
		print_all_branches(node.middle, key)

	else:
		print("No such word is in the TST!")


if __name__ == "__main__": # if the program is being run as its own file (i.e., not as a library or module)
	root_node = Node("")

	while True:
		ch = input("1.Insert\n2.Search\n\nEnter your choice here (1 or 2): ")
		print()
 
		if ch == "1":
			value = input("Enter the word to add to the autocomplete: ")
			insert(root_node, value)
			print(f"\"{value}\" added to autocomplete data.")
 
		elif ch == "2":
			value = input("Enter the word to autocomplete: ")
			autocomplete(root_node, value)
 
		else:
			print(f"{ch} is not an option, please try 1 or 2")
 
		print()

