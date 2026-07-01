class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        curr = self.root
        while True:
            if value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(value)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(value)
                    break

    def debug_print(self, node, depth=0):
        if node:
            self.debug_print(node.right, depth + 1)
            print("    " * depth + f"-> {node.value}")
            self.debug_print(node.left, depth + 1)

# --- Quick Test ---
tree = BinaryTree()
data = [50, 30, 70, 20, 40, 60, 80,100]

for x in data:
    tree.insert(x)

tree.debug_print(tree.root)