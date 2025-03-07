from twttr import shorten


def test_shorten_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("python") == "pythn"
    assert shorten("david") == "dvd"


def test_shorten_upper():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello") == "Hll"
    assert shorten("Python") == "Pythn"
    assert shorten("David") == "Dvd"


def test_shorten_capitalized():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("DAVID") == "DVD"


def test_shorten_punctuation():
    assert shorten("Twitter!") == "Twttr!"
    assert shorten("Hello!") == "Hll!"
    assert shorten("Python!") == "Pythn!"
    assert shorten("David!") == "Dvd!"


def test_shorten_numbers():
    assert shorten("Twitter123") == "Twttr123"
    assert shorten("Hello123") == "Hll123"
    assert shorten("Python123") == "Pythn123"
    assert shorten("David123") == "Dvd123"
