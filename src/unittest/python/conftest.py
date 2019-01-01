import pytest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db(tmpdir):
    """connect db"""
    # SETUP
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # this is where testing happen
    yield

    # TEARDOWN
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_with_multi_per_owner():
    """several owner with each task"""
    return (Task('make a cookie', 'raphael'),
            Task('use an emoji', 'raphael'),
            Task('move to Berlin', 'raphael'),

            Task('create', 'michelle'),
            Task('inspire', 'michelle'),
            Task('encourage', 'michelle'),

            Task('do a handstand', 'daniel'),
            Task('write some books', 'daniel'),
            Task('eat ice cream', 'daniel'))


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_with_multi_per_owner):
    """connect db with several tasks"""
    for t in tasks_with_multi_per_owner:
        tasks.add(t)
