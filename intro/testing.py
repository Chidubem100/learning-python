import addition
import pytest 

def test_add():
    assert addition.addition(4,5) == 9
def test_sub():
  assert addition.subtraction(4,5) == -1  
