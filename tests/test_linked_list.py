import pytest

from src.lab10.linked_list import SinglyLinkedList


@pytest.fixture
def si():
    si = SinglyLinkedList()
    si.append(333)
    si.append("Yes")
    return si


def test_append_node():
    si = SinglyLinkedList()
    si.append(333)
    assert si._size == 1
    node = si.head
    assert node.value == 333


def test_four_append_node(si):
    si.append("No")
    si.append("Maybe")
    assert si._size == 4
    assert si.head.value == 333
    assert si.head.next.value == "Yes"
    assert si.head.next.next.value == "No"
    assert si.head.next.next.next.value == "Maybe"


def test_pretend_node(si):
    si.prepend("No")
    assert si.head.value == "No"
    assert si.head.next.value == 333
    assert si.head.next.next.value == "Yes"
    assert len(si) == 3


def test_insert_node(si):
    si.append("No")
    si.insert(1, "Maybe")
    assert si.head.value == 333
    assert si.head.next.value == "Maybe"
    assert si.head.next.next.value == "Yes"
    assert si.head.next.next.next.value == "No"
    assert len(si) == 4


def test_iter(si):
    si.append("No")

    nodes = list(si)
    assert nodes == [333, "Yes", "No"]


def test_remove_node(si):
    si.append("No")

    si.remove("Yes")
    assert si.head.value == 333
    assert si.head.next.value == "No"
    assert len(si) == 2


def test_remove_invalid_node(si):
    si.append("No")

    si.remove("Maybe")
    assert si.head.value == 333
    assert si.head.next.value == "Yes"
    assert si.head.next.next.value == "No"
    assert len(si) == 3
