import pytest

from src.lab10.structures import Queue


def test_one_push_and_peek():
    qe = Queue()
    qe.enqueue("YES")
    result = qe.peek()
    assert result == "YES"


def test_three_push_and_peek():
    qe = Queue()
    qe.enqueue("YES")
    qe.enqueue("NO")
    qe.enqueue("MAYBE")

    result = qe.peek()
    assert result == "YES"


def test_two_pop():
    qe = Queue()
    qe.enqueue("YES")
    qe.enqueue("NO")
    qe.enqueue("MAYBE")

    qe.dequeue()
    result = qe.dequeue()
    assert result == "NO"


def test_len():
    qe = Queue()
    qe.enqueue("YES")
    qe.enqueue("NO")
    qe.enqueue("MAYBE")

    assert len(qe) == 3


def test_is_empty():
    qe = Queue()
    result = qe.is_empty()
    assert result == True


def test_full_is_empty():
    qe = Queue()
    qe.enqueue(2025)
    result = qe.is_empty()
    assert result == False


def test_peek_error():
    qe = Queue()
    with pytest.raises(IndexError):
        qe.peek()


def test_pop_error():
    qe = Queue()
    with pytest.raises(IndexError):
        qe.dequeue()
