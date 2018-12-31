import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """connect db"""
    # SETUP
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # this is where testing happen
    yield

    # TEARDOWN
    tasks.stop_tasks_db()


def test_add_return_valid_id():
    """tasks.add() should return integer"""
    # GIVEN initialize db
    # auto run initialized_tasks_db

    # WHEN new task id
    new_task = Task('do something')
    task_id = tasks.add(new_task)

    # THEN check return type
    assert isinstance(task_id, int)


def test_add_task_has_id_set():
    """make sure task_is filed is set"""
    # GIVEN initialize db
    # auto run initialized_tasks_db
    # And new task id
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    # WHEN task retrieve
    task_from_db = tasks.get(task_id)

    # THEN task_id match
    assert task_from_db.id == task_id


@pytest.mark.skip(reason='misunderstood the api')
def test_unique_id_1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.skipif(tasks.__version__ < '0.2.0', reason='no support version')
def test_unique_id_2():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """demostate xfail"""
    uid = tasks.unique_id()
    assert uid == 'a duck'


def equivalent(t1, t2):
    return t1.summary == t2.summary and t1.owner == t2.owner and t1.done == t2.done


def test_add_1():
    """tasks.get() use id"""
    task = Task('berathe', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('task',
                         [Task('sleep', done=True),
                          Task('wake', 'brain'),
                          Task('breathe', 'brain', True)])
def test_add_2(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


task_data = [Task('sleep', done=True),
               Task('wake', 'brain'),
               Task('breathe', 'brain', True)]


@pytest.mark.parametrize('task', task_data)
def test_add_3(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


task_ids = ['Task({}, {}, {})'.format(t.summary, t.owner, t.done) for t in task_data]


@pytest.mark.parametrize('task', task_data, ids=task_ids)
def test_add_4(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
