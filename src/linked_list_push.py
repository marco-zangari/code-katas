"""Linked Lists - Push & BuildOneTwoThree, codewars kata, level 7."""


class Node(object):
    """Build class for node object."""

    def __init__(self, data):
        """Init method."""
        self.data = data
        self.next = None

def push(head, data):
    """Push method on linked list."""
  new_node = Node(data)
  new_node.next = head
  return new_node

def build_one_two_three():
    """Build out the linked list with three nodes."""
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained
