import sys

sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# Q breadth for search.
# Stack depth for search. Top to bottom, left to right

# Binary Search Tree is a node-based binary tree data structure which has the following properties:
# The left subtree of a node contains only nodes with keys lesser than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.

# Insert Value
# If no root node, insert as root node (first in tree)
# If node being inserted is greater than root node
# Move right
# If node being inserted is less than root node
# Move left
# If node has traversed and no more nodes to compare. Insert here.

# Find Value
# If no node at root: return false
# Compare value to root
# if smaller:
# Go left. Look at node there
# If Greater or ==:
# Go right.

# Get Max
# If no right child. Return this value
# Otherwise continue right in the tree to find the largest node


# Left and right are children of node

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 1. Insert the given value into the tree
    # insert adds the input value to the binary search tree, adhering to the rules of the
    # ordering of elements in a binary search tree.
    def insert(self, value):

        node = BinarySearchTree(value)

        # if inserted value is > node
        if value > self.value:
            # if no value right
            if self.right is None:
                # set right to node
                self.right = node
            else:
                # recurse insert right child value
                return self.right.insert(value)

        # if inserted value is < node
        elif value < self.value:
            # if no value left
            if self.left is None:
                # set left to node
                self.left = node
            else:
                # recurse insert left child value
                return self.left.insert(value)

    # 2. Return True if the tree contains the value. False if it does not
    def contains(self, target):

        if self.value == target:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # 3. Return the maximum value found in the tree
    def get_max(self):

        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # 4. Call the function `cb` on the value of each node. You may use a recursive or iterative approach
    # for_each performs a traversal of every node in the tree, executing the passed-in callback function on each
    # tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work.
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
