from src.foo.bar import add_two

def test_add_two():
    assert add_two(2) == 4

def test_more():
    assert add_two(3) == 5