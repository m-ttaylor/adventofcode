from day1 import add


def test_add_should_add_correctly():
    expected = 4
    actual = add(2, 2)
    assert expected == actual
