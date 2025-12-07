from lib.text import count_freq


def test_count_freq_1():
    assert count_freq(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}


def test_count_freq_2():
    assert count_freq(["bb", "aa", "bb", "aa", "cc"]) == {"aa": 2, "bb": 2, "cc": 1}
