import pytest

from PythonTasks_Zadania_akademickie_2 import give_value

def test_give_value():
    # Less than 0 - boundary values
    assert give_value(-1) == 0
    # Equal 0 - boundary values
    assert give_value(0) == 0
    # Value in range (0, 100)
    assert give_value(50) == 50
    # Equal 100 - boundary values
    assert give_value(100) == 100
    # More than 100 - boundary values
    assert give_value(100) == 100
    # Another type - float
    assert give_value(100.5) == 100
    # Another type - float
    assert give_value(50.5) == 50
    # Another type - string
    assert give_value("-1") == 0
    # Another type - bool
    assert give_value(False) == 0
    # Another type - bool
    assert give_value(True) == 1
    # Another type - list
    with pytest.raises(TypeError) as error:
        give_value([1,2,3])
    assert error.typename == "TypeError"
    # Another type - tuple
    with pytest.raises(TypeError) as error:
        give_value((1,2))
    assert error.typename == "TypeError"
    # Another type - set
    with pytest.raises(TypeError) as error:
        give_value({1, 2, 3})
    assert error.typename == "TypeError"
    # Another type - dict
    with pytest.raises(TypeError) as error:
        give_value({1: 0})
    assert error.typename == "TypeError"