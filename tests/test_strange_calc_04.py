import pytest
from modules import strange_calc

def test_ab_is_00():
    result = strange_calc.add_calc_if2(0, 0)
    assert 0 == result
    
def test_ab_is_20():
    result = strange_calc.add_calc_if2(2, 0)
    assert 2 == result