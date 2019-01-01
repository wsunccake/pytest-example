import pytest


@pytest.fixture(name='ua')
def ultimate_answer():
    """return answer"""
    return 42


def test_ultimate_answer(ua):
    """use short name"""
    assert ua == 42
