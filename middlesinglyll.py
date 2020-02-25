class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


class Singly:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def mid(self):
        it_one = self.head
        it_two = self.head
        while it_two is not None:
            it_one = it_one.next
            it_two = it_two.next
            it_two = it_two.next
        print(it_one.value)
        return it_one.value


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

# New Challenge

