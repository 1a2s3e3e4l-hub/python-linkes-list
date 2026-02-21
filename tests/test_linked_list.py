# test_linked_list.py
import pytest
from linked_list import linked_list , Node

def test_linked_test_creation():
    node: Node = Node(10)

    assert node.data == 10
    assert node.next is None

    ll:linked_list = linked_list()
    assert ll.head is None
    assert ll.length == 0