#!python
from queue import LinkedQueue
from stack import LinkedStack
from linkedlist import LinkedList

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        # self.height = 0
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

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best and worst case running time: O(log(n)) if tree is balanced.  O(n) if tree is unbalanced"""
        #  Check if left child has a value and if so calculate its height
        height_left = 0
        print(self.data, self.left,self.right)
        if self.left:
            height_left = 1 + self.left.height()

        #  Check if right child has a value and if so calculate its height
        height_right =  0
        if self.right:
            height_right = 1 + self.right.height()

        # self.height = max(height_left, height_right)
        return max(height_left, height_right)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        #  Check if root node has a value and if so calculate its height
        if self.root:
            node = self.root
        return node.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None


    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # node = self._find_node_iterative(item)
        #  Return the node's data if found, or None
        return node.data if node else None
        

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            #  Create a new root node
            self.root = BinaryTreeNode(item)
            #  Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # parent = self._find_parent_node_iterative(item)
        #  Check if the given item should be inserted left of parent node
        if item < parent.data:
            #  Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        #  Check if the given item should be inserted right of parent node
        elif item > parent.data:
            #  Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        #  Increase the tree size
        self.size += 1
    
    def _find_balance(self, item):
        """Find balance factor of a given node item"""
        node = self._find_node_iterative(item)
        print("balance node",node)
    #   left_child, right_child = node.left, node.right
        left_child_h, right_child_h = 0, 0
        # base case, item is root
        print("left",node.left)
        print("right",node.right)
        if node.left: left_child_h = node.left.height() + 1
        if node.right: right_child_h = node.right.height() + 1
        return left_child_h - right_child_h

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node."""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            #  Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            #  Check if the given item is less than the node's data
            elif item < node.data:
                #  Descend to the node's left child
                node = node.left
            #  Check if the given item is greater than the node's data
            elif item > node.data:
                #  Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Check if starting node exists
        if node is None:
            return None         # Not found (base case)
        #  Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        #  Check if the given item is less than the node's data
        elif item < node.data:
            #  Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        #  Check if the given item is greater than the node's data
        elif item > node.data:
            #  Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            #  Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            #  Check if the given item is less than the node's data
            elif item < node.data:
                #  Update the parent and descend to the node's left child
                parent = node
                node = node.left
            #  Check if the given item is greater than the node's data
            elif item > node.data:
                #  Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        #  Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        #  Check if the given item is less than the node's data
        elif item < node.data:
            #  Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)  # Hint: Remember to update the parent parameter
        #  Check if the given item is greater than the node's data
        elif item > node.data:
            #  Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)   # Hint: Remember to update the parent parameter

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        # item doesnt exist
        if not self.contains(item):
            raise ValueError('Given item not in tree')
        
        
        node = self._find_node_recursive(item, self.root)          # Find Node to be deleted
        
        parent = self._find_parent_node_recursive(item, node)      # Find Parent of node to delete

        # Node is a leaf
        if node.is_leaf:
            node.data = None                                        # Remove data from node
            if parent.left == node:                                 # If node is left child, remove pointer
                parent.left = None
            elif parent.right == node:                              # If node is right child, remove pointer
                parent.right = None
                
        # Node to delete has one child
        if node.left == None or node.right == None:
            node.data = None                                        # Remove data from node
            if node == parent.left:                                 # If node is left child, remove pointer
                if node.left:
                    parent.left = node.left
                if node.right:
                    parent.left = node.right
            if node == parent.right:
                if node.left:
                    parent.right = node.left
                if node.right:
                    parent.right = node.right

        # Node to delete has 2 children
        if node.left != None and node.right != None:
            successor = node.right

            while successor.is_leaf() == False:
                successor = successor.left

            successor.left = node.left
            successor.right = node.right

            if parent:
                if node == parent.left:                                 # If node is left child, remove pointer
                    parent.left.data = successor.data
                if node == parent.right:
                    parent.right.data = successor.data
                successor_parent = self._find_parent_node_recursive(successor.data, successor)
                successor_parent.left = None                   
            else:
                self.root.data = successor.data

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            # self._traverse_in_order_recursive(self.root, items.append)
            self._traverse_in_order_iterative(self.root, items.append)
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
            self._traverse_in_order_recursive(node.left, visit)
        #  Visit this node's data with given function
            visit(node.data)
        #  Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)
        
        

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time:   O(3n) because each node is called  3 times.
                        Reduces to O(n)
        Memory usage:   If tree is balanced, height of tree is approx log(n) and memory
                        usage is O(log(n))
                        If Tree is unblanced, height of tree is approx n and
                        memory usasge is O(n)"""
        #  Traverse in-order without using recursion (stretch challenge)
        stack = LinkedStack()

        while True:
            if node == None:
                if stack.is_empty():
                    break
                pop = stack.pop()
                visit(pop.data)
                node = pop.right
            else:
                stack.push(node)
                node = node.left
                




    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_iterative(self.root, items.append)
            # self._traverse_pre_order_recursive(self.root, items.append)
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
            self._traverse_pre_order_recursive(node.left, visit)    #  Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)   #  Traverse right subtree, if it exists

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time:   O(3n) because each node is called recursively 3 times.
                        Reduces to O(n)
        Memory usage:   If tree is balanced, height of tree is log(n) and memory
                        usage is O(log(n))
                        If Tree is unblanced, height of tree is approx n and
                        memory usasge is O(n)"""
        #  Traverse pre-order without using recursion (stretch challenge)
        stack = LinkedStack()
        stack.push(node)
        while not stack.is_empty():
            node = stack.pop()
            visit(node.data)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)
            

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        items_linked = LinkedList()
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            # self._traverse_post_order_recursive(self.root, items.append)
            self._traverse_post_order_iterative(self.root, items_linked.prepend)
        # Return post-order list of all items in tree
        # return items
        return items_linked.items()

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is not None:
            self._traverse_post_order_recursive(node.left, visit)
            self._traverse_post_order_recursive(node.right, visit)
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
         Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        #  Traverse post-order without using recursion (stretch challenge)
        stack = LinkedStack()
        stack.push(node)
        while not stack.is_empty():
            node = stack.pop()
            visit(node.data)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)


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
            if node.left is not None:
                queue.enqueue(node.left)
            #  Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)



def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    items = [3, 2, 1]
    # print('items: {}'.format(items))

    tree = BinarySearchTree()
    # print('tree: {}'.format(tree))
    # print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        # print('insert({}), size: {}'.format(item, tree.size))
    # print('root: {}'.format(tree.root))

    for item in items:
      print('item({}), balance: {}'.format(item, tree._find_balance(item)))

    # print('\nSearching for items:')
    # for item in items:
    #     result = tree.search(item)
    #     print('search({}): {}'.format(item, result))
    # item = 123
    # result = tree.search(item)
    # print('search({}): {}'.format(item, result))

    # print('\nTraversing items:')
    # print('items in-order:    {}'.format(tree.items_in_order()))
    # print('items pre-order:   {}'.format(tree.items_pre_order()))
    # print('items post-order:  {}'.format(tree.items_post_order()))
    # print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
