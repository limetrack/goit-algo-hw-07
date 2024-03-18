class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_min_value(node):
    current = node
    # просуваємося до найлівішого вузла
    while(current.left is not None):
        current = current.left
    return current.val

# Демонстрація використання
root = None
root = insert(root, 15)
insert(root, 10)
insert(root, 20)
insert(root, 25)
insert(root, 8)
insert(root, 12)

print("Найменше значення в дереві:", find_min_value(root))
