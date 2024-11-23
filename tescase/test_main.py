from source.main import add_numbers

def test_answer():
    assert add_numbers(3,4) == 7
    assert add_numbers(4,5) == 9
    assert add_numbers(5,5) == 10