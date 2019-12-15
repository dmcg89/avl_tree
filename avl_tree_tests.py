from avl_tree import AVLSearchTree, AVLNode
import unittest
import numpy as np


class AVLNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = AVLNode(data)
        assert node.data is data
        assert node.left_child is None
        assert node.right_child is None

class AVLTreeTest(unittest.TestCase):

    def test_init(self):
        tree = AVLSearchTree()
        assert tree.root is None
        assert tree.is_empty() is True

    def test_init_with_list(self):
        tree = AVLSearchTree([2, 1, 3])
        assert tree.root.data == 2
        assert tree.root.left_child.data == 1
        assert tree.root.right_child.data == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_strings(self):
        tree = AVLSearchTree(['B', 'A', 'C'])
        assert tree.root.data == 'B'
        assert tree.root.left_child.data == 'A'
        assert tree.root.right_child.data == 'C'
        assert tree.is_empty() is False

    def test_init_with_list_of_tuples(self):
        tree = AVLSearchTree([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.root.data == (2, 'B')
        assert tree.root.left_child.data == (1, 'A')
        assert tree.root.right_child.data == (3, 'C')
        assert tree.is_empty() is False

    def test_search_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        items = [2, 1, 3]
        tree = AVLSearchTree(items)
        assert tree.contains(1) is True
        assert tree.contains(2) is True
        assert tree.contains(3) is True
        assert tree.contains(4) is False

    def test_items_in_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = AVLSearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == ['A', 'B', 'C']

    def test_items_pre_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = AVLSearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == ['B', 'A', 'C']


    def test_items_level_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = AVLSearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == ['B', 'A', 'C']

    def test_items_in_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = AVLSearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == [1, 2, 3, 4, 5, 6, 7]

    def test_items_pre_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = AVLSearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == [4, 2, 1, 3, 6, 5, 7]

    def test_items_level_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = AVLSearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]
    
    def test_random_int_insert(self):
        items = np.random.randint(1,101,100)
        tree = AVLSearchTree(items)
        assert abs(tree.root.left_child.height - tree.root.right_child.height) <= 1
        assert abs(tree.root.left_child.left_child.height - tree.root.left_child.right_child.height) <= 1
        assert abs(tree.root.right_child.right_child.height - tree.root.right_child.left_child.height) <= 1

    # def test_random_int_insert(self):
    #     items = np.random.randint(1,101,100)
    #     tree = AVLSearchTree(items)
    #     assert abs(tree.root.left_child.height - tree.root.right_child.height) <= 1
    #     assert abs(tree.root.left_child.left_child.height - tree.root.left_child.right_child.height) <= 1
    #     assert abs(tree.root.right_child.right_child.height - tree.root.right_child.left_child.height) <= 1


if __name__ == '__main__':
    unittest.main()