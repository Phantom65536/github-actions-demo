from hello import add


def test_add():
    assert 2 == add(1, 1)
    
def test_add_0():
    assert 0 == add(0, 0)
