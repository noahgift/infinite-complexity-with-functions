from hello import one, two, three, main


def test_one():
    assert 2 == one(1)
    
def test_two():
    assert 3 == two(1)

def test_three():
    assert 4 == three(1)

def test_main():
    assert 7 == main(1)