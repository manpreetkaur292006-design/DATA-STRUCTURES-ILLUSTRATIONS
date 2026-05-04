class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    elif root.key == key:
        return root  
    elif root.key < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root is not None
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.key)
        inorder(root.right, result)
insert_keys = [50, 30, 70, 20, 40, 60, 80]
search_keys = [25, 70, 90]
root = None
for key in insert_keys:
    root = insert(root, key)
inorder_result = []
inorder(root, inorder_result)
print("Inorder traversal (sorted):", inorder_result)
print("\nSearch results:")
for key in search_keys:
    status = "Found" if search(root, key) else "Not Found"
    print(f"Key {key}: {status}")