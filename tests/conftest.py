from pytest import fixture

from App.app import hello_world

@fixture
def app():
    return hello_world()