#!python

"""Credit: Alan Davis CS1.3 Binary Search Tree starter code
           AVL Tutorial: https://www.youtube.com/watch?v=lxHF-mVdwK8"""

from queue import LinkedQueue
from stack import LinkedStack
from linkedlist import LinkedList
import numpy as np

class AVLNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.height = 0
        self.left_child = None
        self.right_child = None
        self.parent = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'AVLNode({!r})'.format(self.data)


class AVLSearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        if items is not None:
            for item in items:
                self.insert(item)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        if self.root:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node,  cur_height):
        if cur_node == None: return cur_height

        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)

        return max(left_height,right_height)

    def contains(self, data):
        """Returns true if node exists in tree"""
        if self.root:
            return self._contains(data, self.root)
        else:
            return False

    def _contains(self, data, cur_node):
        if data == cur_node.data: return True

        elif data < cur_node.data and cur_node.left_child:
            return self._contains(data, cur_node.left_child)

        elif data > cur_node.data and cur_node.right_child:
            return self._contains(data, cur_node.right_child)
        return False 

    def insert(self, data):
        if self.root == None:
            self.root = AVLNode(data)
        else:
            self._insert(data ,self.root)

    def _insert(self, data, cur_node):
        """Recursively add new node to appropriate place in tree"""
        if data < cur_node.data:
            if cur_node.left_child == None:
                cur_node.left_child = AVLNode(data)
                cur_node.left_child.parent=cur_node # set parent
                self._check_balance(cur_node.left_child)
            else:
                self._insert(data, cur_node.left_child)
        elif data > cur_node.data:
            if cur_node.right_child == None:
                cur_node.right_child = AVLNode(data)
                cur_node.right_child.parent = cur_node # set parent
                self._check_balance(cur_node.right_child)
            else:
                self._insert(data,cur_node.right_child)
        else:
            print("data already in tree!")

    def _check_balance(self,cur_node,path = []):
        if cur_node.parent==None: return
        path = [cur_node] + path
        # path.append(cur_node)
        # print(path)

        left_height =self.get_height(cur_node.parent.left_child)
        right_height=self.get_height(cur_node.parent.right_child)

        if abs(left_height-right_height)>1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0],path[1],path[2])
            return

        new_height = 1 + cur_node.height 
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._check_balance(cur_node.parent, path)

    def _rebalance_node(self, z, y, x):
        if y == z.left_child and x == y.left_child:
            self._right_rotate(z)
        elif y == z.left_child and x == y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right_child and x == y.right_child:
            self._left_rotate(z)
        elif y == z.right_child and x == y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)

    def _right_rotate(self, z):
        sub_root = z.parent 
        y = z.left_child
        t3 = y.right_child
        y.right_child = z
        z.parent = y
        z.left_child = t3
        if t3: t3.parent=z
        y.parent = sub_root
        if y.parent == None:
                self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))

    def _left_rotate(self,z):
        sub_root = z.parent 
        y = z.right_child
        t2 = y.left_child
        y.left_child = z
        z.parent = y
        z.right_child = t2
        if t2: t2.parent = z
        y.parent = sub_root
        if y.parent == None: 
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height= 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height= 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))

    def get_height(self,cur_node):
        if cur_node == None: return 0
        return cur_node.height

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
            # self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time:   O(3n) because each node is called recursively 3 times.
                        Reduces to O(n)
        Memory usage:   If tree is balanced, height of tree is log(n) and memory
                        usage is O(log(n))
                        If Tree is unblanced, height of tree is approx n and
                        memory usasge is O(n)"""
        #  Traverse left subtree, if it exists
        if node is not None:
            self._traverse_in_order_recursive(node.left_child, visit)
        #  Visit this node's data with given function
            visit(node.data)
        #  Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right_child, visit)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            # self._traverse_pre_order_iterative(self.root, items.append)
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items


    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time:   O(3n) because each node is called recursively 3 times.
                        Reduces to O(n)
        Memory usage:   If tree is balanced, height of tree is log(n) and memory
                        usage is O(log(n))
                        If Tree is unblanced, height of tree is approx n and
                        memory usasge is O(n)"""


        if node is not None:
            visit(node.data)                                        #  Visit this node's data with given function
            self._traverse_pre_order_recursive(node.left_child, visit)    #  Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.right_child, visit)   #  Traverse right subtree, if it exists


    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time:   4 operations for each visited node (dequeue, visit, 2 enqueues(children))
                        O(4n) reduces to O(n)
        Memory usage:   'Width' of tree or most items that end up in queue O(w)
                        Worst case is a balanced tree or greatest # of leaves"""
        #  Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        #  Enqueue given starting node
        queue.enqueue(start_node)
        #  Loop until queue is empty
        while queue.is_empty() == False:
            #  Dequeue node at front of queue
            node = queue.dequeue()
            #  Visit this node's data with given function
            visit(node.data)
            #  Enqueue this node's left child, if it exists
            if node.left_child is not None:
                queue.enqueue(node.left_child)
            #  Enqueue this node's right child, if it exists
            if node.right_child is not None:
                queue.enqueue(node.right_child)



def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]
    items = np.random.randint(1,101,100)
    
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    #items = [15,9,20,21,22]
    # items = [15,9,18,6,5]
    # items = [15,9,6]
    # items = [10, 5, 7]
    # print('items: {}'.format(items))

    tree = AVLSearchTree(items)
    print(len(items))
    print(tree)
    print(tree.root.left_child.height)
    print(tree.root.right_child.height)
    # print('tree: {}'.format(tree))
    # print('root: {}'.format(tree.root))

    # print('\nInserting items:')
    # for item in items:
    #     print("inserting",item)
    #     tree.insert(item)
        # print('insert({}), size: {}'.format(item, tree.size))
    # print('root: {}'.format(tree.root))

    # print('\nSearching for items:')
    # for item in items:
    #     result = tree.search(item)
    #     print('search({}): {}'.format(item, result))
    # item = 123
    # result = tree.search(item)
    # print('search({}): {}'.format(item, result))

    # print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    # print('items pre-order:   {}'.format(tree.items_pre_order()))
    # print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()