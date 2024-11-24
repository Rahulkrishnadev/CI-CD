from source.main import add_numbers,sub_numbers

def test_answer():
    assert add_numbers(3,4) == 7
    assert add_numbers(4,5) == 9
    assert add_numbers(5,5) == 10

def test_ans():
    assert sub_numbers(3,4) == -1
    assert sub_numbers(4,5) == -1
    assert sub_numbers(5,5) == 0    