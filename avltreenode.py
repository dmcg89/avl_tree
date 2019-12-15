#!python
class AVLTreeNode(object):
    
    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.height = 0
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        #  Check if both left child and right child have no value

        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        #  Check if either left child or right child has a value
        has_left_child = self.left is not None
        has_right_child = self.right is not None
        return has_left_child or has_right_child
        # return True if self.left is not None or self.right is not None else False

    def update_height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""

        if self.is_leaf():
            self.height = 0
            return
        #  Check if left child has a value and if so calculate its height
        height_left = 0
        print(self.data, self.left,self.right)
        if self.left:
            height_left = 1 + self.left.update_height()

        #  Check if right child has a value and if so calculate its height
        height_right =  0
        if self.right:
            height_right = 1 + self.right.update_height()

        self.height = max(height_left, height_right)
        # return max(height_left, height_right)

    def find_balance(self):
        """Find balance factor of a given node object"""
        left_child_h, right_child_h = 0, 0
        if self.left: left_child_h = self.left.height + 1
        if self.right: right_child_h = self.right.height + 1
        return left_child_h - right_child_h

    def _rotate_right(self):
        left_node = self.left
        self.left = left_node.right
        left_node.right = self
        self.update_height()
        left_node.update_height()
        return left_node

    def _rotate_left(self):
        right_node = self.right
        self.right = right_node.left
        right_node.left = self
        self.update_height()
        right_node.update_height()
        return right_node