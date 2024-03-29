class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_bst(data):
    if not data:
        return None
    
    root = TreeNode(data[0])
    
    for char in data[1:]:
        insert_node(root, char)
    
    return root

def insert_node(root, char):
    if char < root.data:
        if root.left is None:
            root.left = TreeNode(char)
        else:
            insert_node(root.left, char)
    elif char > root.data:
        if root.right is None:
            root.right = TreeNode(char)
        else:
            insert_node(root.right, char)

def preorder_traversal(root):
    if root:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Input
N = int(input())
data = input().split()

# Construct BST
root = construct_bst(data)

# Perform pre-order traversal
preorder_traversal(root)
