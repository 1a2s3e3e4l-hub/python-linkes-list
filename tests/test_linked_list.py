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

def test_append_and_length():
    ll = linked_list()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    assert ll.length == 3