import pytest

from src.lab10.structures import Stack


def test_one_push_and_peek():
    st = Stack()
    st.push("YES")
    result = st.peek()
    assert result == "YES"


def test_three_push_and_peek():
    st = Stack()
    st.push("YES")
    st.push("NO")
    st.push("MAYBE")

    result = st.peek()
    assert result == "MAYBE"


def test_two_pop():
    st = Stack()
    st.push("YES")
    st.push("NO")
    st.push("MAYBE")

    st.pop()
    result = st.pop()
    assert result == "NO"


def test_len():
    st = Stack()
    st.push("YES")
    st.push("NO")
    st.push("MAYBE")

    assert len(st) == 3


def test_is_empty():
    st = Stack()
    result = st.is_empty()
    assert result == True


def test_full_is_empty():
    st = Stack()
    st.push(2025)
    result = st.is_empty()
    assert result == False


def test_peek_error():
    st = Stack()
    with pytest.raises(IndexError):
        st.peek()


def test_pop_error():
    st = Stack()
    with pytest.raises(IndexError):
        st.pop()
