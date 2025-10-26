from lib.text import *


text = "Aaa aa ++ gGa zzz ^))) !! a aAa jdsfhglkdfj ggA GGa\t\tn"

def test_all():
    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)
    topN = top_n(freq, 2)

    assert topN == [
        ("gga", 3),
        ("aaa", 2),
    ]
