from dataclasses import dataclass

from nodes import BiNode


@dataclass
class BinaryTree:
    root: BiNode

    @staticmethod
    def preorder_traverse(root: BiNode):
        if root:
            yield root.value
            if root.left is not None:
                yield from BinaryTree.preorder_traverse(root.left)
            if root.right is not None:
                yield from BinaryTree.preorder_traverse(root.right)

    @staticmethod
    def inorder_traverse(root: BiNode):
        if root:
            if root.left is not None:
                yield from BinaryTree.inorder_traverse(root.left)
            yield root.value
            if root.right is not None:
                yield from BinaryTree.inorder_traverse(root.right)

    @staticmethod
    def postorder_traverse(root: BiNode):
        if root:
            if root.left is not None:
                yield from BinaryTree.postorder_traverse(root.left)
            if root.right is not None:
                yield from BinaryTree.postorder_traverse(root.right)
            yield root.value


if __name__ == "__main__":
    b1 = BiNode(1)
    b2 = BiNode(2)
    b3 = BiNode(3)
    b4 = BiNode(4)
    b5 = BiNode(5)
    b6 = BiNode(6)
    b7 = BiNode(7)
    b8 = BiNode(8)

    b8.left = b7
    b8.right = b6

    b6.left = b5
    b6.right = b4

    b5.left = b3

    b4.left = b2
    b4.right = b1

    btree = BinaryTree(root=b8)

    for i in BinaryTree.inorder_traverse(btree.root):
        print(i)
