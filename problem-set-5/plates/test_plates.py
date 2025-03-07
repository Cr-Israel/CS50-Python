from plates import is_valid


def test_start_with_letters():
    assert is_valid("1ABCDE") == False
    assert is_valid("A1BCDE") == False
    assert is_valid("AB1234") == True
    assert is_valid("ABC123") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("AB12345") == False


def test_number_placement():
    assert is_valid("AB12CD") == False
    assert is_valid("AB0123") == False
    assert is_valid("AB123") == True


def test_alphanumeric():
    assert is_valid("AB@123") == False
    assert is_valid("AB 123") == False
    assert is_valid("AB123") == True
