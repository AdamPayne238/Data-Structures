import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Queues follow the First-in-First-Out principle (FIFO)
# First one in line at the movies is the first to buy a ticket and enjoy the movie


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # enqueue - adds an element to the end of the queue
    def enqueue(self, value):
        # and of queue is tail same as end of line
        self.storage.add_to_tail(value)
        self.size += 1

    # dequeue - removes the element at the beginning of the queue
    def dequeue(self):
        # remove_from_head - head is the beginning of the queue
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size
