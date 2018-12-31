from tasks import Task
import pytest

def test_default():
    """check default value should pass"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """check member should access"""
    t = Task('buy milk', 'brain')
    assert t.summary == 'buy milk'
    assert t.owner == 'brain'
    assert (t.done, t.id) == (False, None)


def test_asdict():
    """asdict return dict should be equal"""
    t_task = Task('do something', 'ken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'ken',
                'done': True,
                'id': 21}
    assert t_dict == expected


@pytest.mark.run_replace
def test_replace():
    """replace field should pass"""
    t_before = Task('finish book', 'brain', False)
    t_after = t_before._replace(id=10, done=True)
    t_excepted = Task('finish book', 'brain', True, 10)
    assert t_after == t_excepted
