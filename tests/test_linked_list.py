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
def test_insert_at_beginning():
    ll = linked_list()
    ll.insert(0, 10)



def test_insert_invalid_index():
    ll = linked_list()

    with pytest.raises(IndexError):
        ll.insert(5, 100)

def test_remove_at():
    ll = linked_list()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    removed = ll.remove_at(1)

    assert removed == 2
    assert ll.length == 2
    

def test_clear():
    ll =linked_list()
    ll.append(1)
    ll.append(2)
    ll.clear()

