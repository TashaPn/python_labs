from lib.text import top_n


def test_top_n_1():
    assert top_n({"a":2,"b":3,"c":1},n=2) == [("b",3),("a",2)]


def test_top_n_2():
    assert top_n({"aa":2,"bb":2,"cc":1},n=2) == [("aa",2), ("bb",2)]
