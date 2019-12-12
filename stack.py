#!python
# -*- coding: utf-8 -*-

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return self.list.size == 0

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return self.list.size


    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) - prepend at head"""
        # Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if self.is_empty():
            print('list is empty')
            return None

        return self.list.head.data 

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) - change head to head.next"""
        # Remove and return top item, if any (implement with self.list.delete instead)
        if self.is_empty():
            raise ValueError("Stack is empty!")
        top_item = self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1
        return top_item



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        #  Check if empty
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        #  Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1)* - generally empty space to append at end of list"""
        #  Insert given item
        self.list.append(item)
        return self

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        #  Return top item, if any
        if self.is_empty():             # return none if stack is empy
            return None

        item_index = self.length() - 1  # index for top of stack
        return self.list[item_index]    # return top of stack

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) pop at and of list is constant speed"""
        #  Remove and return top item, if any
        if self.is_empty():                     #check if stakc is empty
            raise ValueError("Stack is empty")
        
        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack

