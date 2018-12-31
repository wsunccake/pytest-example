import pytest
import tasks


def test_add_raises():
    """add() raise exception should fail"""
    tasks.add(task='not a Task object')


def test_add_raises_catch():
    """add() catch raise exception should pass"""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')
