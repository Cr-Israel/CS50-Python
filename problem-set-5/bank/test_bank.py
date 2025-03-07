from bank import value


def test_hello():
    assert value("hello") == 0


def test_hello_upper():
    assert value("Hello") == 0


def test_starts_with_h():
    assert value("hi") == 20
    assert value("how are you?") == 20
    assert value("how you Doing?") == 20


def test_starts_with_h_upper():
    assert value("Hi") == 20
    assert value("How are you?") == 20
    assert value("How you Doing?") == 20


def test_without_h():
    assert value("what's up!") == 100
    assert value("nice to see you!") == 100
    assert value("good morning!") == 100
