import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Queues follow the First-in-First-Out principle (FIFO)
# First one in line at the movies is the first to buy a ticket and enjoy the movie
# enqueue - adds an element to the end of the queue
# dequeue - removes the element at the beginning of the queue

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def len(self):
        pass
