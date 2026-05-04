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

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.key)
        inorder(root.right, result)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = minValueNode(root.right)
        root.key = temp.key 
        root.right = delete(root.right, temp.key)  
    
    return root

insert_keys = [50, 30, 70, 20, 40, 60, 80]
delete_keys = [30, 50, 70]  

root = None
for key in insert_keys:
    root = insert(root, key)

print("Initial inorder:", end=' ')
initial_result = []
inorder(root, initial_result)
print(initial_result)

for del_key in delete_keys:
    print(f"\nDeleting {del_key}:")
    root = delete(root, del_key)
    result = []
    inorder(root, result)
    print("Inorder after delete:", result)