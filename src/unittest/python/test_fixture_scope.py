import pytest


@pytest.fixture(scope='function')
def func_scope():
    """function scope"""


@pytest.fixture(scope='module')
def mod_scope():
    """module scope"""


@pytest.fixture(scope='session')
def sess_scope():
    """session scope"""


@pytest.fixture(scope='class')
def cls_scope():
    """class scope"""


def test_scope_1(sess_scope, mod_scope, func_scope):
    """test scope 1"""


def test_scope_2(sess_scope, mod_scope, func_scope):
    """test scope 2"""


@pytest.mark.usefixtures('cls_scope')
class TestSomething:
    """test class scope"""

    def test_scope_3(self):
        """test scope 3"""

    def test_scope_4(self):
        """test scope 4"""
