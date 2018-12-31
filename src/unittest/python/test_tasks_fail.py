from tasks import Task


def test_task_equality():
    """different task should not be equal"""
    t1 = Task('sit there', 'brain')
    t2 = Task('do something', 'ken')
    assert t1 == t2


def test_dict_equality():
    """different tasks compare should fail"""
    t1_dict = Task('make sandwich', 'brain')._asdict()
    t2_dict = Task('make sandwich', 'ken')._asdict()
    assert t1_dict == t2_dict
