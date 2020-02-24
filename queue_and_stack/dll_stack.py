import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# Stacks follow Last-in-First-Out principle (LIFO)
# Just like stacking coins, the last coin we put on top is the one that is the first to be removed from the stack later
# Push - add an element to the top of the stack
# Pop  - removes the element at the top of the stack

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.size.append(value)

    def pop(self):
        pass

    def len(self):
        pass
