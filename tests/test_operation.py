from src.math_operation import addition,sub

def test_add():
    assert addition(2,3)==5
    assert addition(-1,1)==0

def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1


