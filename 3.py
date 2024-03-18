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

def sum_of_values(node):
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

# Демонстрація використання
root = None
root = insert(root, 15)
insert(root, 10)
insert(root, 20)
insert(root, 25)
insert(root, 8)
insert(root, 12)

print("Сума всіх значень у дереві:", sum_of_values(root))
