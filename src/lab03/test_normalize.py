from lib.text import normalize

def test_normalize_1():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"

def test_normalize_2():
    assert normalize("ёжик, Ёлка", yo2e=True) == "ежик, елка"

def test_normalize_3():
    assert normalize("Hello\r\nWorld") == "hello world"

def test_normalize_4():
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"
