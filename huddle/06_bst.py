# 06. Árbol binario de búsqueda (BST): Implementa solo la inserción en un árbol binario de búsqueda para 5 elementos.

class TreeNode:
    def __init__(self, value):
        self.left = None 
        self.right = None 
        self.value = value 

    def insert(self, value):
        if value < self.value: 
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

tree = TreeNode(5)
tree.insert(2)
tree.insert(6)
tree.insert(4)
tree.insert(1)

# https://www.cs.usfca.edu/~galles/visualization/BST.html (For visualization purposes)

five = tree.value
two = tree.left.value 
six = tree.right.value 
four = tree.left.right.value 
one = tree.left.left.value

print(five, two, six, four, one)