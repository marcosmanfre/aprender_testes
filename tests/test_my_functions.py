import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 6
