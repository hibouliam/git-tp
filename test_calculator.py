from calculator import addition
from calculator import division
from calculator import soustraction



def test_addition():
    assert addition(1, 2) == 3

def test_division():
    assert division(6,2)==3
def test_subsatraction():
    assert soustraction(9,4)==5