import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25

    with pytest.raises(ValueError):
        convert("5/3")

    with pytest.raises(ZeroDivisionError):
        convert("3/0")

    with pytest.raises(ValueError):
        convert("a/b")


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
