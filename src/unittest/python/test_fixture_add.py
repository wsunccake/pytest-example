import pytest
import tasks
from tasks import Task


def test_add_return_valid_id(tasks_db):
    """tasks.add() should return integer"""
    # GIVEN initialize db
    # auto run initialized_tasks_db

    # WHEN new task id
    new_task = Task('do something')
    task_id = tasks.add(new_task)

    # THEN check return type
    assert isinstance(task_id, int)


def test_fixture_data(tasks_with_multi_per_owner):
    """send data from fixture"""
    assert len(tasks_with_multi_per_owner) > 0


def test_multi_fixture(db_with_multi_per_owner):
    """multi fixture"""
    assert tasks.count() > 0


def equivalent(t1, t2):
    return t1.summary == t2.summary and t1.owner == t2.owner and t1.done == t2.done


task_data = [Task('sleep', done=True),
             Task('wake', 'brain'),
             Task('breathe', 'brain', True)]


@pytest.fixture(params=task_data)
def a_task(request):
    """task data"""
    return request.param


def test_add_3(tasks_db, a_task):
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)


task_ids = ['Task({}, {}, {})'.format(t.summary, t.owner, t.done) for t in task_data]


@pytest.fixture(params=task_data, ids=task_ids)
def b_task(request):
    """task data"""
    return request.param


def test_add_4(tasks_db, b_task):
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


def ids_func(fixture_value):
    """generate ids"""
    return 'Task({}, {}, {})'.format(fixture_value.summary, fixture_value.owner, fixture_value.done)


@pytest.fixture(params=task_data, ids=ids_func)
def c_task(request):
    """task data"""
    return request.param


def test_add_5(tasks_db, c_task):
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)
