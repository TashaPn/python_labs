from lib.text import tokenize

def test_tokenize_1():
    assert tokenize("привет, мир!") == ["привет", "мир"]

def test_tokenize_2():
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]

def test_tokenize_3():
    assert tokenize("2025 год") == ["2025", "год"]

def test_tokenize_4():
    assert tokenize("hello,world!!!") == ["hello", "world"]

def test_tokenize_5():
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]