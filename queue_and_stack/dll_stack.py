import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Stacks follow Last-in-First-Out principle (LIFO)
# Just like stacking coins, the last coin we put on top is the one that is the first to be removed from the stack later


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # Push - add an element to the top of the stack
    def push(self, value):
        # Tail is top because the last item stacked is on top
        self.storage.add_to_tail(value)
        self.size += 1

    # Pop  - removes the element at the top of the stack
    def pop(self):
        # remove_from_tail (last item in stack is on top (last-in-first-out))
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
